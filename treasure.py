
# Read filename as input
print("Enter filename followed by numbers of lines to print ... ")
print("or just the number of lines.")
str_inp = input("... : ")

# Remove accidental commas and split string
list_inp = str_inp.replace(',', ' ').split()
# print("original: ", list_inp)

numargs = len(list_inp)
if numargs == 1:
    try:
        numlines = int(list_inp[0])
    except Exception:
        print("Error: Single argument must be integer!")
        quit()
    filename = "treasure.txt"

elif numargs != 2:
    # Checking more input format
    print('Input format: You must enter "filename" followed by "number"')
    quit()

else:
    # numargs must be 2 here: filename is first argument
    filename = list_inp[0]
    # Checking for integer number
    try:
        numlines = int(list_inp[1])
    except Exception:
        print('Second argument must be an iteger number.')
        quit()

# Checking file name
try:
    han = open(filename, 'r')
except FileNotFoundError:
    print("File doesn't exist!!!")
    quit()
except Exception:
    print("Something went wrong!")
    quit()

# Write out a number of lines
lnum = 0
for line in han:
    lnum = lnum + 1
    if lnum > numlines:
        break

    listln = list()

    for c in line:
        if ord(c) > ord('z'):
            print(c, '<', ord(c), '>')

        listln.append(c)
    print(line.split())
    # cleanline = ' '.join(line.split())

    # for c in cleanline:
    #     if ord(c) > ord('z'):
    #         print(c, '<', ord(c), '>')
    # print(cleanline)
