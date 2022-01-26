
def main():
    fivedir = open(r"C:\Users\emurphy24\Documents\GitHub\WoordleCalculator\fiveletterdir.txt", "r", encoding="utf-8")
    dirlist = []

    knownloc = input("Known letter position (X-YZ-):")
    loclist = list(knownloc)

    knownlet = input("Known letters (ABC): ")
    letlist = list(knownlet)

    for line in fivedir:
        line = line.strip()
        line = line.lower()
        dirlist.append(line)
        linll = len(letlist)

    locoutput = locfind(dirlist, loclist)
    letoutput = letfind(dirlist, letlist, linll)
        
    print(locoutput)
    print(letoutput)

    if len(letoutput) > len(locoutput):
        for i in range(len(letoutput) - len(locoutput)):
            locoutput.append("")
    if len(locoutput) > len(letoutput):
        for i in range(len(locoutput) - len(letoutput)):
            letoutput.append("")
    output = [i for i, j in zip(locoutput, letoutput) if i == j]

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



def letfind(dirlist, letlist, linll):
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

if __name__ == '__main__':
    main()