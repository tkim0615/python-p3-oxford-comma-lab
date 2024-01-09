import ipdb
def oxford_comma(items):
      if len(items) == 1:
         return items[0]
      elif len(items) == 2:
         return ' and '.join(items)
      else:
        items[-1] = 'and ' + items[-1]
        return ', '.join(items)

print(oxford_comma(['kiwi', 'banana', 'hel']))





# Write a function oxford_comma() in the lib/oxford_comma.py file that takes an array of string elements as 
# an argument and converts it into a string using the Oxford commaLinks to an external site..

# oxford_comma(["fiddleheads", "okra", "kohlrabi"])
# # => "fiddleheads, okra, and kohlrabi"
# Hint: You will need to refer to the section above about converting lists into strings, but note that coding
# this function will involve a couple of extra challenges.

# This might be a challenging lab, so take your time using Google and playing around with your code.
#  Good luck and have fun!