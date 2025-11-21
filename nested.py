Concept : Nested IF 



for i in range(0, 3):
    print(i)


 starting point => 0
ending point => 3 , excluded
output => 0,1,2


Nested Loop => loop inside another loop.



in 1st for loop:
starting point => 0 
ending point => 3 , excluded


for i in range(0, 2):    ##  2 times 

    print("this is my first for loop")
    for j in range(0,1):   ## 1 time

        print("the value of i: ", i, "the value of j:", j)


Phase 1
starting point => 0 , value of i 
ending point => 3 , excluded
=> condition check ( 0 < 3) TRUE
=> perform task , inside loop 
=> value of i = 0  ----------------------

first task : print("this is my first for loop")
second task : 

## inside 2nd for loop 
staring point => 0
ending point => 1
=> value of j = 0 ----------------


value of i is incremented by 1 , i++ , 0 + 1 => 1


staring point => 1 , value of i 
ending point => 2 
check condition ( i < 2) , 1< 2 => TRUE
=> enter in the loop 
=> 1st task: print("this is my first for loop")
=> 2nd task: run second loop