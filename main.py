# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, 'r') as f:
        file = f.read()

    return file

output = read_file_content('./story.txt')
print(output)
        
    
def count_words(str):
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    counts = dict()
    text = str.split()

    for e in text:
        if e in counts:
            counts[e] += 1
        else:
            counts[e] = 1

    return counts

print(count_words(output))
