#Write a function called remove_capitals. remove_capitals
#should accept one parameter, a string. It should return a
#string containing the original string with all the capital
#letters removed. Everything else should be in the same
#place and order as before.
#
#For example:
#
# remove_capitals("A1B2C3D") -> "123"
# remove_capitals("WHAT") -> ""
# remove_capitals("what") -> "what"
#
#Remember, capital letters have ordinal numbers between 65
#("A") and 90 ("Z"). You may use the ord() function to get
#a letter's ordinal number.
#
#Your function should be able to handle strings with no
#capitals (return the original string) and strings with all
#capitals (return an empty string). You may assume we'll
#only use regular characters (no emojis, formatting
#characters, etc.).


#Write your function here!
def remove_capitals(string):
    #Create string with value ""
    res = ""
    #Looping through each character of the input s
    for i in string:
        #Check the character is not an upper case
        if (not i.isupper()):
            #Add non upper
            res += i
    #return result
    return res

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#123
#eorgia nstitute of echnology
print(remove_capitals("A1B2C3D"))
print(remove_capitals("Georgia Institute of Technology"))


ORRRR


#We first write a function called remove_capitals as told in the
#instructions with the parter of a string.

def remove_capitals(String):

#We are asked to remove all the capitals and are given
#the range 65 and 95. We take advantage of this as we
#know that each character in python has an ordinal number.
#
#There are two ways of going about this problem. You could
#either compare the characters or compare ordinal numbers
#
#Note: It is easier to compare characters since you do not have
#to memorize any values!
#
#You can check solution 2 if you want to see how the problem 
#can be solved using ordinal numbers. For this solution, I’ll be
#using characters.
#
#The way we want to approach this is to traverse through
#the given string, and only have characters which are not
#capital letters remaining.
#
#We MUST create an empty string because strings are
#immutable!

	ans = ""

#We use a for-loop because we know exactly the 
#number of times we want to iterate.

	for char in String:

#Within this for-loop we write an if-statement to filter out
#which character is a capital letter or not.

		if char < "A" or char > "Z":

#Notice that we are looking for characters that are less than
#”A” and greater than “Z”. This is because everything in between
#is a capital letter. (Pretty logical)
#If the condition passes, then we know we can concatenate it to our
#empty string.

			ans += char

#Once we are done traversing through the entire
#string and have filtered out the character we want, we
#write a return statement with the answer!

    return ans
    
    
   
ORRRRR



#The thought process is the same as solution 1, but the one
#thing that is different is how we write our conditional in order
#to determine whether the character we are traversing through
#in the string is a capital letter or not.

def remove_capitals(String):
    ans = ""
    for char in String:

#Notice that we have to use ord(char) in order to
#have python know that we are going to be using the ordinal number
#of the character. If you write:
#char < 65 
#you will error since you are comparing a string with an int.
#If you know your ordinal numbers, you can take this approach, but
#visually, I would say that it is easier to see what you are comparing
#when you are simply comparing strings.

        if ord(char) < 65 or ord(char) > 90:
            ans += char
    return ans
