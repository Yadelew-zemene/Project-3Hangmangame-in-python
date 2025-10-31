import random
list_numbers=['0','1','2','3','4','5','6','7','8','8']
list_letters=['a', 'A', 'b', 'B', 'C', 'c', 'd', 'D', 'e', 'E', 'F', 'G', 'f', 'g', 'h', 'i', 'H', 'I', 'j', 'J', 'k', 'K', 'l', 'm', 'L', 'N', 'M', 'n', 'o', 'p', 'O', 'P', 'Q', 'R', 'q', 'r', 's', 'S', 'T', 't', 'u', 'U', 'V', 'v', 'w', 'W', 'x', 'X', 'y', 'z', 'Y', 'z']
list_symbols=['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '[', ']', '}', '?', '/', '|']
print("Well  Come To  My PassWord Genarator!!")
passletter=[]

numberOfLetter=int(input("How many  letters do you want in your password?"))

passletter=random.choices(list_letters,k=numberOfLetter)
print()#printing empty line

numberofinteger=int(input("How many numbers do you want in your passswod?"))
passnumber=[]
for i in range(numberofinteger):
    passnumber.append(str(random.randint(0,9)))#generating one random number each iteration
print()

numberOfSymbols=int(input("How many symbols do you want  in your password?"))
passsymbols=random.choices(list_symbols,k=numberOfSymbols)

totalcode=passletter+passsymbols+passnumber
#shufeled password generator
random.shuffle(totalcode)#shuffling the total code

Password=''.join(totalcode)#joining the list(totalcode
print(f"The password generated: {Password}")




