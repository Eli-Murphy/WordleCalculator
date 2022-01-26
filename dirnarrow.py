dirfrom = open(r"C:\Users\emurphy24\Documents\GitHub\WoordleCalculator\dictfrom.txt", "r", encoding="utf-8")
dirlist = []
for line in dirfrom:
    line = line.strip()
    dirlist.append(line)
print(len(dirlist))

    



dirfrom.close()
dirto = open(r"C:\Users\emurphy24\Documents\GitHub\WoordleCalculator\fiveletterdir", "a", encoding="utf-8")

for i in dirlist:
    if len(i) == 5 and i.isalpha():
        dirto.write(i + "\n")