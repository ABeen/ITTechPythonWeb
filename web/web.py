import tornado.web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        index = int(self.get_argument('index', 1))
        size = int(self.get_argument('size', 10))

        return self.render('index.html', index=index, size=size)


def run(debug=True, port=8888, callback=None):
    settings = {"template_path": './template',
                "debug": debug,
                "port": port}
    
    handlers = [(r"/", IndexHandler)]
    app = tornado.web.Application(handlers, **settings)
    app.handlers = handlers

    if callback:
        callback(app)

    server = HTTPServer(app)
    server.bind(settings['port'])
    server.start()
    IOLoop.instance().start()


__all__ = ['run']
