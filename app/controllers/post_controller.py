import tornado.web

class ListHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, post list")