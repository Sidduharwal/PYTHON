# write a program to find out the line number where python is present from question 06
 

with open("log.txt", 'r') as f:
    lines = f.readlines()

    lineno = 1
    for line in lines:
        if("Python" in line):
            print(f"yes python is present, Line no: {lineno}")
            break
        line =+ 1

    else:
        print("no python is not present")