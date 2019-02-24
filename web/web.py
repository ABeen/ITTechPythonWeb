import tornado.web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


def run(debug=True, port=8888, handlers=None, callback=None):
    if not handlers:
        print("handlers is ：", handlers)
        return

    settings = {"template_path": './template',
                "debug": debug,
                "port": port}

    app = tornado.web.Application(handlers, **settings)
    app.handlers = handlers

    if callback:
        callback(app)

    server = HTTPServer(app)
    server.bind(settings['port'])
    server.start()
    IOLoop.instance().start()


__all__ = ['run']
