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
  


#person as dic :name , age , job , skills
#let the user take a choice to add new person or see all the persons 
allperson=[]
person={}
print('Welcom to our app')
while True:
    print('__'*20)
    print('1- Add new person')
    print('2- See all persons' )
    print('3- Exit')
    choice=input("Enter your choice : ")
    if choice =='1':
        name=input("Enter the person name : ")
        # while True:                  طريقة 2
        #      age=int(input('Enter the user age : '))
        #      if age.isdigit()==False:
        #          print('Please enter void number')
        #          continue        
        # else:
        #     break
        while True:
            try:
                age=int(input('Enter the person age : '))
                break
            except:
                print('please enter a void number ')
                continue
        job=input('Enter the person job : ')
        person ={
            'name':name,
            'age':age,
            'job':job}
        allperson.append(person)
        print('**Your add person successfuly ')



    elif choice=='2':
        counter = 1
        print('__'*20)
        print('all person : ')
        for i in allperson:
           print('person ',counter)
           for key in i:
               print('     ',key,':',i[key])
           counter+=1
               

               
    else:
        print('Thank you for using our app.')
        break


