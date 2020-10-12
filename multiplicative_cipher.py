# get word and the key from the user
word = input("\nEnter Your Password : ")
key = int(input("Enter The Key Value : "))
crypted = ""

# creating dict with alphabets
alpha = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
         13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
       'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

for i in word:

    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':

        if 'a' <= i <= 'z':
            temp = (num[i] * key) % 26
            crypted += alpha[temp]

        else:
            j = i.lower()
            temp_1 = (num[j] * key) % 26
            temp_2 = alpha[temp_1]
            crypted += temp_2.upper()

    else:
        crypted += i

print('\nEncrypted text is : ', crypted, "\n")
