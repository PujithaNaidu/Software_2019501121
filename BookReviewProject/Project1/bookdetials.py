from models import db, Books


def get_book_details(title):
    b = Books.query.get(title)
    return b
