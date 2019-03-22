import tornado.ioloop
import tornado.web
from os import environ

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(environ.get("PORT", 5000))
    tornado.ioloop.IOLoop.current().start()
