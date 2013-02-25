#!/usr/bin/python
print("Eamon O'Brien loves the Crimson tech department!")

# 2. Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

def fizzbuzz():
    for x in range(1, 101):
        # checks if number if multiple of both 3 and 5
        if x % 3 == 0 and x % 5 == 0:
            print "FizzBuzz"
        # checks if number if multiple of 3
        elif x % 3 == 0:
            print "Fizz"
        # checks if number is multiple of 5
        elif x % 5 == 0:
            print "Buzz"
        else:
            print x

# test run
fizzbuzz()

# 3. Write a function that takes one string argument and returns that string with the most common letter swapped with the least common letter.

def swapchars(phrase):
    # define containers for most/least common chars
    most = ''
    mostcount = 0
    least = phrase[0]
    leastcount = phrase.count(phrase[0])
    
    # container for string with swapped chars
    newstring = ''
    
    for char in phrase:
        if char.isalpha():
            # checks to see if char is most common
            if phrase.count(char) > mostcount:
                most = char
                mostcount = phrase.count(char)
            #checks to see if char is least common
            if phrase.count(char) < leastcount:
                least = char
                leastcount = phrase.count(char)
    for char in phrase:
        # swaps most common char with least common char
        if char == most:
            newstring += least
        # swaps least common char with most common char
        elif char == least:
            newstring += most
        else:
            newstring += char
    print newstring

# test run
swapchars("There were a lot of escopeoples in the elevator on Tuesday.")


# 4. Write a function that will take a number n followed by an arbitrary number of string arguments and return the concatenation of the longest n arguments from longest to shortest. If n is -1, concatenate all of the arguments in this fashion. (Optional: Try passing a non-string argument after the first one. What happens? What are some ways to handle this gracefully?)

def sortcat(num, *args):
    longstring = ''
    # sort strings in descending order in terms of length
    args = sorted(args, key=len, reverse = True)
    for arg in args:
        if num == -1:
            longstring += arg
        elif num == 0:
            break
        else:
            longstring += arg
            num -= 1
    print longstring

# tests
sortcat(1, 'abc', 'bc')
sortcat(2, 'bc', 'c', 'abc')

# 5b. Write a Python function that simulates this approach to the Look Away minigame, assuming that Luigi always looks forward and that Mario, Wario, and Peach each randomly choose to look either forward, up, down, left, or right with uniform probability. Your function should take a number of trials to run as input and return the fraction of trials on which Luigi won. You will probably find the random module <http://docs.python.org/library/random.html> useful.
import random
import fractions

def minigame(num):
    # forward = 1, up = 2, down = 3, left = 4, right = 5
    wins = 0
    # set luigi by default to look forward
    luigi = 1
    for trial in range(0, num):
        # make characters randomly look a direction
        mario = random.randint(1, 5)
        wario = random.randint(1, 5)
        peach = random.randint(1, 5)
        # check if any characters looked forward like Luigi
        if luigi == mario or luigi == wario or luigi == peach:
            wins += 1
    print "Luigi won %i out of the %i games" % (wins, num)

    # alternate form of printing: 
    # print fractions.Fraction(numerator=wins, denominator=num)

# tests
minigame(5)
minigame(100)

# 8. a. Using the urllib and json modules, write a function that will get the data for the Quad -> Mass Ave/Garden trip and print out the times at which the next three shuttles will leave along with the number of minutes between each such time and the current time.

import urllib
import json
import datetime
import math

def shuttle():
    # get current date/time
    now = datetime.datetime.now()
    # get data from shuttle boy
    f = urllib.urlopen("http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass+Ave+Garden+St&output=json")
    data = json.loads (f.read())
    
    # store the first three trip datetimes
    a = data[0][u'departs']
    b = data[1][u'departs']
    c = data[2][u'departs']
    
    # store only the times; erase the dates
    a = a[11:]
    b = b[11:]
    c = c[11:]

    # store the current number of minutes and hours
    currentmins = now.minute
    currenthours = now.hour
    
    # store the number of hours for each trip
    ahours = a[0:2]
    bhours = b[0:2]
    chours = c[0:2]
    
    # store the number of mins for each trip
    amins = a[3:5]
    bmins = b[3:5]
    cmins = c[3:5]

    # print out info for three trips and current time
    print "1st Shuttle leaves at: %s, there are %i minutes left till it departs" % (a,math.fabs((int(currentmins)-int(amins)) + (int(currenthours) - int(ahours))* 60))
    print "2nd Shuttle leaves at: %s, there are %i minutes left till it departs" % (b,math.fabs((int(currentmins)-int(bmins)) + (int(currenthours) - int(bhours))* 60))
    print "3rd Shuttle leaves at: %s, there are %i minutes left till it departs" % (c,math.fabs((int(currentmins)-int(cmins)) + (int(currenthours) - int(chours))* 60))
    print now.strftime("Current time: %H:%M:%S")

# test
shuttle()



