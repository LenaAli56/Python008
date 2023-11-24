allperson=[]
person={}
print("Welcom to our app ")
while True:
    print('__'*30)
    print("1- Create accuont ")
    print("2- Login ")
    print("3- Exit ")
    choice=input("Enter your choice ")
    if choice == "1":
        name=input("Enter the user name : ")
        while True :
            age=input("Enter the user age : ")
            if age.isdigit()==False:
                print("Please enter a volid age")
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
        print("you aaded an account seccessfully ")


    elif choice == "2":
        print("__"*30)
        print("Please enter your name and pasword : ")
        name=input("Enter the user name : ")
        password=input("Enter the user password : ")
        for i in allperson:
            if i['name']==name and i['password']==password:
                print("Welcom ", name)
                break
            else:
                print("The name or password is wrong")
                


    elif choice =="3":
        print("Thank you for usind our app ")
        break


    elif choice =="4":
        print(allperson)

        
    elif choice =="5":
       print("your choice is wrong")
