# importar funções
import math

# inserir coordenadas matriz
x_m = 2
y_m = 3

# inserir coordenadas filial 1

x_f1 = 5
y_f1 = 7

# inserir coordenadas filial 2

x_f2 = -1
y_f2 = 4

# inserir coordenadas filial 3

x_f3 = 4
y_f3 = -2

# determinar o módulo (distância em relação à matriz) de cada vetor através da distância Euclidiana

mod_m_f1 = math.sqrt((x_f1 - x_m)**2 + (y_f1 - y_m)**2)

mod_m_f2 = math.sqrt((x_f2 - x_m)**2 + (y_f2 - y_m)**2)

mod_m_f3 = math.sqrt((x_f3 - x_m)**2 + (y_f3 - y_m)**2)

# lista de distâncias e nomes das filiais

distancias = [mod_m_f1, mod_m_f2, mod_m_f3]
nomes_filiais = ['Filial 1', 'Filial 2', 'Filial 3']

# determinar a menor distância

menor_distancia = distancias.index(min(distancias))

# exibir
print(f'A menor distância é da {nomes_filiais[menor_distancia]}, com distância de {
      distancias[menor_distancia]:.2f} Km')
