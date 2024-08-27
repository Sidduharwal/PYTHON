# write a program to greet all the person names stored in a list 'l' and which starts with S 

# l = ["siddh", "shubham","isha","rahul"]



l = ["siddh", "shubham","isha","rahul"]

for name in l:

    if (name.startswith("s")):  
        print(f"Hello {name}")
