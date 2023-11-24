###data types:
#1-Sting :any thing in '' or "" 
name1 = 'lena ali'
print(name1)
name2 = '''lena
ali
123'''
print(name2)
# 2- Numbers : a- int
num = 10
print(num)
# b- float
num2=12.2
print(num2)
# 3- Boolen:True,Folse
print(1==1)
# 4-List : [1,2,3,4,5]/(changable)
#    index 0 1 2 3 4
 
lis=[1,2,3,4,5,6,7,8,9,10,0]
print(lis)
# 5- Tuple : {1,2,3,4,5}/(unchangable)
tup={1,2,3,4,5,6,7,8,9,0}
print(tup)
# 6- Dictionary : {key:value} 
person={'name':'Lena',
        'age':19,
        'job':'developer',
        'skilles':['python','java']}
print(person)


###If condition: 
n=11
b=20
if(n==b):
    print("Hello")
elif(n>b):
    print("Hi")


###Operators in py
# 1- Arithmatic : +,-,*,/,%,**
x=10**4
print(x)
# 2-Assignment : = ,+=,-=,*=,/=,%=
# 3-Comprison : ==,!=,>,<,<=,>=
# 4-Logical : and,or,not
# 5-Identity : is , is not


### Loop : for loop
# for var in iterable : # iterable : list,tuple, string,dictionary

arr={1,2,3,4,5,6,7,8,9,99,0}
for i in arr:
    print(i) ## output is value not index

# for with in range
for i in person :
  #  print(i) # output is key 
    print(i,":",person[i])

# for with <,>,<=,>=
for i in range(0,10,2):
    print(i)
   

n=50
for i in range(0,n,2):
    print(i)

  