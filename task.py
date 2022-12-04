'''
DAY:sunday
DATE:4th  dec 2022
TOPIC:task
AUTHOR:pooja
'''
#name_id_salary
name=input('enter name:')
id=int(input('enter id:'))
salary=float(input('enter salary:'))
print(f'name is: {name},id is: {id}, salary is:{salary}') #name is:pooja,id is:40,salary is:3.5
#sum and avg of 3 numbers
a,b,c=5,4,3
sum=a+b+c
print(sum)#12
avg=sum/3
print(avg)#4.0
#area of circle
r=int(input('enter the radius:'))#2
py=22/7
area=py*r**2
print('the area of circle is %.2f' %area)#the area of circle is 12.57
#get_char_display
c=input('enter the char:')#pooja
print('the char is:'+c[4])#the char is:a
#joining_strings
a='pooja'
b='12'
print(a+b)#pooja12
#cube_numbers(2 ways)
a=4
print(a**3)#64
for i in range(1,5):
  print(i**3,end=" ")#1 8 27 64