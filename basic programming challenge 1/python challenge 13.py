txt=input("input a sentence")
replace=input("what word do you want to replace")
while replace not in txt:
    print ("please use a word from within the txt")
new_word= input ("what word do you want to replace the word with?")
print(txt.replace(replace,str(new_word)))
