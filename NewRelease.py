days_since_release = 14
original_price = 60
greatest_hits = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a conditional that determines the price of a
#newly-released game, movie, or album based on the time since
#it was released.
#
#Assume that a new release loses $2 off its price for every
#full week since it was released. So, two full weeks (14 days)
#after a $60 game is released, it will cost $56.
#
#However, if the release is considered a "greatest hit", it
#loses value half as fast: after two weeks, it will be $58
#instead of $56.
#
#No release will ever fall to below $20, however, no matter
#how fast it loses value or whether it's a greatest hit.
#
#Add some code below to print the current price of the release.
#For example, with the values above, it would pring $58.


#Add your code here! Make sure to print the dollar sign, too.

week = 7
now = days_since_release // week
prices = 2

if greatest_hits:
    prices -= 1

maxs = 20
final = original_price - (now * prices)

if final < 20:
    final = maxs
else:
    final = final
   
print("${}".format(final))




ORRR



#We have to first write an if-else statement to determine
#whether the music is a greatest hit or not.
#If the song is a greatest hit, then the value decreases
#half as fast as compared to a song that isn’t a greatest hit
#
#We have to do floor division since for cases such as 17 days
#only two full weeks have passed
#
#Notice that we don’t write greatest_hit == True. This is not
#necessary because greatest_hit is a boolean value and
#if/elif blocks are automatically triggered when the condition
#is a True value

if greatest_hits:
    loss = days_since_release // 7
else:
    loss = days_since_release // 7 * 2

#We update the price from its original price by subtracting
#the amount of depreciated, which we found from the
#if-statement above
#
#You can have original_price on the left OR create a new
#variable. It will depend on whether you may need the
#original price or not

price = original_price - loss

#This if-statement determines whether the new price is greater
#then 20. If it is, we print the new price, if not, we simply print
#$20
#
#Notice that we have to convert the price to string because
#price is an int.

if price > 20:
    print("$" + str(price))
else:
    print("$20”)
