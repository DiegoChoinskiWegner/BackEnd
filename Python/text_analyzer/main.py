import re

def text_analyzer(input):
    total_words = 0
    total_sentences = 0
    top_5_dict = {}
    top_5 = []
    unique_words = []

    input = input.lower()
    splited_input = re.split(r"\s,.?!\n", input)
    
    for word in splited_input.split():
        total_words += 1
        if word not in unique_words:
            unique_words.append(word)
        if word not in top_5_dict:
            top_5_dict[word] = 1
        else:
            top_5_dict[word] += 1
        
        if top_5_dict:
            if len(top_5) < 5:
                top_5.append(word)

        
    new_split = re.split(r"\s,.?!\n", input)
    for sentence in new_split:
        total_sentences += 1




    result = f"Total de palavras: {total_words}, Total de frases: {total_sentences}, Top 5: {top_5}, Palavras únicas: {unique_words}" 
    print (result)

    return result