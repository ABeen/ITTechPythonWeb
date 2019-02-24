import tornado.web
from logic.user import get_user, get_range


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        index = int(self.get_argument('index', 1))
        size = int(self.get_argument('size', 10))

        return self.render('index.html', index=index, size=size)


class AuthorHandler(tornado.web.RequestHandler):
    def get(self):
        author, range, pen = get_user()
        return self.render('author.html', data=author )


class Author1Handler(tornado.web.RequestHandler):
    """ 作者处理逻辑
    """
    def get(self):
        author, range, pen = get_user()
        asd = get_range()
        return self.render('author1.html', info=range, data=asd)




__all__ = ['IndexHandler', 'AuthorHandler', 'Author1Handler']




