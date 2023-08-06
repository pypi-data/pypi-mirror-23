# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
#

"""Tests for the plugin."""

# Test library imports

import os
import pytest
import requests
import os.path as osp
from qtpy.QtWebEngineWidgets import WEBENGINE

# Local imports
import spyder_terminal.terminalplugin
from spyder_terminal.terminalplugin import TerminalPlugin
from spyder.py3compat import getcwd


LOCATION = os.path.realpath(os.path.join(os.getcwd(),
                                         os.path.dirname(__file__)))
LOCATION_SLASH = LOCATION.replace('\\', '/')

TERM_UP = 10000
WINDOWS = os.name == 'nt'

CLEAR = 'clear'
if WINDOWS:
    CLEAR = 'cls'

PWD = 'pwd'
if WINDOWS:
    PWD = 'cd'


def check_pwd(termwidget):
    """Check if pwd command is executed."""
    if WEBENGINE:
        def callback(data):
            global html
            html = data
        termwidget.body.toHtml(callback)
        try:
            return LOCATION in html
        except NameError:
            return False
    else:
        return LOCATION in termwidget.body.toHtml()


@pytest.fixture(scope="module")
def setup_terminal(qtbot):
    """Set up the Notebook plugin."""
    terminal = TerminalPlugin(None)
    qtbot.addWidget(terminal)
    terminal.create_new_term()
    terminal.show()
    return terminal


def test_terminal_font(qtbot):
    """Test if terminal loads a custom font."""
    terminal = setup_terminal(qtbot)
    qtbot.wait(TERM_UP)

    term = terminal.get_current_term()
    port = terminal.port
    status_code = requests.get('http://127.0.0.1:{}'.format(port)).status_code
    assert status_code == 200
    term.set_font('Ubuntu Mono')
    fonts = term.get_fonts()
    assert fonts == "'Ubuntu Mono', 'Ubuntu Mono', monospace"
    terminal.closing_plugin()


def test_terminal_tab_title(qtbot):
    """Test if terminal tab titles are numbered sequentially."""
    terminal = setup_terminal(qtbot)
    qtbot.wait(TERM_UP)
    terminal.create_new_term()
    num_1 = int(terminal.tabwidget.tabText(0)[-1])
    num_2 = int(terminal.tabwidget.tabText(1)[-1])
    assert num_2 == num_1 + 1
    terminal.closing_plugin()


def test_new_terminal(qtbot):
    """Test if a new terminal is added."""
    # Setup widget
    terminal = setup_terminal(qtbot)
    qtbot.wait(TERM_UP)

    # Test if server is running
    port = terminal.port
    status_code = requests.get('http://127.0.0.1:{}'.format(port)).status_code
    assert status_code == 200

    terminal.create_new_term()
    term = terminal.get_current_term()
    qtbot.wait(1000)
    # Move to LOCATION
    # qtbot.keyClicks(term.view, 'cd {}'.format(LOCATION))
    # qtbot.keyPress(term.view, Qt.Key_Return)
    term.exec_cmd('cd {}'.format(LOCATION_SLASH))

    # Clear
    # qtbot.keyClicks(term.view, 'clear')
    # qtbot.keyPress(term.view, Qt.Key_Return)
    term.exec_cmd(CLEAR)

    # Run pwd
    # qtbot.keyClicks(term.view, 'pwd')
    # qtbot.keyPress(term.view, Qt.Key_Return)
    term.exec_cmd(PWD)

    # Assert pwd is LOCATION
    qtbot.waitUntil(lambda: check_pwd(term), timeout=TERM_UP)

    terminal.closing_plugin()


def test_output_redirection(qtbot):
    """Test if stdout and stderr are redirected on DEV mode."""
    spyder_terminal.terminalplugin.DEV = True
    terminal = setup_terminal(qtbot)

    stdout = osp.join(getcwd(), 'spyder_terminal_out.log')
    stderr = osp.join(getcwd(), 'spyder_terminal_err.log')
    assert osp.exists(stdout) and osp.exists(stderr)
    terminal.closing_plugin()
