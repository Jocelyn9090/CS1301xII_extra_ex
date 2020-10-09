#Imagine you're writing the software for an inventory system for
#a store. Part of the software needs to check to see if inputted
#product codes are valid.
#
#A product code is valid if all of the following conditions are
#true:
#
# - The length of the product code is a multiple of 4. It could
#   be 4, 8, 12, 16, 20, etc. characters long.
# - Every character in the product code is either an uppercase
#   character or a numeral. No lowercase letters or punctuation
#   marks are permitted.
# - The character sequence "A1" appears somewhere in the
#   product code.
#
#Write a function called valid_product_code. valid_product_code
#should have one parameter, a string. It should return True if
#the string is a valid product code, and False if it is not.


#Add your code here!
def valid_product_code(string):
    if(len(string)%4 == 0):
        for x in string:
            if(not (x.isdigit() or x.isupper())):
                return False
        if("A1" in string):
            return True
    return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, False
print(valid_product_code("A12B44BP"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
print(valid_product_code("A1BBD5"))
print(valid_product_code("BDD5664S"))
print(valid_product_code("66aBSaA1fdsv"))



ORRR



#As always, we start by writing the function name and parameters:

def valid_product_code(String):

#The first thing we want to check is the length of the String. If it is
#not a multiple of 4, there is not reason for us to do anything as we
#can simply return False.

    if len(String) % 4 != 0:
        return False
    found = False

#We create a boolean “found” which will later be used in the code
#
#If the String length is a multiple of 4, then we have to iterate through
#the String and check for two things. Rather than having two for-loops
#we can check both conditions at the same time. Having two for-loops
#makes your code inefficient, which is something you do NOT want.
#
#We write a for-loop because we know how many times we want to
#iterate, and notice that our range is from 0 to len(String - 1).
#
#Note when you have:
#in range(0, len(String - 1)) we end at the second last index.

    for index in range(0, len(String) - 1):

#Now we need.a conditional that will catch any character within the String
#that is not an uppercase or number.

        if (String[index] < '0') or (String[index] > '9' and String[index] < 'A') or (String[index] > 'Z'):     
            return False

#Notice that there is an and statement when comparing to see if it is greater
#than ‘9’ but less than ‘A’. This is because of the order of the ASCII table. If
#we had an “or” instead, the conditional would trigger the String[index] > 9
#even if the letter was a lowercase.
#
#The second conditional is where we look to see if “A1” exists. Since the
#way we set our for loop allows us to access the appropriate index, we
#check to see if the current String[index] and String[index] add up to “A1”.
#If it does, then we set our found variable to be True.
#The reason why we have a found variable rather than have that condition
#return True is because f we were to have a product code of “A1btT” it
#would return True even though it is not a correct product code since the
#second condition is triggered. Thus, we store the boolean value in found 
#and return that value at the end.
#We have to initially store the boolean value as False because we have not
#found “A1” yet. However, when we do, we CAN return True if the product
#code does not have any lower or non numbers which is checked by
#our first condition.

        if String[index] + String[index+1] == "A1":
            found = True

    return found
