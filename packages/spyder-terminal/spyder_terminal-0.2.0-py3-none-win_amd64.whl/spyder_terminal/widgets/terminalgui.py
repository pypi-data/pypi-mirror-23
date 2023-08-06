# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Spyder Project Contributors
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Terminal Widget."""

from __future__ import print_function

import sys

from spyder.config.base import _, DEV
from qtpy.QtCore import Qt, QUrl, Signal, Slot, QObject, QEvent
from qtpy.QtWidgets import (QMenu, QFrame, QVBoxLayout, QWidget, QShortcut)
from qtpy.QtGui import QKeySequence
from spyder.widgets.browser import WebView
from spyder.utils import icon_manager as ima
from qtpy.QtWebEngineWidgets import QWebEnginePage, QWebEngineSettings
from spyder.utils.qthelpers import create_action, add_actions

from qtpy.QtWebEngineWidgets import WEBENGINE


class TerminalWidget(QFrame):
    """Terminal widget."""

    def __init__(self, parent, port, path='~', font=None):
        """Frame main constructor."""
        QWidget.__init__(self, parent)
        url = 'http://127.0.0.1:{0}?path={1}'.format(port, path)
        self.view = TermView(self, term_url=url)
        self.font = font
        self.initial_path = path

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.setLayout(layout)

        self.body = self.view.document

        self.view.page().loadFinished.connect(self.setup_term)

    @Slot(bool)
    def setup_term(self, finished):
        """Setup other terminal options after page has loaded."""
        if finished:
            # This forces to display the black background
            print("\0", end='')
            self.set_font(self.font)
            self.set_dir(self.initial_path)

    def eval_javascript(self, script):
        """Evaluate Javascript instructions inside view."""
        return self.view.eval_javascript(script)

    def set_dir(self, path):
        """Set terminal initial current working directory."""
        self.eval_javascript('setcwd("{0}")'.format(path))

    def set_font(self, font):
        """Set terminal font via CSS."""
        self.font = font
        self.eval_javascript('fitFont("{0}")'.format(self.font))

    def get_fonts(self):
        """List terminal CSS fonts."""
        return self.eval_javascript("$('.terminal').css('font-family')")

    def exec_cmd(self, cmd):
        """Execute a command inside the terminal."""
        self.eval_javascript('exec("{0}")'.format(cmd))

    def is_alive(self):
        """Check if xterm is ready."""
        return self.eval_javascript('consoleReady()')


class TermView(WebView):
    """XTerm Wrapper."""

    def __init__(self, parent, term_url='http://127.0.0.1:8070'):
        """Webview main constructor."""
        WebView.__init__(self, parent)
        self.parent = parent
        self.copy_action = create_action(self, _("Copy text"),
                                         icon=ima.icon('editcopy'),
                                         triggered=self.copy,
                                         shortcut='Ctrl+Shift+C')
        self.paste_action = create_action(self, _("Paste text"),
                                          icon=ima.icon('editpaste'),
                                          triggered=self.paste,
                                          shortcut='Ctrl+Shift+V')
        self.term_url = QUrl(term_url)
        self.load(self.term_url)

        if WEBENGINE:
            self.document = self.page()
            self.document.profile().clearHttpCache()
        else:
            self.document = self.page().mainFrame()

        self.initial_y_pos = 0
        self.setFocusPolicy(Qt.ClickFocus)

    def copy(self):
        """Copy unicode text from terminal."""
        self.triggerPageAction(QWebEnginePage.Copy)

    def paste(self):
        """Paste unicode text into terminal."""
        self.triggerPageAction(QWebEnginePage.Paste)

    def contextMenuEvent(self, event):
        """Override Qt method."""
        menu = QMenu(self)
        actions = [self.pageAction(QWebEnginePage.SelectAll),
                   self.copy_action, self.paste_action, None,
                   self.zoom_in_action, self.zoom_out_action]
        if DEV and not WEBENGINE:
            settings = self.page().settings()
            settings.setAttribute(QWebEngineSettings.DeveloperExtrasEnabled,
                                  True)
            actions += [None, self.pageAction(QWebEnginePage.InspectElement)]
        add_actions(menu, actions)
        menu.popup(event.globalPos())
        event.accept()

    def eval_javascript(self, script):
        """Evaluate Javascript instructions inside DOM."""
        if WEBENGINE:
            return self.document.runJavaScript("{}".format(script))
        else:
            return self.document.evaluateJavaScript("{}".format(script))

    def wheelEvent(self, event):
        """Catch and process wheel scrolling events via Javascript."""
        delta = event.angleDelta().y()
        self.eval_javascript('scrollTerm({0})'.format(delta))

    def event(self, event):
        """Grab all keyboard input."""
        if event.type() == QEvent.ShortcutOverride:
            key = event.key()
            modifiers = event.modifiers()

            if modifiers & Qt.ShiftModifier:
                key += Qt.SHIFT
            if modifiers & Qt.ControlModifier:
                key += Qt.CTRL
            if modifiers & Qt.AltModifier:
                key += Qt.ALT
            if modifiers & Qt.MetaModifier:
                key += Qt.META

            sequence = QKeySequence(key).toString(QKeySequence.PortableText)

            if sequence == 'Ctrl+Alt+Shift+T':
                event.ignore()
                return False
            elif sequence == 'Ctrl+Shift+C':
                self.copy()
            elif sequence == 'Ctrl+Shift+V':
                self.paste()
            event.accept()
            return True

        return WebView.event(self, event)


def test():
    """Plugin visual test."""
    from spyder.utils.qthelpers import qapplication
    app = qapplication(test_time=8)
    term = TerminalWidget(None)
    # term.resize(900, 700)
    term.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    test()
