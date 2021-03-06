#Imagine you're playing a game in which every action you
#take grants you some number of experience points. There is
#an item called a Lucky Egg that, when used, doubles the
#number of experience points you earn. The company behind
#the game also runs occasional events where they increase
#how many experience points you earn for each action by 50%,
#100%, or even 200%.
#
#Write a function called find_total_exp. find_total_exp
#should have one positional parameter, a base number of
#experience points. It should also have two keyword
#parameters: lucky_egg, whose default value is False, and
#event_mulitplier, whose default value is 1.
#
#The function should return the number of experience
#points earned based on these two variables. The base number
#of experience points should always be multiplied by the
#event multiplier, and then doubled if lucky_egg is True.
#
#You should convert the final result from a float to an
#integer before returning it. This will automatically round
#down.


#Add your code here!
def find_total_exp(points, lucky_egg = False, multiplier = 1):
    if lucky_egg:
        points*=2
    else:
        points=points
    hs = points * multiplier
    return int(hs)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#100
#200
#150
#300
print(find_total_exp(100))
print(find_total_exp(100, lucky_egg = True))
print(find_total_exp(100, multiplier = 1.5))
print(find_total_exp(100, lucky_egg = True, multiplier = 1.5))


ORRRR



#We first write the function name as told in the instructions.
#
#The difference between a positional parameter and keyword
#parameter is that keyword parameters have a default value.
#You can override the default value by putting a new value in
#the parameter when using the function. If we do not put a value
#for the keyword parameter, it automatically uses the value that
#is set. Examples will be at the end for further explanation if needed.

def find_total_exp(base_num, lucky_egg = False, multiplier = 1):

#The mathematics in the return statement is simply multiplying
#the base_num and multiplier as stated in the instructions.
#
#As for the lucky_egg variable, in the instructions, it tells
#us that we have to double the value when it IS a lucky egg.
#In Python, False has a value of 0 and True has a value of 1.
#Therefore, we can use this to our advantage and +1.
#This works because when it is NOT a lucky egg, we just
#want the value of base_num * multiplier. When it IS a
#lucky egg we want double the value, thus if we add 1
#to the True value, we get 2, thus getting double the
#base_num * multiplier
#
#Finally, we have to cast the entire calculation as
#an int. This is because we have to convert the final
#result from a float to an int before returning it

    return int(base_num * multiplier * (lucky_egg + 1))

#As for a further explanation on keyword parameters
#you can override the default value by simply including
#it without your parameters. As shown in the test case
#print(find_total_ex(100, lucky_egg = True, multiplier = 1.5)
#the value of lucky_egg is changed to True, and multiplier
#changed to 1.5. If we did not include those parameters
#when using the function, lucky_egg would stay as False
#and multiplier would stay as 1.
