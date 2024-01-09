# import ipdb
# def oxford_comma(items):
#       if len(items) == 1:
#          return items[0]
#       elif len(items) == 2:
#          return ' and '.join(items)
#       else:
#         items[-1] = 'and ' + items[-1]
#         return ', '.join(items)

# print(oxford_comma(['kiwi', 'banana', 'hel']))



def oxford_comma(list):
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return ' and '.join(list)
    elif len(list) >= 3:
      list[-1] = 'and ' + list[-1]
      print(list)
      return ', '.join(list)
print(oxford_comma(['kiwi', 'banana', 'hel']))
    
   

# Write a function oxford_comma() in the lib/oxford_comma.py file 
# that takes an array of string elements as an argument and converts
# it into a string using the Oxford commaLinks to an external site..

# oxford_comma(["fiddleheads", "okra", "kohlrabi"])
# # => "fiddleheads, okra, and kohlrabi"