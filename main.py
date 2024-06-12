
def main():
  book_path = "books/frankenstein.txt"
  book = get_text(book_path)
  count = count_words(book)
  print(f"There are {count} words in the book.")



def get_text(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents


def count_words(book):
  list = book.split()
  return (len(list))

main()

def char_count():
  dict = {}
  book_path = "books/frankenstein.txt"
  book = get_text(book_path)
  book = book.lower()
  for char in book:
    if char in dict:
      dict[char] = dict[char] +1
    else:
      dict[char] = 1
  print(dict)

  