import sys
import cmd

path = './csvfiles/'
outputPath = './output/data.csv'



def data_set_creator():
    firstFile = input('First file name (file1): ') or "file1"
    secondFile = input('Second file name (file2): ') or "file2"

    fileone = ''
    filetwo = ''
    with open(path + firstFile +'.csv', 'r') as t1, open(path + secondFile + '.csv', 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()
    with open(outputPath, 'w') as outFile:
        for line in filetwo:
            if line in fileone:
                outFile.write(line)

#main function
if __name__ == "__main__":
    data_set_creator()
