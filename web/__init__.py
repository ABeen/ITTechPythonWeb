from .web import *
from .handlers import IndexHandler, AuthorHandler,Author1Handler

my_handlers = [(r"/", IndexHandler), (r"/red", AuthorHandler),(r"/Author1", Author1Handler)]
