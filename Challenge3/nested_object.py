# getkey value should be passed and it will retur
# if user passes getkey = 'a', value will be {'b': {'c': 'd'}}
# if user passes getkey = 'b', value will be {'c': 'd'}
# if user passes getkey = 'c', value will be d

def get_all_values(nested_dictionary,parameter):
    for key, value in nested_dictionary.items():
        if type(value) is dict:
           get_all_values(value, parameter)
           if key == parameter:               
               print(key, "-->", value)
        else:
           if key == parameter: 
               print(key, "-->", value)


object = {'a': { 'b': {'c': 'd' } } }

object1 = {'x': { 'y': {'z': 'a' } } }

print("getting Value for Key: a ")
get_all_values(object , parameter='a')

print("getting Value for Key: b ")
get_all_values(object, parameter='b')

print("getting Value for Key: c ")
get_all_values(object, parameter='c')

print("getting Value for Key: x ")
get_all_values(object1 , parameter='x')

print("getting Value for Key: y ")
get_all_values(object1, parameter='y')

print("getting Value for Key: z ")
get_all_values(object1, parameter='z')


