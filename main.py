def main():
    path = "/home/samwise/workspace/github.com/thenakedgypsy/bookbot/books/frankenstein.txt"
    text = getBookText(path)
    print(text)
    print(f"Word Count: {getWordCount(text)}")
    print("Character Counts:")
    getCharacterCounts(text)

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
    print(alphabet)

        

    



main()