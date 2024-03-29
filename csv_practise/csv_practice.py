import utils
import sorts

bookshelf = utils.load_books('books.csv')
long_bookshelf = utils.load_books('books_long.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
    return len(book_a['title_lower']) > len(book_b['title_lower'])


sorts.merge_sort(long_bookshelf, by_total_length)

for book in long_bookshelf:
    print("{} by {}".format(book['title'], book['author']))
