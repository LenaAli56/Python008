#class2 
page={'title1':'Kingdom of Jordan'}
page1={'title2':'Egypation Republic'}
page2={ 'welcom':'Welcome to Kingdom of Jordan page',
        'subject':'Jordan is an Arab Islamic country,it is located on the continent of Asia,its capital is Amman'}
page3={ 'welcome':'Welcome to Egypation Republic page',
        'subject':'Egypt is an Arab Islamic country,it is located on the continent of Africa ,its capital is Cairo'}
for i in page:
    print(page[i])
    for j in page2:
        print(' ',page2[j])
    for n in page1:
        print(page1[n])
    for o in page3:
        print(' ',page3[o])

