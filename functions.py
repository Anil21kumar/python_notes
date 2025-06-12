# it is set of block of code which is used for some specific task 
# the same function can be used as many times as we need just by calling the function
# def is a key word by using def we create a function
# syntax of this is = def function_name ():
#                        block of code
#                     functionname() this is function calling
def add ():
    a=12
    b=13
    c=a+b                    # block of code---this is example of user define funcion
    print('value of c',c)
add()    # function call
# out put is 25

# there are two types of function 1=user define function,--devolaper will create as per user need  
#                                 2=in built function -- these are present in the librery ex=print,input,list,float,type,etc...

# in user define function there are two typesfunction without parameters and function with parameters
def add (a,b):
     c=a+b
     print(c)
add(2,3) # here we gave values for paremeters that given in function 

def anil(a=6,b=3):
    c=a*b
    print(c)
anil(5,6) # we can give values or it will consder a=2,b=3 as defult values
    
# out put is 30 it wil not take the defult values because we specificaly enterd values 5,6
def anil2(a=4,b=3):
    c=a*b
    print(c)
anil2(3) # we gave only single value it consider for a now a=3 and b value will be default value so b=3
def anil3(a=4,b=3):
    c=a*b
    print(c)
anil3(b=9) # the value of b=9 because we specificly we gave b=9,the a value is default value


def add(a,b):
    c=a*b
    print(c)
    
def sub(c=3,d=3):
    f=c+d
    print(f)
add(8,8)
sub(4)


def int(a,b):
    d=a+b
    print(d)
int(2,8)

def list(a,b):
    c=a*b
    print(c)
list(3,3)

def none(f=3,t=5):
    y=f*t
    print(y)
none()    
