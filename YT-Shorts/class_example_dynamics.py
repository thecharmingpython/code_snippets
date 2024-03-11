##### Charmingpython.com #####

class Animal():
    pass


animal = Animal()

#dynamically add attributes to a class

#animal.type = "dog"
#animal.noise ='bark!'

#print (animal.type)
#print (animal.noise)

#or use setattr

type_key = 'type'
type_val = 'dog'





setattr(animal, type_key, type_val)

print (animal.type)



