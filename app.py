import tornado.ioloop
import tornado.web
import config.routes as router

def application():
    return tornado.web.Application(
        router.get_routes()
    )

if __name__ == "__main__":
    print('hello tornado')
    app = application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
