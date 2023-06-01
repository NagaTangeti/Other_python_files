def count_words(filename):
    """Count the approx. number of words in a file."""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
       pass#print(f"Sorry, the file {filename} doesn't exist.") 
    else:
    #Count the appropriate number of words in a file (Analysing text).
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'moby_dick.txt'] #taken from 'gutenberg.org'.
for filename in filenames:
    count_words(filename)