# class Clinet:
#     name="Lena"
#     age=19
#     city="Irbid"

# clinet1=Clinet()
# print(clinet1.name)


#class has attributes and methods
#what is the difference between atributes and methods
###attributes : are varibales
###method : are functions


class Person ():
    def __init__(self,name,age,job,skills,password):
        self.name = name
        self.age = age
        self.job = job
        self.skills = skills
        self.password=password


    def nameAndAge(self):
     return f'name : {self.name} , age : {self.age}'
    
    def callPerson(self,person):
       return f'{self.name} is calling {person}'
    
    def __str__(self):
     return f"name : {self.name} , age : {self.age} , job : {self.job} , skills : {self.skills} "

person1=Person(age=19,skills=['python','java','js'],name='lena',job='developer')
person2=Person(age=20,skills=['java','js'],name='ali',job='developer')
print(person1)
print(person2.callPerson('Ziad'))
print(person2.nameAndAge())
        











