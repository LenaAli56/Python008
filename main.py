# ###data types:
# #1-Sting :any thing in '' or "" 
# name1 = 'lena ali'
# print(name1)
# name2 = '''lena
# ali
# 123'''
# print(name2)
# # 2- Numbers : a- int
# num = 10
# print(num)
# # b- float
# num2=12.2
# print(num2)
# # 3- Boolen:True,Folse
# print(1==1)
# print(1==2)
# # 4-List : [1,2,3,4,5]/(changable)
# #    index 0 1 2 3 4
# lis=[1,2,3,4,5,6,7,8,9,10,0]
# print(lis)
# # 5- Tuple : {1,2,3,4,5}/(unchangable)
# tup={1,2,3,4,5,6,7,8,9,0}
# print(tup)
# # 6- Dictionary : {key:value} 
# person={'name':'Lena',
#         'age':19,
#         'job':'developer',
#         'skilles':['python','java']}
# print(person)


# ###If condition: 
# n=11
# b=20
# if(n==b):
#     print("Hello")
# elif(n>b):
#     print("Hi")
# else:
#     print("Bye")


# ###Operators in py
# # 1- Arithmatic : +,-,*,/,%,**
# x=10**4
# print(x)
# # 2-Assignment : = ,+=,-=,*=,/=,%=
# # 3-Comprison : ==,!=,>,<,<=,>=
# # 4-Logical : and,or,not
# # 5-Identity : is , is not


# ### Loop : for loop
# # for var in iterable : # iterable : list,tuple, string,dictionary

# arr={1,2,3,4,5,6,7,8,9,99,0}
# for i in arr:
#     print(i) ## output is value not index

# # for with in range
# for i in person :
#   #  print(i) # output is key 
#     print(i,":",person[i])

# # for with <,>,<=,>=
# for i in range(0,10,2):
#     print(i)
   

# n=50
# for i in range(0,n,2):
#     print(i)
# print("*"*30)
# import numbers
# choose1=input("Enter your choose : ")
# choose1=int(choose1)
# print(type(choose1))
# if choose1 != numbers:
#     print("wrong input")
# else:
#     print("corect input")

# print("*"*30)
# for i in range(1,10):
#     print(i)
    
# for i in range(10):
#     if i%2==0:
#         print(i)
#     else:
#         print("Odd")


# print("**"*30)


# # 1- function without parmeters
# def myfunction ():
#     print("Hello Word")
# myfunction()

# # 2- function with parmeters
# # def myFunction (name variable(parmeter)): 
# #       print(name variable(parmeter))
# # myFunction('hello ,word')
# def function (l):
#     print(l)
# function('Hi lena')
# def function12 (l,k):
#     print(l)
#     print(k)
# function12('Hi','lena')

# # 3- function with return

# def function123 ():
#     return(9+10)
# print(function123())

# num1=float(input("enter the fist number  "))
# num2=float(input("enter the scound number "))
# def sum(x,y): 
#     print(x ," + ",y ,"= ",end= ' ')
#     return(x+y)
# print(sum(num1,num2))

# print("**"*30)

# i=0
# wiletest=True
# while wiletest:
#     if i ==5:
#         i+=1
#         continue
#     print(i)
#     i+=1
#     if i == 10:
#         break
#*******************************************************************************************************
# list1=[{'new2':'new'},{'new3':'new'},{'new4':'new'}]
# list3=['aa','ff','a','cc','a','dd','a']
# dic1={'dic1':'dic1'}
# dic2={'dic2':'dic2'}
# list1.insert(0,dic1)
# print(list1)
# list1.insert(2,dic2)
# print(list1)
# list3.sort()
# print(list3)
# list3.reverse()
# print(list3)
# print('count a :',list3.count('a'))
# print('len in the liste is ',list3.__len__())
# # list3.clear()
# # print(list3)
# list3.pop(2)
# print(list3)

#******************************************************************************************************

## person as dic : name,age,job,skills
## let the user take a choice to add new person or see all the person
allperson=[]
person={}
print("Welcom to our app")
while True:
    print("__"*20)
    print("1- Create account ")
    print("2- login ")
    print("3- Exit ")
    choice=input("Enter your choice ")
    if choice =="1":
        name=input("Enter the user name : ")
        if allperson !=[]:
            isExited=True
            while isExited: 
                for i in allperson:
                    # i =1 person as dic
                    # #input i=c
                    # ['a','b',c'] 
                    if name==i['name']:
                        print("This name is already exist")
                        name=input("Enter the user name : ")
                        isExited=True
                        break
                    else:
                        isExited=False
        while True:
            try:
                age=int(input("Enter the user age : "))
                break
            except:
                print("Please enter a valid age")
        job=input("Enter the user job : ")
        password=input("Enter the user password : ")

        # make the name unique

        person={
            'name':name,
            'age':age,
            'job':job,
            'password':password
        }
        allperson.append(person)
        print("You added person successfully")



    elif choice =="2":
        # conter=1
        # print("__"*20)
        # print("all person : ")
        # for i in allperson:
        #     print("person",conter)
        #     for key in i :
        #         print("  ",key ,' : ',i[key])
        #     conter+=1

        print("__"*30)
        print("Please enter your name and password : ")
        name=input("Enter the user name : ")
        password=input("Enter the user password : ")
        ## if to check if the name and password is correct > are in the allperson list and dic(person)
        for i in allperson:
            if i['name']==name and i['password']==password:
                print("Welcom ",name)
                break
            else:
                print("the name or password is wrong")





    elif choice =="3":
        print("Thank you for using our app.")
        break
    elif choice =="4":
        print(allperson)
    else:
        print("wrong choice ")