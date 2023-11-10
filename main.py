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
        if allperson !=[]:
            isExited=True
            while True:
                for i in allperson:
                    #i =1 person as dic
                    if name ==i['name']:
                        print("this name is already exist")
                        name=input('enter the user name : ')
                        isExited=True
                        break
                    else:
                        isExited=False
        while True:
            try:
                age=input("Enter the person age : ")
                break
            except:
                print("Please enter valid age : ")
                
        job=input("Enter the person job : ")
        skills=[]
        while True:
            try:
                counter2=input('enter the number of skills')
                break
            except Exception as e:
                print('please enter a void number ')
                continue
        for i in range(counter2):
            print('enter the skill number',i+1,'; ')
            skills.append(input)
        person['name']=name
        person['age']=age
        person['job']=job
        person['skills']=skills
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
    
 





  