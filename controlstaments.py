# there are twothree types of cntrol statements 
# these are the conditional statements 1=if ,2= if else ,3=if elseif 
# nestedif , nested if else ,nested ifelse if and ladder
a=99
b=45
c=90
# example for if condition 
if (a<b):
    print ("a is greater than b")

# out put is a is greater than b

# example for if else 
if (a>b):
    print("a is lesser than b")
else:
    print("a is greater tha b")    




# example for if else if 
if (a==b):
    print('a is equal to b')
elif(a<=c):
    print("a is lesser than or equal to b")
elif(a>b):
    print ('somthing happen')    
else:
    print('you are greate') 

# nested conditions are nested if,nested if else ,nested if else if,..
#  if we write the condition in side the condition then we called it as nested condition 
#  nested if  block example     
if (a>b):
    print ("i m in if  in if block ")
    if (a>b):
       print("iam in inner if block")
    else:
        print("out of box")
else:
    print(' iam in else block')

# ladder this is also a looping stament that
#  in a sub condition there will be another sub condition that is called ladder           
if (a>b):                            # main condition
    print ("i m in if  in if block ")
    if (a>b):                         # first sub condition 
       print("iam in inner if block")
       if (a>b):                       # second sub condition we can add we per recquired
           print ('a is grater than b')
       else :
           print('a is lesser than b')  
    else:
        print("out of box")
else:
    print(' iam in else block')


 