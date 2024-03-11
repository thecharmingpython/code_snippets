##### Charmingpython.com #####

#In Python we frequently return values that are tuples

my_items = ('a','b','c')
print (my_items)
   
str1, str2, str3 = my_items
print(str1, str2, str3)

# but sometime you only want one of the values

str1, _, _ = my_items # tells python we are not using the first

str1, *strs = my_items # strs now holds last 2 vars
print(str1, strs)

*strs, str3  = my_items # strs now holds first 2 vars
print(strs, str3)