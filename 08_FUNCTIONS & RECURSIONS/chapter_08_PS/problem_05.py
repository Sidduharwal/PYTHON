# Write a python function to return print first n lines of the following pattern

# * * *
# * *
# *   for n=3


def pattern(n):
    if (n==0):

        return 
    
    
    print("*" * n)

    pattern(n-1)

pattern(5)