
def main():
  book_path = "books/frankenstein.txt"
  book = get_text(book_path)
  word_count = count_words(book)
  char_dict = char_count(book)
  print("--- Begin report of books/frankenstein.txt ---")
  print(word_count," words found in the document")
  print("")
  for entry in char_dict:
    print(f"The'{entry['letter']}' character was found {entry['times']} times")
  print("--- End report ---")
  



def get_text(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents


def count_words(book):
  list = book.split()
  return (len(list))



def char_count(book):
  """this get the text, turns it into lowercase, then makes a dictionary of characters and occurences
  then goes through this dict, makes sure the character is a letter, and makes a list of dictionaries 
  with the format "letter":letter, "times":times, this gets sorted using the sort_on function which i
  dont really get
  for future: make report using this info and the other stuff required on boot.dev
  """
  dict = {}
  list_of_dicts = []
  book = book.lower()
  for char in book:
    if char in dict:
      dict[char] = dict[char] +1
    else:
      dict[char] = 1
  for entry in dict:
    if entry.isalpha():
      temp = {"letter":entry,"times":dict[entry]}
      list_of_dicts.append(temp)
  list_of_dicts.sort(reverse=True, key=sort_on)
  return (list_of_dicts)    

def sort_on(dict):
  return dict["times"]

main()