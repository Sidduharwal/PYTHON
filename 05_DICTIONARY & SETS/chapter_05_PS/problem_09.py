#  can you change the values inside a list which is contained in set ?

# s = {8, 12, 65, "siddh" [1,45]}

# s =[4][0]=9

#  no you can't change the values inside a list

#  here is how can we do it :


s = {8, 12, 65, "siddh", (1,4)}
s.remove((1,4))
new_tuple =(9,2)
s.add(new_tuple)
print(s)

# output {65, 'siddh', 8, 12, (9, 2)}