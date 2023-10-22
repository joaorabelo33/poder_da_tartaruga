#Passo_2:Auto_repeticao
#Desafio: Variáveis e Loops
#exemplo com hexagono
lados = 6
angulo = 360 / lados

from turtle import*

speed (11)
shape('turtle') 

for count in range(lados):
    forward(100)
    right(60)

done()