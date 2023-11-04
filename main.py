 #python 
allperson=[]
person={}
print("Welcom to our app")
while True:
    print("_"*20)
    print("1-Add new person")
    print("2- see all persons")
    print("3- exit")
    choise=input("Enter your choise : ")
    if choise =="1":
        name=input("Enter the person name : ")
        # while True:
        #     age=input("Enter the person age : ")
        #     if age.isdigit()==False:
        #         print("Please enter valid age : ")
        #         continue
        #     else :
        #         break
        while True:
            try:
                age=input("Enter the person age : ")
                break
            except:
                print("Please enter valid age : ")
                
        job=input("Enter the person job : ")
        person['name']=name
        person['age']=age
        person['job']=job
        allperson.append(person)
        print("Add your person successfully")
    elif choise =="2":
        counter=1
        print('_'*20)
        print('all persons : ')
        for i in allperson:
            print("person",':',counter)
            for key in i:
                print('     ',key,':',i[key])
            counter+=1
    else:
        print("Thanks")
        break
                

  