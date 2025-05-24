

def text_analyzer(input):
    total_words = 0
    total_sentences = 0
    top_5_dict = {"word": "count"}
    top_5 = []
    unique_words = []

    input.split()
    for word in input.split():
        total_words += 1
        if word not in unique_words:
            unique_words.append(word)
        if word not in top_5_dict:
            top_5_dict[word] = 1
        else:
            top_5_dict[word] += 1
        
        

    new_split = input.split('.' | ',' | '!' | '?' | '...' | ';' | ':')
    for sentence in new_split:
        total_sentences += 1

    





    result = f"Total de palavras: {total_words}, Total de frases: {total_sentences}, Top 5: {top_5}, Palavras únicas: {unique_words}" 

    return result