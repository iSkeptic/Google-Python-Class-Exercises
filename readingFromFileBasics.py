import sys


def main():

    fileName = sys.argv[1]
    myFile= open(fileName)

    # Looping through each line
    for line in myFile:
        print line,  # The comma prevents the \n that comes with each print command!

    myFile.close()

if __name__ == "__main__":
    main()
