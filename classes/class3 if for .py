#We will lear about how to deal with if else condition in python and how to take input from user
# choose=input("Enter your choose ")
# print(choose)
# print(type( choose))
# choose=float(choose)
# print(type( choose))



import numbers
choose1=input("Enter your choose : ")
choose1=int(choose1)
print(type(choose1))
if choose1 != numbers:
    print("wrong input")
else:
    print("corect input")

for i in range(1,10):
    print(i)
    
for i in range(10):
    if i%2==0:
        print(i)
    else:
        print("Odd")