# -*- coding: iso-8859-15 -*-

"""Main HTTP routes request handlers."""

import tornado.web
import tornado.escape


class MainHandler(tornado.web.RequestHandler):
    """Handles creation of new terminals."""

    def initialize(self, db=None):
        """Stump initialization function."""
        self.db = db

    @tornado.gen.coroutine
    def get(self):
        """GET verb."""
        self.status_code(403)

    @tornado.gen.coroutine
    def post(self):
        """POST verb: Create a new terminal."""
        rows = int(self.get_argument('rows', None, 23))
        cols = int(self.get_argument('cols', None, 73))
        pid = yield self.application.term_manager.create_term(rows, cols)
        self.write(pid)


class ResizeHandler(tornado.web.RequestHandler):
    """Handles resizing of terminals."""

    def initialize(self, db=None):
        """Stump initialization function."""
        self.db = db

    @tornado.gen.coroutine
    def get(self):
        """GET verb: Forbidden."""
        self.status_code(403)

    @tornado.gen.coroutine
    def post(self, pid):
        """POST verb: Resize a terminal."""
        rows = int(self.get_argument('rows', None, 23))
        cols = int(self.get_argument('cols', None, 73))
        self.application.term_manager.resize_term(pid, rows, cols)
