allaccount=[]
account={}
print("Welcom to our app ")
while True:
    print("__"*50)
    print('1- Create new account : ')
    print('2- Long in your account : ')
    print('3- Exit .')
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
        while True:
            password=input('Enter the password : ')
            upperChar=False
            lowerChar=False
            numberChar=False

            if len(password)>=8:
                for i in password:
                    if i.isupper():
                        upperChar=True
                    elif i.islower():
                        lowerChar=True
                    elif i.isdigit():
                        numberChar=True
               
                while True:
                      if upperChar ==False:
                       print('you need a upper char ')
                       break
                      elif lowerChar == False:
                          print('you need a lower char ')
                          break
                      elif numberChar==False:
                          print('you need a number  ')
                          break
                      elif upperChar and lowerChar and numberChar:
                          print('The password is strong ')
                          break 
                      else :
                         print('The password is not strong ')
            else :
              print('The password is shorter than 8 char')


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
                print("__"*20)
                print('1- read a book')
                print('2- add a book')
                print('3- buy a book')
                print('4- update your account ')
                print('5- delete your account ')
                print('6-logout ')
                choiceBook=input('Enter your choice: ')
                if choic
                break
            else:
                print('The name or password is wrong')
            




    elif choice=='3':
        print("Thank you for using our app.")
    elif choice=='4':
        print(allaccount)
    else:
        print('Wrong choice')
