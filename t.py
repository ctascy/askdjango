class Person(object):#object는 넣어라
    def __init__(self, name):
        self.name = name


person = Person('sosi')
print(person.name)
