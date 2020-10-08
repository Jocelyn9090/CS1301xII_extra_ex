#Write a function called num_factors. num_factors should
#have one parameter, an integer. num_factors should count
#how many factors the number has and return that count as
#an integer
#
#A number is a factor of another number if it divides
#evenly into that number. For example, 3 is a factor of 6,
#but 4 is not. As such, all factors will be less than the
#number itself.
#
#Do not count 1 or the number itself in your factor count.
#For example, 6 should have 2 factors: 2 and 3. Do not
#count 1 and 6. You may assume the number will be less than
#1000.


#Add your code here!
def num_factors(n):
    total = 0
    for x in range(2,n):
        if n % x == 0:
            total +=1
    return total

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 0, 2, 0, 6, 6, each on their own line.
print(num_factors(5))
print(num_factors(6))
print(num_factors(97))
print(num_factors(105))
print(num_factors(999))



ORRRR



#We first write the function name and have one
#parameter, as written in the instructions

def num_factors(num):

#We declare a variable that will count the number
#of factors the input num will have.

    count = 0

#We use a for loop because we know the number
#of iterations we have to go through for this problem
#We start from 2 because 1 does not count as a factor
#and end in the number because the number itself 
#is not a factor either
#
#The rule for factors is that when you divide the factor
#to the number, the remainder is 0. In code, you use
#the modulus operator to represent that. As shown, when
#the num and i is divided, it must equal 0 to be a factor.
#Since the count increment is only passed through when
#we verify that the current i value is a factor, we can return
#the count at the end which tells us the number of factors it has

    for i in range(2, num):
        if num % i == 0:
            count += 1
    return count
