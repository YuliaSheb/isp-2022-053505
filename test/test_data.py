class Person(object):
    weight = 50
    heigth = 165
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return 'Hello ' + self.name

person = Person("John")

def myprint(i):
    print(i)
    return i*2

list_data = ['this', 'is', 'a', 'simple', 'list', 35]
tuple_data = ('one', 'two', 'three')
complex_list_data = ['this', 'is', 'a', [1, 'complex', 'list', True]]
dict_data = {"lang": "Python", "complexity": "high", "time": 22}
complex_dict_data = {"lang": "Python", "time": 22, "value": ['one', 'two', 3]}
int_data = 100
float_data = 120.345
bool_data = True
str_data = 'my string to serialization'