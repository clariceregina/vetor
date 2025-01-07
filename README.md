# Determinação da Filial Mais Próxima

Este script em Python calcula a filial mais próxima de uma matriz central com base nas coordenadas fornecidas. Ele utiliza a fórmula da distância Euclidiana para determinar a menor distância entre a matriz e três filiais. O realizei com a intenção de colocar em prática meu conhecimento de geometria analítica, em especial, vetores, associado à análise de dados.

## Funcionalidades

- Calcula a distância Euclidiana entre a matriz central e cada filial.
- Identifica a filial mais próxima com base na menor distância calculada.
- Exibe o resultado formatado com o nome da filial e a distância correspondente.

## Pré-requisitos

- Python 3.x instalado.
- Módulo `math` (nativo no Python).

## Estrutura do Código

1. **Importação de Funções:**
   O módulo `math` é importado para realizar cálculos matemáticos, como a raiz quadrada.

2. **Definição das Coordenadas:**
   As coordenadas da matriz central e das filiais são definidas diretamente no código.

3. **Cálculo da Distância Euclidiana:**
   A fórmula da distância Euclidiana é usada para determinar a distância entre a matriz e cada filial:
   \[
   d = \sqrt{(x_f - x_m)^2 + (y_f - y_m)^2}
   \]

4. **Identificação da Menor Distância:**
   Uma lista é criada para armazenar as distâncias, e a função `min` identifica a menor distância.

5. **Exibição dos Resultados:**
   O nome da filial mais próxima e sua respectiva distância são exibidos no formato:
