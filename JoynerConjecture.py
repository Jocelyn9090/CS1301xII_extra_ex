#The Joyner Conjecture is a not-at-all famous mathematical
#series inspired by the Collatz Conjecture for use in this
#class.
#
#The Joyner Conjecture proceeds as follows:
#
#Start with any number. If the number is divisible by 3,
#divide it by 3. Otherwise, add 2 to the number. Eventually,
#no matter what number you begin with, this series will run
#into 1 or 2. If it runs into 1, it will repeat 1-3 forever.
#If it runs into 2, it will repeat 2-4-6 forever.
#
#For example, imagine we started with the number 5:
#5 is not divisible by 3, so 5 + 2 = 7
#7 is not divisible by 3, so 7 + 2 = 9
#9 is divisible by 3, so 9 / 3 = 3
#3 is divisible by 3, so 3 / 3 = 1
#
#Start with 5, this sequence converges on 1 in 4 iterations:
#5 -> 7, 7 -> 9, 9 -> 3, 3 -> 1.
#
#Write a function called joyner. joyner should have one
#parameter, an integer. It should return the number of
#iterations required to reach either 1 or 2 for the first
#time.


#Add your code here!
def joyner(n):
    count = 0
    while(n!=1 and n!=2):
        if(n%3 == 0):
            n = n // 3
        else:
            n += 2
        count += 1
    return count
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 4, 5, and 10, each on their own lines.
print(joyner(5))
print(joyner(15))
print(joyner(29))



ORRRRR



#We start by writing the function name and parameters as instructed.

def joyner(num):

#Because we want to count the number of iterations required to reach
#either 1 or 2, we create a count variable that will increment every iteration.

    count = 0

#Since we do not know how many iterations is required for the number
#to reach 1 or 2, we use a while loop and set a condition when we want the
#loop to end.
#We want to finish when the number is either 1 or 2, so in code it translate to:

    while (num != 1) and (num != 2):

#We only pass in num when it is not 1 or 2.
#
#Within the while loop, we have to check if the number is divisible by 3.
#If we were to reword that, it would be a number when divided by 3 has
#no remainder. Thus the condition would look like this:

        if num % 3 == 0:

#Within the if-condition, we are asked to divide the number by 3 and then 
#repeat the cycle, so we simply restore the new value of num, increment
#count by one, since we are done with one iteration.

            num = num / 3
            count += 1

#If the num cannot be divisible by 3, we have to add 2. We write this by having
#an else statement, since we add 2 in ALL other cases. We update the num
#increment count and end that iteration.

        else:
            num += 2
            count += 1

#Once the num, after count number of iterations, becomes either 1 or 2
#we return the count. Thus, it must be outside the while loop.

    return count
