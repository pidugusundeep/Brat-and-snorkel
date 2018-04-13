import re
allLines = []

def getInputFile():
    filename = raw_input("Enter the file location: ")
    if(filename[len(filename)-4:len(filename)] != ".ann"):
        print("Invalid File")
        getInputFile()
    else:
        file = open(filename, "r")  
def formatText(str):
    print(str)
    for strings in str[2].split():
        if(str[2].split().index(strings) == 0):
            if(len((str[2].split())) == 1):
                f.write(strings+"\t"+"O-"+str[1].split()[0])
                f.write("\n")
            else:
                f.write(strings+"\t"+"B-"+str[1].split()[0])
                f.write("\n")
        else:
            f.write(strings+"\t"+"I-"+str[1].split()[0])
            f.write("\n")
    return

getInputFile()
for line in file:
    allLines.append(re.split(r'\t+', line.rstrip('\t')))
sortedLines = sorted(allLines,key=lambda x: x[1].split()[1])
sortedLinesFinal = sorted(allLines,key=lambda x: x[1].split()[2])
outputFilename = raw_input("Enter the output File name : ")
f = open(outputFilename+".txt","a+")
f.write('\n')
for eachEntity in sortedLinesFinal:
    formatText(eachEntity)
f.close()