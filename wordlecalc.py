import re
import os

def main():
    fileloc = fileLoc = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    fivedir = open(r"C:\Users\emurphy24\Documents\GitHub\WoordleCalculator\fiveletterdir.txt", "r", encoding="utf-8")
    dirlist = []

    knownloc = input("Known letter position (X-YZ-):")
    loclist = list(knownloc)

    knownlet = input("Known letters (ABC): ")
    letlist = list(knownlet)

    nolist = input("What letters are not in the word?: ")
    nolist = list(nolist)

    for line in fivedir:
        line = line.strip()
        line = line.lower()
        dirlist.append(line)
        linll = len(letlist)

    locoutput = locfind(dirlist, loclist)
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

    output = nolap(output, nolist)

    print("\n\nPOSSIBLE OUTCOMES: ", output)



def locfind(dirlist, loclist):
    hold = []
    for i in dirlist:
        wordlist = list(i)
        matchcount = 0
        for j in range(len(wordlist)):
            #print(i)
            if wordlist[j] == loclist[j] or loclist[j] == "-":
                matchcount += 1
                if matchcount == 5:
                    hold.append(i)
    return hold



def letfind2(dirlist, letlist, linll):
    hold = []
    for i in dirlist:
        wordlist = list(i)
        matchcount = 0
        for j in range(len(wordlist)):
            if wordlist[j] in letlist: 

                #BUG: If given data like "[i,c,a]", words such as "ababa" 
                # will pass due to the "a" being counted three times. Ideally,
                # all the letters would need to be in the string to pass, however
                # I am unaware of how to code a feature that would know which letter
                # was used, and remove it from [letlist]. However due to it not being
                # iterated, I cannot remove that specific letter using variable j.

                matchcount += 1
                if matchcount == linll:
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
        #wordlist = list(i)

        if re.findall(regexcode, i):
            hold.append(i)
    return hold

def nolap(output, nolist):
    print("output: ", type(output))
    print("nolist: ", type(nolist))
    if len(output) > len(nolist):
        for i in range(len(output)-len(nolist)):
            nolist.append(" ")
    if len(output) < len(nolist):
        for i in range(len(nolist)-len(output)):
            output.append(" ")
        
    for i in range(len(nolist)):
        outputword = list(output[i])
        for j in range(len(nolist)):
            nolistletter = nolist[j]
            for k in range(len(outputword)):
                outputletter = outputword[k]
                if nolistletter == outputletter:
                    try:
                        output.remove(output[i])
                    except:
                        pass
    return output



if __name__ == '__main__':
    main()