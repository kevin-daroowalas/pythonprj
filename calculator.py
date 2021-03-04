print('hello this is a program coded in python')
print(' ')
print('This program will imitate a calculator with 4 funtions')
print(' ')
print('The functions are addition - substraction - multiplication and division')
print(' ')
print('You can do a successive additon - substration - multiplication or division according to how many number you enter')
print(' ')
print('You can also choose how many number you want to enter')
print(' ')
num = float(input('Please enter the number of values you would like to do the functions mentionned above :' ))
list_num = []
i=0
val=0
for i in range (0,int(num)):
  if i==0:
    val=float(input('Please enter the first value :'))
    list_num.append(val)
    i+=1
  else:
    val=float(input('Please enter the next value : '))
    print('this was the ',i+1,' value')
    list_num.append(val)
    i+=1
    
option_operation = int(input('Select the function by entering the number corresponding to the funtion 1- Addition 2- Substraction 3- Multiplication 4- Division : '))

if option_operation == 1 :
  print('You have chosen to add !!! ')
  add=0
  k=0
  for k in range (0,len(list_num))):
    add+= list_num[k]
    print('Result ',k + 1,' = ',add,' !') 
    
   print(add ,'is the final result')
