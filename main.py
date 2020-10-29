import requests
import json

print('Welcome to my Project Guntenberg search app. You can search for thousands of free ebooks for which the US copyright has expired.')
print()

def title():
  title_search = input('Enter all or part of a title to search: ')
  print()
  response = requests.get(f'http://gutendex.com/books?search={title_search}')
  transform = response.json()

  for item in transform["results"]:
      print(item["title"])
      print(' ' * 4, 'Author: ', item["authors"][0]["name"])
      print(' ' * 4, 'Book Shelf: ', item["bookshelves"])
      print()

def author():
  author_search = input('Enter all or part of the author\'s name to search: ')
  print()
  response = requests.get(f'http://gutendex.com/books?search={author_search}')
  transform = response.json()

  for item in transform["results"]:
      print(item["title"])
      print(' ' * 4, 'Author: ', item["authors"][0]["name"])
      print(' ' * 4, 'Book Shelf: ', item["bookshelves"])
      print()

def subject():
  subject_search = input('Enter the subject to search: ')
  print()
  response = requests.get(f'http://gutendex.com/books?topic={subject_search}')
  transform = response.json()

  for item in transform["results"]:
      print(item["title"])
      print(' ' * 4, 'Author: ', item["authors"][0]["name"])
      print(' ' * 4, 'Additional Subjects: ', item["subjects"])
      print()

backdoor = " "
while backdoor != "exit":
  print('With this app you can search by title, author, or subject. Please make your selection: ')
  backdoor = input()
  if backdoor == 'title':
    title()
  elif backdoor == 'author':
    author()
  elif backdoor == 'subject':
    subject()
  else:
    print('Please pick one of the three options.')

print('Yall come back now hear')




