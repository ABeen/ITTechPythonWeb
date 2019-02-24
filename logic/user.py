
def get_user():
    author = {"age": 40, "name": "zm", "address": "dongying"}
    range = "two miles"
    pen = ["pak", "英雄"]
    return author, range, pen


def get_range():
    return "five bags"


__all__ = ["get_user", "get_range"]
