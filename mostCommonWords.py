
# State desired text file and call findWords function.
# For example:
# findWords('myfile.txt').
 
from collections import Counter

def findWords(textFile):
    # Array to store words.
    words = []

    # Extract content from .txt file and separate content into words using .split().
    # And store words into words array as lower case.
    with open(textFile, 'r') as text:
        fileContent = text.read()
        words.extend(fileContent.lower().split())

    # Use the Counter class to find the top 10 most common words.
    wordCount = Counter(words)

    # Print 10 most common words.
    print(wordCount.most_common(10))

findWords('')