# if elif else statments
x=10
y=90
if x==y:
    print(x,' is greater than ',y)
else:
    print(y,' is greater than ',x)

z=5
if z>0:
    print(z,' is greater than zero')
elif z<0:
    print(z,' is less than zero')
else:
    print(z,' is equal to zero')
# boolean
is_raining =True
if is_raining:
    print('please, take your raincoat')
else:
    print('go out freely')
    
is_student = False
if is_student:
    print(' please study hard for your future')
else:
    print('what is your job,......')
weather = 'fogy'
if weather == 'rainy':
    print(' please take your raincoat')
elif weather== 'fogy':
     print('the day seems very fogy')
else:
    print('go out freely')
    

userinput = input('please enter the weather : ')
weather =userinput.lower()

if weather == 'rainy':
    print(' please take your raincoat')
elif weather== 'fogy':
     print('the day seems very fogy')
else:
    print('go out freely')

# student grade using condition
grade= input(' please enter the grade of the student : ')
grade =int(grade)
if grade >=90 and grade<=100:
             print('the student grade is = :A')
elif grade >70 and grade<90:
             print('the student grade is = :B')
elif grade >50 and grade<70:
             print('the student grade is = :c')
else:
    print(' the student grade is F')
# for loops
for x in range(3):  # x=0 initialy by default
    print('x=',x)
for z in range(1,10,2):  # initialization z=1,  top limit z=10, increament z=2
    print('   z=',z)
# uppend method/ fuction
university= ['amu','aau','ddu','bdu','ju']
un=[]
for uni in university:
    un.append(uni.upper())
print(un)
'''
total_3 = 0
for num in range(4,16,1):
    total_3 += num
    print(total_3)

print(total_3+6)
'''
sum=0
for t in range(1,10,2):
    sum= sum + t
    print(sum)
print('the sum is :',sum)
 
#while loop
sum2=0
c=0
while c<10:
    c = c + 1
    sum2 = sum2 + c
    print('the sum2 is: ',sum2)

# functions
def first_function():
    print('this is the first python function')

first_function()

input_op = input('enter the operator')
val1= input('enter the first operand')
val1= int(val1)
val2= input('enter the second operand')
val2 = int(val2)
def cal_fun():
    if input_op == '+':
        sum= val1 + val2
        print('the sum of',val1,' and ',val2,'=',sum)
    elif input_op == '-':
        pro= val1-val2
        print('the difference of',val1,' and ',val2,'=',dif)
    elif input_op == '*':
        pro= val1*val2
        print('the product of',val1,' and ',val2,'=',pro)
    else:
        div= val1/val2
        print('the dividend of',val1,' and ',val2,'=',div)
cal_fun()
