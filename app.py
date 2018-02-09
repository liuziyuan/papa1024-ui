import tornado
import config.routes as router

def init_app():
    return tornado.web.Application(
        router.get_routes()
    )

if __name__ == "__main__":
    print('hello tornado')
    app = init_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
