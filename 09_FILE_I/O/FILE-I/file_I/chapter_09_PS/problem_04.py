# a file contains a word "donkey" multiple times,
#  you need to write a program which replace this word with ##### by updating the same file

word = "donkey"

with open ("file.txt", "r")as f:
    content =f.read()
contentNew = content.replace(word,"#####")
with open("file.txt","w") as f:
    f.write(contentNew)
