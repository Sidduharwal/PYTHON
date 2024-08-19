# =============> Write a program to fill in a letter template given below with name and date <==========

letter= ''' Dear <|Name|>
    your selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Siddh").replace("<|Date|>", "19 AUG 2024"))