#Check whether the given input is anagram or not
def checkAnagram(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    if len(word1)>=len(word2):
        for i in range (0,len(word2)):
            if word2[i] in word1:
                continue
            else:
                return False
        return True


str1=input("Enter word1:")
str2=input("Enter word2:")
print(checkAnagram(str1,str2))
