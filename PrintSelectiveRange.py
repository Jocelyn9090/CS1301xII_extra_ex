minimum = 5
maximum = 14
even = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write a loop (we suggest a for loop) that prints the numbers
#from minimum to maximum, including minimum and maximum
#themselves. If even is True, print only the even numbers.
#If even is False, print only the odd numbers. You may assume
#minimum will always be less than maximum.
#
#With the initial values for minimum, maximum, and even above,
#this should print 6, 8, 10, 12, 14 -- each number would be on
#its own line, no commas.


#Add your code here!

for number in range(minimum, maximum +1):
    if number %2 ==0:
        if even == True:
            print("{}".format(number))
else:
    for number in range(minimum, maximum +1):
        if number %2 !=0:
            if even == False:
                print("{}".format(number))
                
                
ORRRR



#We have to traverse through all the values between the
#minimum and maximum. Thus, it is appropriate to use a
#for loop since we the range.
#
#The first if-statement inside the for loops checks to see if we 
#are looking for even values. If so, then it goes to the next
#if statement to make sure it only prints the even. If not, we
#only print the odd number, which would have a remainder 
#of 1 when divided by 2.
#
#Notice that we have to use maximum + 1 because there may
#be cases where the maximum value may be part of the 
#expected output.
#
#Notice that we don’t have to write even == True because
#even is a boolean value, making it redundant.

for num in range (minimum, maximum + 1):
    if even:
        if num % 2 == 0:
            print(num)
    else:
        if num % 2 == 1:
            print(num)
