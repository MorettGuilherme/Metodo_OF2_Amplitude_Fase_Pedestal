# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado).
# Autor: Guilherme Barroso Morett.
# Data: 26 de julho de 2024.

# Objetivo do código: implementação da validação cruzada K-Fold para o método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado).

""" 
Organização do código:

Importação de arquivos.
Método OF2 Otimizado para a estimação da amplitude, fase ou pedestal: metodo_OF2_otimizado.py

Funções presentes:

1) Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold pelo método OF2 Otimizado.
Entrada: número de ocupação, número do janelamento, média do dado estatístico, variância do dado estatístico, desvio padrão do dado estatístico de interesse.
Saída: nada.

2) Instrução da validação cruzada K-Fold.
Entrada: matriz com os pulsos de sinais e o vetor da amplitude, fase ou pedestal de referência.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação de bibliotecas.
import numpy as np
import os
from tqdm import tqdm
import time
from termcolor import colored

# Importação dos arquivos.*
from metodo_OF2_otimizado import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída pela técnica de validação cruzada K-Fold para o método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado).:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ---------------------- 1) INSTRUÇÃO PARA SALVAR OS DADOS ESTATÍSTICOS DO K-FOLD DO MÉTODO OF2 OTIMIZADO ------------------------------------ ###

# Definição da instrução para salvar as médias dos dados estatísticos da validação cruzada K-Fold em arquivo de saída pelo método OF2 Otimizado.
def arquivo_saida_dados_estatisticos_k_fold_erro_estimacao_OF2_otimizado(parametro, n_ocupacao, n_janelamento, media_dado_erro_estimacao, var_dado_erro_estimacao, DP_dado_erro_estimacao, dado):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = f"janelamento,media_{dado}_erro,var_{dado}_erro,DP_{dado}_erro\n"

    # Definição da pasta que contém o arquivo de saída.
    pasta_saida = f"K_Fold_{parametro}_{dado}_Dados_Estatisticos_OF2_Otimizado_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = f"k_fold_{parametro}_{dado}_dados_estatisticos_OF2_Otimizado_OC_{n_ocupacao}.txt"

    # Caminho completo para o arquivo de saída.
    caminho_arquivo_saida = os.path.join(pasta_saida, arquivo_saida)

    # Verifica se o arquivo existe e está vazio
    try:
        with open(caminho_arquivo_saida, 'r') as arquivo_saida_dados_estatisticos:
            primeiro_caractere = arquivo_saida_dados_estatisticos.read(1)
            if not primeiro_caractere:
                # Arquivo está vazio, escreva o título
                with open(caminho_arquivo_saida, 'a') as file:
                    file.write(titulo_arquivo_saida)
    except FileNotFoundError:
        # Se o arquivo não existe, cria e escreve o título
        with open(caminho_arquivo_saida, 'w') as file:
            file.write(titulo_arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        # Abre o arquivo de saída no modo de acrescentar (append).
        with open(caminho_arquivo_saida, "a") as arquivo_saida_dados_estatisticos:
            # Escrita dos dados de interesse.
            arquivo_saida_dados_estatisticos.write(f"{n_janelamento},{media_dado_erro_estimacao},{var_dado_erro_estimacao},{DP_dado_erro_estimacao}\n")
    # Excessão.
    except Exception as e:
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------------------------------------- 2) INSTRUÇÃO PARA A VALIDAÇÃO CRUZADA K-FOLD PELO MÉTODO OF2 OTIMIZADO ----------------------------------------------- ###

# Definição da instrução da técnica de validação cruzada K-Fold pelo método OF2 Otimizado.
def K_fold(parametro, n_ocupacao, n_janelamento, Matriz_Pulsos_Sinais, vetor_amplitude_referencia, vetor_fase_referencia):
    
    # Criação da lista vazia blocos_pulsos_sinais.
    blocos_pulsos_sinais = []

    # Criação da lista vazia blocos_amplitude_referencia.
    blocos_amplitude_referencia = []
    
    # Criação da lista vazia blocos_fase_referencia.
    blocos_fase_referencia = []

    # Criação da variável quantidade_blocos que armazena a quantidade de blocos.
    quantidade_blocos = 100

    # Definição da quantidade de elementos de cada bloco.
    quantidade_elementos_bloco = len(Matriz_Pulsos_Sinais) // quantidade_blocos
    
    # Para i de início em zero até a quantidade de elementos de amostras com incremento igual a quantidade_elementos_bloco.
    for i in range(0, len(Matriz_Pulsos_Sinais), quantidade_elementos_bloco):
    
        # Definição do bloco de pulsos de sinais.
        bloco_pulsos_sinais = Matriz_Pulsos_Sinais[i:i+quantidade_elementos_bloco]
        # O bloco dos pulsos de sinais é acrescentado a lista dos blocos dos pulsos de sinais.
        blocos_pulsos_sinais.append(bloco_pulsos_sinais)
    
        # Definição do bloco dos dados da amplitude de referência.
        bloco_amplitude_referencia = vetor_amplitude_referencia[i:i+quantidade_elementos_bloco]
        # O bloco da amplitude de referência é acrescentado a lista dos blocos da amplitude de referência.
        blocos_amplitude_referencia.append(bloco_amplitude_referencia)
        
        # Definição do bloco dos dados da fase de referência.
        bloco_fase_referencia = vetor_fase_referencia[i:i+quantidade_elementos_bloco]
        # O bloco da fase de referência é acrescentado a lista dos blocos da amplitude de referência.
        blocos_fase_referencia.append(bloco_fase_referencia)
        
    # Definição da lista vazia lista_bloco_media_erro_estimacao.
    lista_blocos_media_erro_estimacao = []
    
    # Definição da lista vazia lista_bloco_var_erro_estimacao.
    lista_blocos_var_erro_estimacao = []
    
    # Definição da lista vazia lista_bloco_DP_erro_estimacao.
    lista_blocos_DP_erro_estimacao = []
     
    # Para indice_bloco de 0 até o tamanho da matriz de dados de entrada com incremento igual a quantidade de elementos no bloco.
    for indice_teste in range(0, len(blocos_pulsos_sinais)):
        
        # Definição do bloco_teste_pulsos_sinais como sendo aquele de índice igual ao indice_teste.
        bloco_teste_pulsos_sinais = blocos_pulsos_sinais[indice_teste]
        
        # Definição do bloco_treino_pulsos_sinais como sendo aqueles de índices diferentes do indice_teste.
        bloco_treino_pulsos_sinais = blocos_pulsos_sinais[:indice_teste]+blocos_pulsos_sinais[indice_teste+1:]
        
        # Reescreve os elementos bloco_treino_pulsos_sinais em sequência, uma lista unidimensional.
        bloco_treino_pulsos_sinais = [elemento for sublista in bloco_treino_pulsos_sinais for elemento in sublista]
        
        # Definição do bloco_teste_amplitude_referencia como sendo aquele de índice igual ao indice_teste.
        bloco_teste_amplitude_referencia = blocos_amplitude_referencia[indice_teste]
        
        # Definição do bloco_treino_amplitude_referencia como sendo aqueles de índices diferentes do indice_teste.
        bloco_treino_amplitude_referencia = blocos_amplitude_referencia[:indice_teste]+blocos_amplitude_referencia[indice_teste+1:]
        
        # Reescreve os elementos bloco_treino_amplitude_referencia em sequência, uma lista unidimensional.
        bloco_treino_amplitude_referencia = [elemento for sublista in bloco_treino_amplitude_referencia for elemento in sublista]
        
        # Definição do bloco_teste_fase_referencia como sendo aquele de índice igual ao indice_teste.
        bloco_teste_fase_referencia = blocos_fase_referencia[indice_teste]
        
        # Definição do bloco_treino_fase_referencia como sendo aqueles de índices diferentes do indice_teste.
        bloco_treino_fase_referencia = blocos_fase_referencia[:indice_teste]+blocos_fase_referencia[indice_teste+1:]
        
        # Reescreve os elementos bloco_treino_fase_referencia em sequência, uma lista unidimensional.
        bloco_treino_fase_referencia = [elemento for sublista in bloco_treino_fase_referencia for elemento in sublista]
        
        # A variável bloco_lista_erro_estimacao_parametro recebe o valor de retorno da função metodo_BLUE1.
        Bloco_lista_erro_estimacao_parametro = metodo_OF2_otimizado(parametro, n_janelamento, bloco_treino_pulsos_sinais, bloco_teste_pulsos_sinais, bloco_teste_amplitude_referencia, bloco_teste_fase_referencia)
        
        # Cálculo dos dados estatísticos de cada bloco.
        bloco_media_erro_estimacao = np.mean(Bloco_lista_erro_estimacao_parametro)
        bloco_var_erro_estimacao = np.var(Bloco_lista_erro_estimacao_parametro)
        bloco_DP_erro_estimacao = np.std(Bloco_lista_erro_estimacao_parametro)
        
        # Adiciona essas informações em suas respectivas listas.    
        lista_blocos_media_erro_estimacao.append(bloco_media_erro_estimacao)
        lista_blocos_var_erro_estimacao.append(bloco_var_erro_estimacao)
        lista_blocos_DP_erro_estimacao.append(bloco_DP_erro_estimacao)
        
    # Cálculo dos dados estatísticos da média.
    media_media_blocos_erro_estimacao_parametro = np.mean(lista_blocos_media_erro_estimacao)
    var_media_blocos_erro_estimacao_parametro = np.var(lista_blocos_media_erro_estimacao)
    DP_media_blocos_erro_estimacao_parametro = np.std(lista_blocos_media_erro_estimacao)
     
    # Salva a informação dos dados estatísticos da média do erro de estimação do parâmetro em seus respectivos arquivos de saída.   
    arquivo_saida_dados_estatisticos_k_fold_erro_estimacao_OF2_otimizado(parametro, n_ocupacao, n_janelamento, media_media_blocos_erro_estimacao_parametro, var_media_blocos_erro_estimacao_parametro, DP_media_blocos_erro_estimacao_parametro, dado = "media")
        
    # Cálculo dos dados estatísticos da variância.
    media_var_blocos_erro_estimacao_parametro = np.mean(lista_blocos_var_erro_estimacao)
    var_var_blocos_erro_estimacao_parametro = np.var(lista_blocos_var_erro_estimacao)
    DP_var_blocos_erro_estimacao_parametro = np.std(lista_blocos_var_erro_estimacao)
      
    # Salva a informação dos dados estatísticos da variância do erro de estimação do parâmetro em seus respectivos arquivos de saída.  
    arquivo_saida_dados_estatisticos_k_fold_erro_estimacao_OF2_otimizado(parametro, n_ocupacao, n_janelamento, media_var_blocos_erro_estimacao_parametro, var_var_blocos_erro_estimacao_parametro, DP_var_blocos_erro_estimacao_parametro, dado = "var")
        
    # Cálculo dos dados estatísticos do desvio padrão.
    media_DP_blocos_erro_estimacao_parametro = np.mean(lista_blocos_DP_erro_estimacao)
    var_DP_blocos_erro_estimacao_parametro = np.var(lista_blocos_DP_erro_estimacao)
    DP_DP_blocos_erro_estimacao_parametro = np.std(lista_blocos_DP_erro_estimacao)
    
    # Salva a informação dos dados estatísticos do desvio padrão do erro de estimação do parâmetro em seus respectivos arquivos de saída.
    arquivo_saida_dados_estatisticos_k_fold_erro_estimacao_OF2_otimizado(parametro, n_ocupacao, n_janelamento, media_DP_blocos_erro_estimacao_parametro, var_DP_blocos_erro_estimacao_parametro, DP_DP_blocos_erro_estimacao_parametro, dado = "DP")
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ### 

### --------------------------- 3) INSTRUÇÃO PARA APLICAR O K-FOLD EM TODAS AS OCUPAÇÕES PELO MÉTODO OF2 OTIMIZADO ----------------------------- ###
  
# Definição da função principal (main) do código.
def principal_K_fold_OF2_otimizado():
    
    # A variável parametro_amplitude armazena a string "amplitude".
    parametro_amplitude = "amplitude"
    
    # A variável parametro_fase armazena a string "fase".
    parametro_fase = "fase"
    
    # A variável parametro_pedestal armazena a string "pedestal".
    parametro_pedestal = "pedestal"
    
    # A variável ocupacao_inicial armazena o valor inicial da ocupação que é 0.
    ocupacao_inicial = 0
    
    # A variável ocupacao_final armazena o valor final da ocupação que é 100.
    ocupacao_final = 100
    
    # A variável incremento_ocupacao armazena o valor de incremento entre as ocupações.
    incremento_ocupacao = 10
    
    # A variável n_janelamento_inicial armazena o valor inicial do janelamento que é 7.
    n_janelamento_inicial = 7
    
    # A variável n_janelamento_final armazena o valor final do janelamento que é 19.
    n_janelamento_final = 19
    
    # A variável incremento_janelamento armazena o valor do incremento entre os janelamentos.
    incremento_janelamento = 2
    
    # Para o número de ocupações de 0 até 100 com incremento de 10. 
    for n_ocupacao in tqdm(range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao)):
    
        # Para o número de janelamento de 7 até 19 com incremento de 2.
        for n_janelamento in tqdm(range(n_janelamento_inicial, n_janelamento_final+1, incremento_janelamento)):
    
            # Chamada ordenada das funções.
    
            Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao)
            
            Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
            
            vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
        
            Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
            
            Matriz_Pulsos_Sinais_Janelado, vetor_fase_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento)
            
            K_fold(parametro_amplitude, n_ocupacao, n_janelamento, Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado, vetor_fase_referencia_janelado)
    
            K_fold(parametro_fase, n_ocupacao, n_janelamento, Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado, vetor_fase_referencia_janelado)
    
            K_fold(parametro_pedestal, n_ocupacao, n_janelamento, Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado, vetor_fase_referencia_janelado)
     
# Chamada da função K_fold_OC.
principal_K_fold_OF2_otimizado()       
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

# Impressão de uma linha que representa o fim do programa.

print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")