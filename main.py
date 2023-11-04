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
                

  