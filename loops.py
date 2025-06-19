
    # looping statements 
    # programming tools that allow a block of code to be executed 
    # it will executed repeatedly until a specific condition is met
    # there are few types they are 1= for loop ,,2=while loop ,,3=nested loop....
    # for loop Used for iterating over a sequence (like a list, tuple, string, or range).
    
    # for loop 
    
    #  used for iterating over a secquence 
    #  Executes a block of code for each item in the sequence.
    #  Ideal when the number of iterations is known beforehand.
    #  it execuits only certine number of times as per the user 
   

#  Range = start , stop , step 
#  range = n-1s
 

# for i in range (5): 
#     print (i)

# here in this example we gave only one value in range 
# so it consider the value as the number of times the loop should run in a range
# we didn't gave any value to i so it automaticaly consider value from 0
# for i in range (3,10):
#     print("value ofi is",i)

#   value ofi is 3
#   value ofi is 4
#   value ofi is 5
#   value ofi is 6
#   value ofi is 7
#   value ofi is 8
#   value ofi is 9 

# in this example we can see that there are two values in range 
# now as per the range the s3 start , stop , step .
# the first value will be consider as starting value the second value will be consider as where the loop should stop
# the loop will automaticaly stop when the output reachs the range at given value 10.

# for i in range (111,120,2):
#     print("value of i is",i)

# # value of i is 111
# value of i is 113
# value of i is 115
# value of i is 117
# value of i is 119

# in the above example we gave three values in range 
# so as per the range (start,stop,step) 
# the first value is start the sccond value is stop the third value is step 
# the out put will be as shown in above



#  nested for loop 

# for i in range (5):
#     for k in range (3):
#         print("k is",k)

# for i in range(3):
#     for j in range(3):
#         print ("*",end=" ")
#     print() # this is helps to print the output in next line

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()


# for i in range(3):
#     for j in range (3):
#         print("A",end=" ")
#     print()



# for i in range (1,4):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()    

# a=1
# for i in range (1,4):
#     for j in range (1,i+1):
#         print(a,end=" ")
#         a+=1
#     print()    

# for i in range(0,4):
#     for j in range(1,i+1):
#         print("a",end=" ")
#     print()        


# a="*"
# for i in range (5,1):
#     for j in range(j,i+1):
#         print(a,end=" ")
#         a=a*a+1
#     print()        

# for i in range(4):
#    for j in range (1,i+1):
#        print("a",end=" ")
#    print()

# for i in range(5):
#     x='*'
#     x=x*(5-i)
#     print(x)


# for i in range(1,5):
#     x='*'
#     x=x*i
#     print(x)

# # for i in range(1,5):
# #     for j in range(i):
# #         print('*',end="")
# #     print()


# # for i in range(1,5):
# #     for j in range(3):
# #         print(i,j)
# #     print()        

# # for i in range (1,4):
# #     for j in range(1,4):
# #         for k in range(4):
# #             print(i,j,k)
# #         print()


# # a=5

# # for i in range(1,5):
# #     s=' '*(a-i)*2
# #     h='1'*i
# #     print(s+h.strip())


# # for i in range(1,4):
# #     for j in range(1,i+1):
# #         print("*")

# for i in range (1,4):
#     print("  " *(3-i),end="")
#     for j in range (1,i+1):
#         print(j,end=' ')
#     print()  
#     output=

#                  1 
#                1 2 
#              1 2 3
   

# # for i in range (3):
# #     for j in range(3):
# #         print("A",end="")

# # ord =it is a key word that is used to number to char 
# # ascii = 
# a="A"
# for i in range (3):
#     for j in range(3):
#         print(a,end=" ")
#         a= chr( ord(a) + 1)
           
#     print()
# #    output =
# #              A B C 
# #              D E F 
# #              G H I

# a="A"
# for i in range (1,4):
#     for j in range(1,4):
#         print(a,end=" ")
#         a= chr( ord(a) + 1)
#     a="A" 
#     print()
# #    out put =
# #             A B C
# #             A B C
# #             A B C

# for i in range(1,11):
#     print("2 x",i,"=",i+2 )
# # 2 table using for loop
b=1
for b in range(1,9):
    if b==4:
        continue
    if b==6:
        continue
    print(b)
    
#    # out put =
#    # 1
#    # 2
#    # 3
#    # 5
#    # 6
#    # 8
#    # 9


# a=1
# while a<=10:
#     print("2 x",a,"=",a*2)
#     a+=1
# # 2 table using while loop

# a=1
# for i in range(1,11):
#         print("5 x",a,"=",a*5)
#         a+=1
# out put = 5 table using for loop


a="A"
for i in range(1,4):
    print("  "*(3-i),end=" ")
    for j in range(1,i+1):
        print(a,end=" ")
        a=chr(ord(a)+1)
    print()
   
#      out put==
#                      A
#                    B C
#                  D E F
# a="A"
# for i in range(1,4):
#     print(" "*(3-i),end=" ")  # the only difference is here we gave single space and above we gave double space
#     for j in range(1,i+1): 
#         print(a,end=" ")
#         a=chr(ord(a)+1)
#     print()    
#  output==
#              A
#             B C
#            D E F

a=1
for i in range(1,4):
    print("  "*(3-i),end=" ")
    for j in range (1,i+1):
        print(a,end=" ")
        a+=1
    print()    
    # out put ==

    #                1
    #              2 3
    #            4 5 6