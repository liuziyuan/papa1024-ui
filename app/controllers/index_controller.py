import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, index page")