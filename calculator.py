print('hello this is a program coded in python')
print(' ')
print('This program will imitate a calculator with 4 funtions')
print(' ')
print('The functions are addition - substraction - multiplication and division')
print(' ')
print('You can do a successive additon - substration - multiplication or division according to how many numbers you enter')
print(' ')
print('You can also choose how many number you want to enter')
print(' ')
num = float(input('Please enter the number of values you would like to do the functions mentionned above :' ))
list_num = []
i=1
val=0
for i in range (1,num):
  if i==1:
    val=float(input('Please enter the first value :'))
    list_num.append(val)
    i+=1
  else:
    val=float(input('Please enter the next value : '))
    print('this was the ',i,' value')
    list_num.append(val)
    i+=1
