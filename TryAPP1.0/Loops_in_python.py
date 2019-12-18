# loops in python
    #for loops
primes=[2,3,5,7,11]
for x in primes:
    print(x)

for x in range(5):
    print(x)

for x in range(3,6):
    print(x)

for x in range(2,7,3):
    print(x)

count=0;
while(count<5):
    print(count)
    count+=1

#Break and continue statements work same as in c, cpp
b=1
while b < 6:
    print(b)
    break
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)


#UNLIKE C and C++ you can use else block with for loops also
#When the loop condition of "for" or "while" statement fails then code part in "else" is executed.
# If break statement is executed inside for loop then the "else" part is skipped.
# Note that "else" part is executed even if there is a continue statement.
# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

