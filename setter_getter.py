class Student:
    def __init__(self, name):
        self.__name = name
    #
    # def get_name(self):
    #     return self.__name
    #
    # def set_name(self, new_name):
    #     if ' ' in new_name:
    #         raise Exception('')
    #     self.__name = new_name
    #
    # def delete_name(self):
    #     raise Exception('Нельзя удалять name')
    #
    # name = property(get_name, set_name, delete_name)




    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if ' ' in new_name:
            raise Exception('В имени не должно быть пробелов')
        self.__name = new_name

    @name.deleter
    def name(self):
        raise Exception('Нельзя удалять name')


s = Student('Jannat')
print(s.name)

s.name = 'Жаннат'
print(s.name)



# print(s.get_name())
# s.set_name('Жаннат')
# print(s.get_name())

