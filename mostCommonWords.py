
# State desired text file and call findWords function.
# For example:
# findWords('myfile.txt').
 
def findWords(textFile):
    # Import Counter class to count word occurences.
    from collections import Counter
    # Array to store words.
    words = []
    # Extract content from .txt file and separate content into words using .split().
    # And store words into words array.
    with open (textFile, 'r') as text:
        fileContent = text.read()
        words.append(fileContent.split())
    # Use the counter class to find the top 5 most common words.
    wordCount = Counter(words)
    mostCommonWords = wordCount.most_common(5)

    return mostCommonWords
