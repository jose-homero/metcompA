# -*- coding: utf-8 -*-
"""tabalho erro integral

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gZoe-fcMkvNF9EK59ijOQ8VZLphxu21X

Nesta atividade vamos estimar o erro da seguinte forma:

ε = |Iexata-I(N)|

onde I(N) é o valor da integral obtido dividindo o intervalo de integração em N partes e Iexata é a solução analítica para a integral.

Um teste simples para verificar quando a resposta está convergindo é aumentar N e calcular o erro a cada incremento no seu valor.  Se Δx é a fatia sobre o eixo x após dividi-lo em N partes. Espera-se que o erro seja proporcional a Δxα.

1 - Escreva um programa que calcule o erro do método do trapézio em função de N. Este programa deve usar 10 valores diferentes de N: 2²,...,2²⁰. Para cada valor de N corresponde um Δx, calcule quanto vale a integral para este Δx e guarde o erro em relação à solução exata em uma lista. Assim, você poderá calcular o erro com relação à solução exata para as diferentes partições do intervalo, portanto, para cada Δx.
"""

import math   #importaçao
import numpy as np

# funcao da integral pelo metodo do trapezio 

def int_tpz(N, a, b):
  
  dx = (b - a) / N   #fatias em função de N
  
  soma = 0 #inicializa variavel soma
  
  for n in range(1, N): #laço que percorre N

    soma += f( a  + (dx * n) )

  return dx * (0.5 * f(a) + 0.5 * f(b) + soma )

# função  da equacao que vai integrada

def f (x):

  return 1 / ((x ** 2) + 1)

import matplotlib.pyplot as plt

def graf(tpz, simp, x):     #funcao grafico

  figura = plt.figure(figsize=(10, 5))
  plt.plot(x, tpz, color='darkorange', label = 'Trapézio')
  plt.plot(x, simp, color='steelblue', label = 'Simpson')
  plt.legend(fontsize = 15)
  plt.xlabel('log(Δx)', fontsize = 20)
  plt.ylabel('log(ε)', fontsize = 20)
  plt.title('Erro dos Métodos de Integração', fontsize = 25)
  print("\n")
  plt.show()

#funcao p/ calculo do erro do trapezio 

def erro_tpz(N, i_tab, a, b):
  
  return abs(i_tab - int_tpz(N, a, b))

#valor tabelado da integral pelo wolfram

i_tab = 2.4980915447965089

dx_tpz = []     #criação de lista p/ armazenar
e_tpz =[]

b = 3         #limites da integral
a =-3

# N = 2^k, k varia de  de 2  a 20

for k in range(2, 22, 2):# laço percorre k e calcula o erro p/ cada valor de N

  N=int(2**k)  #valor de N
  while N % 2!= 0:
    N= int(input("Digite N par"))

  #resolvi aplicar ln para ficar mais ludico no grafico
  dx_tpz.append( np.log ((b - a) / N) ) #lista armazena dx em func de N

  e_tpz.append ( np.log (erro_tpz( N, i_tab, a, b )) ) # armazena erros

# funcao p/ calcular simpson

def i_simpson(N, a, b): 

  par = 0     #inicializando variaveis p/ calcular o par e o impar 
  impar = 0

  h = (b - a) / N  #h do metodo de simpson

  for i in range(1, N, 2):    #laco percorre N 

    impar += f(a +  i * h)    # somatorio da da funcao  a + n * pedaço

  for p in range(2, N, 2):    

    par += f(a + p * h)

  return (h /3) * (f(a) + f(b) + 4 * impar + 2 * par)    #retorna integral de simpson de N

"""3-Escreva um programa que calcule o erro do método de Simpson em função de N de maneira similar ao do exercício anterior. Lembre que o método de Simpson requer que N seja par. """

#funcao que calcula do erro simpson

def e_simpson(N, i_tab, a, b):
  
  return abs(i_tab - i_simpson(N, a, b))  #modulo da diferença

"""Os gráficos gerados """

h_simp = []    #inicializa lista
e_simp = []

for k in range(2, 22, 2):# laço percorre k e calcula o erro p/ cada valor de N

  N=2**k

  h_simp.append( np.log ((b - a) / N) ) #lista armazena h em func de N
  
  e_simp.append( np.log (e_simpson ( N, i_tab, a, b ))) # armazena erros
  
# como dx = h nos dois vou passar só 1
graf(e_tpz, e_simp, dx_tpz)

"""Determine a inclinação do gráfico log(ε) x log(Δx)"""

tx_tpz = (e_tpz[6] - e_tpz[5])/(dx_tpz[6]- dx_tpz[5])
print('Inclinação do Método de Simpson','{0:.2f}'.format(tx_tpz))

tx_simp = (e_simp[3] - e_simp[2])/(h_simp[3]- h_simp[2])
print('Inclinação do Método de Simpson','{0:.2f}'.format(tx_simp))