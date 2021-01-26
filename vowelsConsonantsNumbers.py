str1 = "Hello World #@% 122345634"
vowels = {}
consonants = {}
numbers = {}
specialChar = {}
vowelsList = ["a", "e", "i", "o", "u"]
for s in str1:
    ch = str(s).lower()
    if((ch>='a' and ch<='z')):
        if(ch in vowelsList):
            if(ch in vowels):
                vowels[ch] +=1
            else:
                vowels[ch] = 1
        else:
            if(ch in consonants):
                consonants[ch] +=1
            else:
                consonants[ch] = 1
    elif((ch >= "0" and ch <= "9")):
        if ch in numbers:
            numbers[ch] += 1
        else:
            numbers[ch] = 1
    else:
        if ch in specialChar:
            specialChar[ch] += 1
        else:
            specialChar[ch] = 1
print("Vowels", vowels)
print("consonants", consonants)
print("Numbers", numbers)
print("special Char", specialChar)
