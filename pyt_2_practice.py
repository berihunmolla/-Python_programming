'''def first_fun():
    a=10
    b=25
    sum=a+b
    print('the sum is:',sum)
first_fun()

dob_year=1994
cur_year=2014
age= cur_year-dob_year
if age>=18: # 20>=18
  print(age,' is greater than the requerd age , the individual can participate in election')
else:
    print('the induvidual can not pariticipate in the election')
    

score = 55
if score>=90 and score <=100:
    print('your grade is: A+')
    print('you are first class student')
elif score >=85 and score < 90:
    print('your grade is A')
elif score>=80 and score <85:
    print(' your grade is A-')
elif score >=75 and score <80:
    print(' your grade is B+')
elif score>=70 and score <75:
    print(' your grade is B')
elif score>=65 and score <70:
    print(' your grade is B-')
elif score>60 and score <65:
    print(' your grade is C+')
elif score>=50 and score <60:
    print(' your grade is C')
elif score>=45 and score <50:
    print(' your grade is C-')
elif score>=40 and score <45:
    print(' your grade is D')
elif score<40:
    print(' your grade is F')
else:
    print(' your course grade is incommplete')
  



n=10
if n==0:
    print(' the number is zero')
else:
    print('the number is different from zero')
    if n>0:
         print(n,' is greater  than zero')
    else:
         print('the number is lessthan zero')
         

def first_while():
    i=1
    t=input('please enter the loop limit')
    n=int(t)
    while(i<=n):   # 10<=10
         print(i)
         i=i+1
first_while()

def fibo():
    len=10
    z=0
    x=1
    i=0
    if len <=0:
        print('please enter the length greater than zero')
    elif len==1:
        print(' fibo sequence'.format(len),':')
    else:
        print('the fibonacy sequence is ,...'.format(len),':')
        while(i<len):
            print(x,end=',')
            a=z+x
            z=x
            x=a
            i+=1
fibo()


def even_natural():
    i=1
    lim=100
    while(i<=lim):
        if i%2!=0:
           print(i,',')
           i+=1
        else:
            i+=1
even_natural()

'''

def forLoop():
    sum=0
    num_value = [1,5,10,15,20,25,30,35]
    for i in num_value:
        sum+=i
        print(sum)
forLoop()

