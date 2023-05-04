import os
import string

for i in string.ascii_uppercase:
    d = open(i + ".txt", "w")
    d.close()