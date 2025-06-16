
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
 

for i in range (5): 
    print (i)

# here in this example we gave only one value in range 
# so it consider the value as the number of times the loop should run in a range
# we didn't gave any value to i so it automaticaly consider value from 0
for i in range (3,10):
    print("value ofi is",i)

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

for i in range (111,120,2):
    print("value of i is",i)

# value of i is 111
# value of i is 113
# value of i is 115
# value of i is 117
# value of i is 119

# in the above example we gave three values in range 
# so as per the range (start,stop,step) 
# the first value is start the sccond value is stop the third value is step 
# the out put will be as shown in above



