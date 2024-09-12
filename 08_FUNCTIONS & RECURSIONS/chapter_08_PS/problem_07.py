# write a python function to remove  a given word from a list ad strip it at the same time


def rem (l, word):
    n=[]
    for item in l :
        if not (item==word):
            n.append(item.strip(word))
    return n
l=["siddh", "ishan", "ishu", "rohan", "an"]
print(rem(l,"an"))


# def rem(l, word):
#     n = []
#     for item in l:
#         if not (item == word):
#             n.append(item.strip(word))  # Strip occurrences of the word
#     return n  # Return outside the for loop

# l = ["siddh", "ishan", "ishu", "rohan", "an"]
# print(rem(l, "an"))
