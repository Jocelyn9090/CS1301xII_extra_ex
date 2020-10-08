#Write a function called valid_release_date. The function
#should have two parameters: a date and a string. The
#string will represent a type of media release: "Game",
#"Movie", "Album", "Show", and "Play".
#
#valid_release_date should check to see if the date is
#a valid date to release that type of media according to
#the following rules:
#
# - Albums should be released on Mondays.
# - Games should be released on Tuesdays.
# - Shows should be released on Wednesdays or Sundays.
# - Movies should be released on Fridays.
# - Plays should be released on Saturdays.
#
#valid_release_date should return True if the date is
#valid, False if it's not.
#
#The date will be an instance of Python's date class. If
#you have an instance of date called a_date, you can
#access an integer representing the day of the week with
#a_date.weekday(). a_date.weekday() will return 0 if the
#day is Monday, 1 if it's Tuesday, 2 if it's Wednesday,
#up to 6 if it's Sunday.
#
#If the type of release is not one of these strings,
#the release date is automatically invalid, so return
#False.

from datetime import date

#Write your function here!
def valid_release_date(a_date, string):
    if(type(a_date)!=date and type(string)!=str):
        return False
    if a_date.weekday() == 0:
        if string == "Album":
            return True
        else:
            return False
    elif a_date.weekday() == 1:
        if string == "Game":
            return True
        else:
            return False
    elif a_date.weekday() == 2 or a_date.weekday()==6:
        if string == "Show":
            return True
        else:
            return False
    elif a_date.weekday() == 4:
        if string == "Movie":
            return True
        else:
            return False
    elif a_date.weekday() == 5:
        if string == "Play":
            return True
        else:
            return False
    return False

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, False, each on their own line.
print(valid_release_date(date(2018, 7, 11), "Show"))
print(valid_release_date(date(2018, 7, 11), "Movie"))
print(valid_release_date(date(2018, 7, 11), "Pancake"))


ORRRR



#The first thing that should come to your mind after you
#read this problem is that we need a lot of conditionals.
#
#As always, we start by writing the function name and parameters
#which are all stated in the instructions.

def valid_release_date(date, string):

#Once we have done that, the instructions give us a way to represent
#days of the week with numbers so that it is convenient for us to compare
#values in our conditions.

	day = date.weekday()

#The line above works because we import date from datetime.
#As explained in the instructions, we are able to access the day of
#the week by writing “date.weekday()”. If you want to know more about
#the date class, you can google it, but this is outside the scope of this course.
#
#Keeping in mind that 0 is Monday, 1 is Tuesday, so on and so forth
#we write the conditions with respect to the day and the type of media
#that should be released on that day.

    if day == 0 and string == "Album":
        return True
    elif day == 1 and string == "Game":
        return True
    elif (day == 2 or day == 6) and string == "Show":
        return True
    elif day == 4 and string == "Movie":
        return True
    elif day == 5 and string == "Play":
        return True

#Notice that we use elif. It is convention to use elif when listing multiple
#conditionals, rather than having multiple if-statements.
#
#Lastly, we have an else statement that returns False if none of the
#conditions are met

    else:
        return False
