##### Charmingpython.com #####
 
f = open('my_file.txt', 'r')

file_contents = f.read()

print(file_contents)

f.close()

# need to remember the close so we use a context manager instead





##### Charmingpython.com #####

# File Context Manager


with open('my_file.txt', 'r') as f:
    file_contents = f.read()
    print(file_contents)
    
# context managers are availabe for a variety of purposes and save you considering resource management
