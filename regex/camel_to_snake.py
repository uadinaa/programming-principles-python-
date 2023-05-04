import re 
 
def camel_to_snake(obj): 
  return obj.group("g1")+ "_" + obj.group("g2").lower() 
 
text = input() 
x = "(?P<g1>[a-z])(?P<g2>[A-Z])+" 
 
print(re.sub(x, camel_to_snake, text))