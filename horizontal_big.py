from my_lib import pattern, alpha

word=input("Insert word: ")
word=list(word.lower())
word_array=[""]*5
print("\n")

for i,lt in enumerate(word):
    j=0
    if lt.isalpha():
        while j<5:
            word_array[j]+= pattern[alpha[lt][j]] + " "
            j+=1
    elif lt==" ":
        j=0
        while j<5:
            word_array[j]+="   "
            j+=1
j=0
while j<5:
    print(word_array[j])
    j+=1