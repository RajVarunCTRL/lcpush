
def reverseWords(s):
    def countVowels(word):
        vowels = set('aeiou')
        return sum(1 for char in word if char in vowels)


    words = s.split()
    tarCnt = countVowels(words[0])
    
    for i in range(1, len(words)):
        if countVowels(words[i]) == tarCnt:
            words[i] = words[i][::-1]
    return " ".join(words)

s = "cat and mice"
print(reverseWords(s))