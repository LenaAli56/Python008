allaccount=[]
account={}
print("Welcom to our app ")
while True:
    print("__"*50)
    print('1- Create new account : ')
    print('2- Long in your account : ')
    print('3- Exet .')
    choice=input('Enter your choice : ')
    if choice =='1':
        name=input('Enter the user name : ')
        
        while True:
            try:
                age=int(input('Enter the user age : '))
                break
            except:
                print('Please enter void number')
        job=input('Enter the user job : ')
        password=input('Enter the password : ')
        account={
            'name':name,
            'age':age,
            'job':job,
            'password':password
               }
        allaccount.append(account)
        print("The account has been created successfully")

    elif choice=='2':
        print('Please enter your name and password')
        name=input('Enter the user name : ')
        password=input('Enter the password : ')
        for i in allaccount :
            if i ['name']==name and i['password']==password:
                print('Welcom ',name)
                break
            else:
                print('The name or password is wrong')
            




    elif choice=='3':
        print("Thank you for using our app.")
    elif choice=='4':
        print(allaccount)
    else:
        print('Wrong choice')
