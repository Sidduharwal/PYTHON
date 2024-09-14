# write a program to mine a log file and find out whether it contains 'python'property


with open("log.txt", 'r') as f:
    content =f.read()

    if("Python" in content):
        print("yes python is present")
        
    else:
        print("no python is not present")