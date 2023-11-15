# a=3
# b=4
# b,a=a**2,b-2
# c=0
# print(a,b)
# while b>2:
#     c=b+a
#     b-=2
#     print(c,a,b)

a=0
sum=0
while True:
    print(a)
    a+=1
    sum+=a
    if a==10:
        break
print('sum = ',sum)