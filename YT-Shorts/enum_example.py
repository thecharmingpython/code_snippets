##### Charmingpython.com #####

counting = ['zero','one','two','three','four','five']

for i in range(0, len(counting)):
    print(i, counting[i])
    
# or

index = 0
for number in counting:
    print(index, number)
    index +=1






##### Charmingpython.com #####

# better use enum
for index, number in enumerate(counting):
    print(index, number)

# change the index start number
counting_from_1 = ['one','two','three','four','five']

for index, number in enumerate(counting_from_1, start=1):
    print(index, number)