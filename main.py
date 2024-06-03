def main():
    path = "/home/samwise/workspace/github.com/thenakedgypsy/bookbot/books/frankenstein.txt"
    text = getBookText(path)
    print("--- Begin report of " + path + " ---")
    count = getWordCount(text)
    print(f"{count} words found in the document")
    print(" ")
    printCharacterCounts(getCharacterCounts(text))
    print("--- End report ---")




def getBookText(path):
    with open(path) as f:
        return f.read()
    
def getWordCount(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def getCharacterCounts(text):
    alphabet = dict()
    lowered = text.lower()
    characters = list(lowered)
    for letter in characters:
        if letter in alphabet:
            alphabet[letter] += 1
        else:
            alphabet[letter] = 1
    return(alphabet)

def printCharacterCounts(alphabet):
    for letter in alphabet:
        print(f"The '{letter}' character was found {alphabet[letter]} times")



    
main()