from unittest import case
import requests
from bs4 import BeautifulSoup



def pesquisarAtleta():
    atleta =str(input("qual atleta deseja buscar"))
    response = requests.get("https://www.worldsurfleague.com/athletes?tourIds%5B%5D=1")
    soup = BeautifulSoup(response.content, 'html.parser')
    
    ## varaivel filtrando o conteudo desejado do html, onde o primeiro parametro é a tag html, e o segundo a chave valor que deseja procurar
    listaAtletas = soup.find("div", {"class":"athletes-directory-module__body new-content-module-body"})
    listaCompleta = listaAtletas.find_all("div", {"class":"avatar-text-primary"})
    
    for listaCompleta.index in listaCompleta:
        if(atleta == listaCompleta.index.get_text()):
            href = listaCompleta.index.find('a').get('href')
            print(listaCompleta.index.get_text() +"\n")
            print(href)
        

    #print(atletaBuscado)
  #  try:   
        

   # finally:
    #    response = requests.get("https://www.worldsurfleague.com/athletes" + atleta)
     #   response = requests.get("https://www.worldsurfleague.com/athletes" + atleta)
      #  file = open("arquivo.txt","w")
      #  file.write(response.text)
        ## aqui sera feita a avaliação no arquivo para ver quais eventId possuem no texto.
        ## concatenação dos dados dos eventos  "?yearResultsRank=" + anoEvento + "&yearResultsTourCode=" + codigoCategoria + 
        ##variavel anoEvento 2013><2024 , 
        ##variavel codigoEvento mct = Mens Championship Tour; mcs = Mens Challenger Series ; mqs = Mens Qualifying Series ; mjun = Mens Junior Tour;
        ##variavel codigoEvento wct = Womens Championship Tour; wcs = Womens Challenger Series ; wqs = Womens Qualifying Series ; wjun = Womens Junior Tour;
       # file.close()


    ## For(comparar o i com o tanto de eventos que atleta participou no ano, e para cada iteração gerar um arquivo com dados da performance dele no evento.)
    
    #for(i=0)
     #   try:
      #      response = requests.get("https://www.worldsurfleague.com/athletes" + atleta + evento)
       #     fileEvent = open("arquivoEvento.txt","w")
        #    fileEvent.write(response.text)
         #   fileEvent.close()



pesquisarAtleta()    
#def gerarEstatistica():








##def eventosPorAtleta():
#    try:
 #       
  #      if 
   #    
    #finally: 
        