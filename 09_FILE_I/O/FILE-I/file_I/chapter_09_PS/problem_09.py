# write a program whether a file is identical and matches the content of another file


with open("this.txt") as f:
    content1 = f.read()

with open("this_copy_text") as f:
    content2 = f.read()

    if (content1 == content2):
        print("Yes, these files are identical.")

    else:
        print("No, these files are not identical.")