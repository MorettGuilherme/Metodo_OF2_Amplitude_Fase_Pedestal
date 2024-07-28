# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado).
# Autor: Guilherme Barroso Morett.
# Data: 26 de junho de 2024.

# Objetivo do código: gráfico dos dados estatíticos ao longo das ocupações de acordo com o janelamento para o método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado).

""" 
Organização do Código:

Leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.

Funções presentes:

1) Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento pelo método OF2 Otimizado.
Entrada: número do janelamento.
Saída: Matriz com os dados de entrada organizados de acordo com a coluna (número da ocupação, média, variância e desvio padrão do erro de estimação do parâmetro de interesse).

2) Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento pelo método OF2 Otimizado.
Entrada: dado estatístico desejado (média, variância ou desvio padrão) e a matriz dos dados.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import os
from termcolor import colored

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Plote do gráfico do dado estatístico do erro de estimação da amplitude, fase ou pedestal ao longo das ocupações para um determinado janelamento pelo método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------- 1) FUNÇÃO PARA A LEITURA DOS DADOS ESTATÍSTICOS DE TODAS AS OCUPAÇÕES PARA UM DETERMINADO JANELAMENTO PELO MÉTODO OF2 OTIMIZADO ---------- ###

# Definição da função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento pelo método OF2 Otimizado.
def leitura_dados_estatisticos_janelamento_OF2_otimizado(parametro, n_janelamento):

    # Nome da pasta em que se encontra o arquivo de entrada dos dados estatísticos de acordo com o janelamento.
    pasta_dados_estatisticos_janelamento = f"Dados_Estatisticos_OF2_Otimizado_{parametro}_OC"

    # Nome do arquivo de entrada dos dados estatísticos de acordo com o janelamento.
    arquivo_dados_estatisticos_janelamento = f"dados_estatisticos_OF2_Otimizado_janelamento_{n_janelamento}.txt"

    # O caminho para esse arquivo de entrada das ocupações.
    caminho_arquivo_dados_estatisticos_janelamento = os.path.join(pasta_dados_estatisticos_janelamento, arquivo_dados_estatisticos_janelamento)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_estatisticos_janelamento):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_estatisticos_janelamento,"r") as arquivo_entrada_dados_estatisticos_janelamento:
        
            # Armazena os dados na variável Matriz_Dados_Estatisticos_Janelamento.
            Matriz_Dados_Estatisticos_Janelamento = np.array(np.loadtxt(arquivo_entrada_dados_estatisticos_janelamento, skiprows = 1, dtype = 'double', delimiter = ','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_estatisticos_janelamento} não existe na pasta {pasta_dados_estatisticos_janelamento}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar em uma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_Dados_Estatisticos_Janelamento.
    return Matriz_Dados_Estatisticos_Janelamento

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------ 2) FUNÇÃO PARA O PLOTE DOS GRÁFICO DO DADO ESTATÍSTICO AO LONGO DAS OCUPAÇÕES PARA UM DETERMINADO JANELAMENTO PELO MÉTODO OF2 OTIMIZADO ----------------- ###

# Definição da função para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento pelo método OF@ Otimizado.
def grafico_dado_estatistico_janelamento_OF2_otimizado(parametro, dado_estatistico, Matriz_Dados_Estatisticos_Janelamento):
    
    # Definição da variável indice_coluna_ocupações que armazena o valor do índice da coluna das ocupações.
    indice_coluna_ocupacoes = 0
    
    # Definição da variável indice_coluna_media que armazena o valor do índice da coluna das médias.
    indice_coluna_media = 1
    
    # Definição da variável indice_coluna_var que armazena o valor do índice da coluna das variâncias.
    indice_coluna_var = 2
    
    # Definição da variável indice_coluna_DP que armazena o valor do índice da coluna dos desvios padrão.
    indice_coluna_DP = 3
    
    # Definição do eixo das abscissas.
    vetor_ocupacoes = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_ocupacoes]
    
    # Comando para o nome do eixo das abscissas.
    plt.xlabel("Ocupação (OC.)", fontsize = 18)
    plt.xticks(fontsize = 16)
    
    # Caso a variável dado_estatistico seja 1 (média).
    if dado_estatistico == 1:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_media]
        
        # Caso a variável parametro seja "fase".
        if parametro == "fase":
            
            # Comando para o nome do eixo das ordenadas de acordo com a fase.
            plt.ylabel(f"Média do erro de estimação da {parametro} (ns)", fontsize = 18)
            
        else:
            
            # Comando para o nome do eixo das ordenadas de acordo com os demais parâmetros.
            plt.ylabel(f"Média do erro de estimação da {parametro} (ADC Count)", fontsize = 18)
        
    # Caso a variável dado_estatistico seja 2 (variância).
    elif dado_estatistico == 2:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_var]
        
        # Caso a variável parametro seja "fase".
        if parametro == "fase":
            
            # Comando para o nome do eixo das ordenadas de acordo com a fase.
            plt.ylabel(f"Var. do erro de estimação da {parametro} (ns)", fontsize = 18)
            
        else:
            
            # Comando para o nome do eixo das ordenadas de acordo com os demais parâmetros.
            plt.ylabel(f"Var. do erro de estimação da {parametro} (ADC Count)", fontsize = 18)
        
    # Caso a variável dado_estatistico seja 3 (desvio padrão).
    elif dado_estatistico == 3:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_DP]
        
        # Caso a variável parametro seja "fase".
        if parametro == "fase":
            
            # Comando para o nome do eixo das ordenadas de acordo com a fase.
            plt.ylabel(f"DP. do erro de estimação da {parametro} (ns)", fontsize = 18)
            
        else:
            
            # Comando para o nome do eixo das ordenadas de acordo com os demais parâmetros.
            plt.ylabel(f"DP. do erro de estimação da {parametro} (ADC Count)", fontsize = 18)
        
    # Comando que define o tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Comando para o plote do gráfico.
    plt.plot(vetor_ocupacoes, vetor_dados, color = 'blue', linestyle = '--', marker = 'o')
    
    # Comando para o grid.
    plt.grid()
    
    # Comando para o plote.
    plt.show()
        
### -------------------------------------------------------------------------------------------------------------------------------------------- ###        
        
### ---------------------------------------------------- 3) FUNÇÃO PRINCIPAL DO CÓDIGO (MAIN) -------------------------------------------------- ###

# Definição da função principal (main) do código.
def principal_grafico_dado_estatistico_janelamento_OF2_otimizado():
    
    # Impressão de mensagem no terminal.
    print("Opções de parâmetros:\nAmplitude: 1\nFase: 2\nPedestal: 3\n")
    
    # A variável parametro armazena o número do tipo inteiro digitado pelo usuário via terminal.
    parametro = int(input("Digite o número do parâmetro desejado: "))
    
    # Impressão de mensagem no terminal.
    print("Opções de análise:\nMédia: 1\nVariância: 2\nDesvio padrão: 3\n")

    # A variável dado_estatistico armazena o número do tipo inteiro digitado pelo usuário via terminal.
    dado_estatistico = int(input("Digite o número da opção desejada: "))

    # A variável valores_dados é uma lista com os valores aceitáveis para opcao.
    valores_dados = list(range(1,4,1))

    # Caso o valor digitado armazenado na variável dado_estatistico não estiver presente na lista valores_dados.
    if dado_estatistico and parametro not in valores_dados:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Caso a variável parametro seja igual a 1.
    if parametro == 1:
        
        # A variável parametro recebe a string "amplitude".
        parametro = "amplitude"
        
    # Caso a variável parametro seja igual a 2.
    elif parametro == 2:
    
        # A variável parametro recebe a string "fase".
        parametro = "fase"
        
    # Caso a variável parametro seja igual a 3.
    elif parametro == 3:
        
        # A variável parametro recebe a string "pedestal".
        parametro = "pedestal"  
    
    # A variável n_janelamento armazena a quantidade de janelamento especificada no terminal pelo usuário.
    n_janelamento = int(input("Digite a quantidade de janelamento: "))

    # A variável valores_janelamento é uma lista com os valores aceitáveis do janelamento de 7 até 19 com incremento de dois.
    valores_janelamento = list(range(7,20,2))

    # Caso o valor digitado armazenado na variável n_janelamento não estiver presente na lista valores_janelamento.
    if n_janelamento not in valores_janelamento:
    
        # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
        print("Quantidade de janelamento inválida! Opções de janelamento: 7, 9, 11, 13, 15, 17, 19.")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Chamada das funções.
    
    Matriz_Dados_Estatisticos_Janelamento = leitura_dados_estatisticos_janelamento_OF2_otimizado(parametro, n_janelamento)
    grafico_dado_estatistico_janelamento_OF2_otimizado(parametro, dado_estatistico, Matriz_Dados_Estatisticos_Janelamento)
    
# Chamada da função principal do código.
principal_grafico_dado_estatistico_janelamento_OF2_otimizado()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")
    
