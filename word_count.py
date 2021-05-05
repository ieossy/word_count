def word_count(text):
    # initialize a dictionary to hold the word count
    words_count = {}
    # interate through and remove whitespaces, dot, punctuations marks, newline and question marks
    for punctuations in '.,"\n?!': 
        text = text.replace(punctuations, '') # so as not to count words with any of the above characters as different words
        
    # split words into list of words separated by whitespace by making each word a dictionary key
    text = text.split()
    
    for words in text:
        words_count[words] = words_count.get(words,0) + 1
        
    print(words_count)
    
text = "i'd rather not go to school today,\n because i'm yet to complete my assignment and my school teacher \nwill punish me for not doing my assignment, but i love to go to school. What then should i do today?"
word_count(text)
