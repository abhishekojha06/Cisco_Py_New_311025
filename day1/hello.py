# name = 'Abhishek' #stored in heap memory
# name = 'Abhishek'  #reference count of actual memory location

# Abhishek = name

def greet(name):
    result = f'Hello {name}'
    return result

def Hi(name):
    result = f'hi {name}'
    return result

person = input('name: ')
print(f'Hello {person}')

print(greet(person))
print(Hi(person))