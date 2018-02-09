import app.controllers.board_controller as board_controller
import app.controllers.post_controller as post_controller
import app.controllers.index_controller as index_controller

def get_routes():
    return [
        (r"/", index_controller.IndexHandler),
        (r"/boards", board_controller.ListHandler),
        (r"/posts", board_controller.ListHandler)
    ]

