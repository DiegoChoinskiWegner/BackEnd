from main import text_analyzer 

input = "Olá! Tudo bem? Eu estou aprendendo Python. Python é muito legal. Python é poderoso."


waited_output = "Total de palavras: 11, Total de frases: 4, Top 5: ['python', 'é', 'olá', 'tudo', 'bem'], Palavras únicas: ['olá', 'tudo', 'bem', 'eu', 'estou', 'aprendendo', 'legal', 'poderoso']" 

def test1(input, waited_output): 
    output= text_analyzer(input)

    if output == waited_output:
        return "test 1 = PASSED"
    else:
        return "test 1 = FAILED"



print(test1(input, waited_output))

#test1(input2)

#test1(input3)