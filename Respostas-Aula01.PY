                                                #DESAFIO 01#
#O Paulo fez uma análise rápida e disse que tem 18 filmes sem avaliações, será que ele acertou?
#Determine quantos filmes não tem avaliações e quais são esses filmes.

import pandas as pd
filmes = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"] # Setando as Colunas para os filmes

avaliacoes = pd.read_csv("https://github.com/alura-cursos/introducao-a-data-science/blob/master/aula0/ml-latest-small/ratings.csv?raw=true")
avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"] # Setando as Colunas para as Avaliacoes

notas_medias_por_filme = avaliacoes.groupby("filmeId")["nota"].mean() # Vai pegar todas as notas tirar a media e colocar de volta na coluna nota de acordo com o filmeId

filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId") # Criando a Coluna Media no DataFrame de acordo com os IDs dos Filmes



tabela_true_false = filmes_com_media["nota"].isnull() # Vai resultar em uma Serie com os valores das notas
                                                      # não preenchidas como true e as linha preenchidas como false

filmes_sem_nota = filmes_com_media[tabela_true_false] # Vai passar uma serie de trues e falses de forma que só retorne
                                                      # as linhas onde o valor for true(null) no index correspondente e aparentemente na mesma coluna
print(filmes_sem_nota) # Vai demorar um pouco

