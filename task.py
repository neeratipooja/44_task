'''
DAY:sunday
DATE:4th  dec 2022
TOPIC:task 
AUTHOR:pooja
'''
#even_odd
for i in range(1,20,2):
  print(i,end=',') #1,3,5,7,11,13,15,17,19,21
for i in range(2,20,2):
  print(i,end=',')  #2,4,6,8,10,12,14,16
#even_odd_zero
n=int(input('enter the value:'))
if(n%2==0):
  print(f'{n} is even number')#6 is even number
else:
  print(f'{n} is odd number')   #5 is odd number