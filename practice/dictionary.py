#dictionaries
dictionary = {
    'a': [1,2,3] ,
    'b': 'hello' ,
    'c': True ,
    'x': 'mic testing'
}

my_list = [
    {
    'a': [1,2,3] ,
    'b': 'hello' ,
    'c': True
    } ,
    {
    'a': [1,2,3] ,
    'b': 'hello' ,
    'c': True
     }
]

print(my_list[1]['b'])
print(dictionary['a'])
print(dictionary['x'])
print(dictionary.keys())
print(dictionary.popitem())

