allperson=[]
person={}
print("Welcom to our app ")
while True:
    print("__"*30)
    print("1- Create account ")
    print("2- Login ")
    print("3- Exit ")
    choice=input("Enter your choice ")
    if choice =='1':
        name=input("Enter the user name : ")
        while True:
            age=input("Enter the user age : ")
            if age.isdecimal()==False:
                print("Please enter a valid age")
                continue
            else:
                break
        job=input("Enter the user job : ")
        password=input("Enter the user password : ")
        person={
            'name':name,
            'age':age,
            'job':job,
            'password':password
        }
        allperson.append(person)
        print("You added an account seccessfully")


    elif choice == '2':
        print("Please enter your name and password : ")
        name=input("Enter the user name : ")
        password=input("Enter the user password : ")
        for i in allperson :
            if i['name']==name and i['password']==password:
                print("Welcom ",name)
                break
            else:
                print("Your name or password is wrong ")


    elif choice =='3':
        break
    elif choice =='4':
        print(allperson)
    else:
        print("Your choice is wrong")