import re
import os
from unittest import skip
from art import *

outputLim = 100

def main():
    fileloc = fileLoc = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    fivedir = open(r"C:\Users\emurphy24\Documents\GitHub\WoordleCalculator\fiveletterdir.txt", "r", encoding="utf-8")
    dirlist = []

    knownloc = input("Please input the known letter positions in this format:(-x-y-):")
    if len(knownloc) == 5:
        loclist = list(knownloc)
    else:
        print("Please input something, or if there isnt any known letters, input (-----)")
        main()
    knownlet = input("Please input the unknown position letters in this format or leave blank:(xyz):")

    letlist = list(knownlet)
    skipLetCheck = False
    if len(letlist) == 0:
        skipLetCheck = True

    nolist = input("What letters are not in the word? (leave blank if unknown): ")
    nolist = list(nolist)
    skipNolist = False

    if len(nolist) == 0:
        skipNolist = True

    for line in fivedir:
        line = line.strip()
        line = line.lower()
        dirlist.append(line)
        linll = len(letlist)

    locoutput = locfind(dirlist, loclist)
    if not skipLetCheck:
        letoutput = letfind(dirlist, letlist)
        

        l1 = []
        l2 = []
        output = []
        if len(letoutput) > len(locoutput): 
            l1 = letoutput
            l2 = locoutput
        else:
            l1 = locoutput
            l2 = letoutput

        for i in range(len(l1)):
            l1item = l1[i]
            for k in range(len(l2)):
                l2item = l2[k]
                if l1item == l2item:
                    output.append(l1item)
    if skipNolist and skipLetCheck:
        output = locfind(dirlist, loclist)
    else:
        locoutput = output
    if not skipNolist:
        output = nolap(output, nolist)

    if len(output) > outputLim:
        print("Sorry, there were over", str(outputLim), "possible words! Try narrowing it down.")
        main()

    print("\n\nPOSSIBLE OUTCOMES: ", output)



def locfind(dirlist, loclist):
    hold = []
    for i in dirlist:
        wordlist = list(i)
        matchcount = 0
        for j in range(len(wordlist)):
            if wordlist[j] == loclist[j] or loclist[j] == "-":
                matchcount += 1
                if matchcount == 5:
                    hold.append(i)
    return hold

def letfind(dirlist, letlist):
    hold = []
        
    if len(letlist) == 1:
        regexcode = (r"^(?=.*" + str(letlist[0]) + ").*$")
    elif len(letlist) == 2:
        regexcode = (r"^(?=.*" + str(letlist[0]) + ")(?=.*" + str(letlist[1]) + ").*$")
    elif len(letlist) == 3:
        regexcode = (r"^(?=.*" + str(letlist[0]) + ")(?=.*" + str(letlist[1]) + ")(?=.*" + str(letlist[2]) + ").*$")
    elif len(letlist) == 4:
        regexcode = (r"^(?=.*" + str(letlist[0]) + ")(?=.*" + str(letlist[1]) + ")(?=.*" + str(letlist[2]) + ")(?=.*" + str(letlist[3]) + ").*$")
    elif len(letlist) == 5:
        regexcode = (r"^(?=.*" + str(letlist[0]) + ")(?=.*" + str(letlist[1]) + ")(?=.*" + str(letlist[2]) + ")(?=.*" + str(letlist[3]) + ")(?=.*" + str(letlist[3]) + ").*$")
    
    
    for i in dirlist:
        if re.findall(regexcode, i):
            hold.append(i)
    return hold

<<<<<<< HEAD
def nolap(output, nolist):
    for i in range(len(output)):
        outputword = list(output[i])
        for j in range(len(nolist)):
            nolistletter = nolist[j]
            for k in range(len(outputword)):
                outputletter = outputword[k]
                if nolistletter == outputletter:
=======
def nolap(wordlists, nolist):
    i = 0
    output = wordlists
    for w in range(len(wordlists)):
        wordRemoved = False
        for l in nolist:
            if not wordRemoved:
                if l in output[i]:
>>>>>>> 52950b549eb60e6a428164253d34f3915efa7551
                    output.remove(output[i])
                    wordRemoved = True
        if not wordRemoved:
            i += 1
                    
    return output

if __name__ == '__main__':
    tprint("     WORDLE    ENGINE\n\n")
    print("This code is part of the Battleship project (https://github.com/Eli-Murphy/WordleCalculator)\n\n")
    main()


# Copyright (c) 2022 Elijah A. Murphy
# Distributed under the terms of the MIT License. 
# SPDX-License-Identifier: MIT
# This code is part of the Battleship project (https://github.com/Eli-Murphy/WordleCalculator)