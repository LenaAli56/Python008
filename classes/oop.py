class Person():
    def __init__(self,name,age,job,skills):
        self.name=name
        self.age=age
        self.job=job
        self.skills=skills
    def __str__(self):
        return f'name : {self.name}, age : {self.age} , job : {self.job} , skills : {self.skills}'
    def name2age(self):
        return f'name : {self.name} , age : {self.age}'
    def callPerson(self,person):
        return f'{self.name} is calling {person}'
    
person=Person("Lena",19,"programer",['python','java','HTML'])
print(person.callPerson('Hussam'))
