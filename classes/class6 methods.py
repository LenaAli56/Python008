#method in list : append() , insert() , remove() , pop() , clear() , sort() , reverse() , count() , _len_()
#  insert() : اضافة عنصر الى ليست مع تحديد موقع الاضافة  
#  remove(): تحذف عنصر واحد من ليست
#  sort():تقوم بترتيب العناصر تصاعديا او تنازليا 
#  reverse(): تقوم بطباعة العناصر عكسيا
#  count():عدد تكرار العنصر اللي انا بحدده
#  __len__():عدد العناصر الموجودة داخل ليست
#  clear():حذف جميع العناصر
#  

#method in dic : key() , values() , items() , get()
dic1 = {
    'name':'lena',
    'age':19,
    'job':'developer',
    'skills':['python','java' ,'js']
     }

#keys method : to get all the keys in the dic
print(dic1.keys())
#values method : to get all the values in the dic
print(dic1.values())
#items method : to get all the item in the dic  
print(dic1.items())
#get method : to get value of the key
print('get method ',dic1.get('name'))
# dic1={'name1':'ali'}
# print(dic1)
dic1['skills'].append('html')
dic1['skills'].remove('java')
dic1['skills'].insert(1,'css')
print(dic1)

list1=[{'new2':'new'},{'new3':'new'},{'new4':'new'}]
list3=['aa','ff','a','cc','a','dd','a']
dic1={'dic1':'dic1'}
dic2={'dic2':'dic2'}
list1.insert(0,dic1)
print(list1)
list1.insert(2,dic2)
print(list1)
list3.sort()
print(list3)
list3.reverse()
print(list3)
print('count a :',list3.count('a'))
print('len in the liste is ',list3.__len__())
# list3.clear()
# print(list3)
list3.pop(2)
print(list3)























# list1=[{'new':'new'},{'new1':'new1'},{'new2':'new2'}]
# dic1={'dic1':'dic1'}
# dic2={'dic2':'dic2'}
# list1.insert(0,dic1)
# print(list1)
# list1.insert(3,dic1)
# print(list1)
# # list3.sort()
# list3=['aa','lr','65','p','w','999']
# list3.sort()
# print(list3)
# list3.reverse()
# print(list3.count('7'))
# print(list3.__len__())
# list3.remove('aa')
# print(list3)
# # list3.clear()
# # print(list3)
# list3.pop(2)
# print(list3)



