from random import randrange

from inheritance.main import Human


class Native(Human):
    def __init__(self, name, date_of_birth,gender,height,phone):
        super().__init__(name,date_of_birth,gender,height)
        self.phone = phone
        self._id = self.generate_id()

    @staticmethod
    def generate_id():
        return "scv" + str(randrange(1000,999999))


    def __str__(self):
        return f'''
        {super().__str__()}
        Phone :{self.phone}
        ID :{self._id}'''


person = Native("Edwin","22-03-1995","Male","6.2","09096041561")
print(person)