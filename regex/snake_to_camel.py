import re
def snake_to_camel(word):
  return ''.join(x.capitalize() or '_' for x in word.split('_'))

text = input()
print(snake_to_camel(text))