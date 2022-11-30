import my_lib
word= input("Insert word: ")
word=list(word)

print("\n")

for n in word:
    my_lib.print_big(n)
    print("\n")