# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado).
# Autor: Guilherme Barroso Morett.
# Data: 26 de julho de 2024.

# Objetivo do código: análise do erro absoluto do parâmetro da amplitude, fase ou pedestal pelo método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado).

"""
Organização do Código:

Importação de arquivos.
Método OF2 Otimizado para a estimação da amplitude, fase ou pedestal: metodo_OF2_otimizado.py

Funções presentes:

1) Função para o cálculo da estatística do erro de estimação da amplitude, fase ou pedestal pelo método OF2 Otimizado.
Entrada: lista com os erros de estimação da amplitude, fase ou pedestal.
Saída: a média, a variância e o desvio padrão do erro de estimação da amplitude, fase ou pedestal.

2) Instrução para o plote do histograma do tipo A do erro de estimação da amplitude, fase ou pedestal pelo método OF2 Otimizado.
Entrada: número de ocupação, parâmetro, lista com os erros de estimação da amplitude, fase ou pedestal e seus dados estatísticos.
Saída: nada.

3) Instrução para o plote do histograma do tipo B do erro de estimação da amplitude, fase ou pedestal pelo método OF2 Otimizado.
Entrada: número de ocupação, parâmetro, lista com os erros de estimação da amplitude, fase ou pedestal e seus dados estatísticos para os janelamento 7, 15 e 19.
Saída: nada.

4) Função principal.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from termcolor import colored

# Importação dos arquivos.
from metodo_OF2_otimizado import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Análise do erro de estimação da amplitude, fase ou pedestal pelo método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado).:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------ 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE, FASE OU PEDESTAL PELO MÉTODO OF2 OTIMIZADO ------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude, fase ou pedestal pelo método OF2 otimizado.
def dados_estatisticos_erro_estimacao_parametro_OF2_otimizado(lista_erro_estimacao_parametro):
    
    # A lista do erro de estimação da amplitude, fase ou pedestal é convertida para o tipo numpy array.
    vetor_erro_estimacao_parametro = np.array(lista_erro_estimacao_parametro)

    # Cálculo da média do erro de estimação da amplitude, fase ou pedestal.
    media_erro_estimacao_parametro = np.mean(vetor_erro_estimacao_parametro)

    # Cálculo da variância do erro de estimação da amplitude, fase ou pedestal.
    var_erro_estimacao_parametro = np.var(vetor_erro_estimacao_parametro)

    # Cálculo do desvio padrão do erro de estimação da amplitude, fase ou pedestal.
    desvio_padrao_erro_estimacao_parametro = np.std(vetor_erro_estimacao_parametro)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação da amplitude, fase ou pedestal.
    return media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro
    
### --------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----- 2) FUNÇÃO PARA A CONSTRUÇÃO DO HISTOGRAMA DO TIPO A DO ERRO DE ESTIMAÇÃO DA AMPLITUDE, FASE OU PEDESTAL PELO MÉTODO OF2 OTIMIZADO ----- ###

# Definição de função para o plot do histograma do erro de estimação da amplitude, fase ou pedestal pelo método OF2 otimizado.
def histograma_A_erro_estimacao_parametro_OF2_otimizado(n_ocupacao, parametro, lista_erro_estimacao_parametro, media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro):
    
    # A lista do erro de estimação do parâmetro é convertida para o tipo numpy array.
    vetor_erro_estimacao_parametro = np.array(lista_erro_estimacao_parametro)

    # Se a variável parametro for igual a string "amplitude".
    if parametro == "amplitude":
        
        # Nomeação do eixo x de acordo com o parâmetro da amplitude.
        plt.xlabel(f'Erro de estimação da {parametro} (ADC Count)', fontsize = 18)
        
        # A variável x_inf recebe o valor inferior do eixo das abscissas para a amplitude.
        x_inf = -400
    
        # A variável x_sup recebe o valor superior do eixo das abscissas para a amplitude.
        x_sup = 400

    # Se a variável parametro for igual a string "fase".
    elif parametro == "fase":
        
        # Nomeação do eixo x de acordo com o parâmetro da fase.
        plt.xlabel(f'Erro de estimação da {parametro} (ns)', fontsize = 18)
        
        # A variável x_inf recebe o valor inferior do eixo das abscissas para a fase.
        x_inf = -10000
    
        # A variável x_sup recebe o valor superior do eixo das abscissas para a fase.
        x_sup = 10000
     
    # Se a variável parametro for igual a string "pedestal".   
    elif parametro == "pedestal":
        
        # Nomeação do eixo x de acordo com o parâmetro do pedestal.
        plt.xlabel(f'Erro de estimação do {parametro} (ADC Count)', fontsize = 18)
        
        # A variável x_inf recebe o valor inferior do eixo das abscissas para o pedestal.
        x_inf = -500
    
        # A variável x_sup recebe o valor superior do eixo das abscissas para o pedestal.
        x_sup = 500
        
    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)
    
    # A variável n_bins recebe a quantidade de bins presente no histograma.
    n_bins = 100

    # A variável texto recebe uma string com as informações de interesse.
    texto = f"Média: {round(media_erro_estimacao_parametro, 6)} \n Variância: {round(var_erro_estimacao_parametro, 6)} \n Desvio padrão: {round(desvio_padrao_erro_estimacao_parametro, 6)}"

    # Definição do histograma a partir do vetor vetor_erro_parametro.
    plt.hist(vetor_erro_estimacao_parametro, bins = n_bins, range = [x_inf, x_sup], edgecolor = 'black', linewidth = 1.2)
    
    # Definição do título do histograma.
    #plt.title(f"Ocupação {n_ocupacao}")
    
    # Posicionamento do texto no gráfico.
    plt.text(0.99, 0.98, texto, horizontalalignment = 'right',
    verticalalignment = 'top',
    transform = plt.gca().transAxes,
    bbox = dict(facecolor = 'white', alpha = 0.5),
    fontsize = 14)

    # Criação de grid.
    plt.grid()

    # Exibição do gráfico.
    plt.show()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----- 2) FUNÇÃO PARA A CONSTRUÇÃO DO HISTOGRAMA DO TIPO B DO ERRO DE ESTIMAÇÃO DA AMPLITUDE, FASE OU PEDESTAL PELO MÉTODO OF2 OTIMIZADO ---- ###

# Definição de função para o plot dos histogramas do erro de estimação da amplitude, fase ou pedestal para diferentes janelamentos para uma dada ocupação pelo método OF2 otimizado.
def histograma_B_erro_estimacao_parametro_OF2_otimizado(n_ocupacao, parametro, lista_erro_estimacao_parametro_J7, media_erro_estimacao_parametro_J7, var_erro_estimacao_parametro_J7, desvio_padrao_erro_estimacao_parametro_J7, lista_erro_estimacao_parametro_J15, media_erro_estimacao_parametro_J15, var_erro_estimacao_parametro_J15, desvio_padrao_erro_estimacao_parametro_J15, lista_erro_estimacao_parametro_J19, media_erro_estimacao_parametro_J19, var_erro_estimacao_parametro_J19, desvio_padrao_erro_estimacao_parametro_J19):
    
    # A lista do erro de estimação do parâmetro para o janelamento 7 é convertida para o tipo numpy array.
    vetor_erro_estimacao_parametro_J7 = np.array(lista_erro_estimacao_parametro_J7)
    
    # A lista do erro de estimação do parâmetro para o janelamento 15 é convertida para o tipo numpy array.
    vetor_erro_estimacao_parametro_J15 = np.array(lista_erro_estimacao_parametro_J15)
    
    # A lista do erro de estimação do parâmetro para o janelamento 19 é convertida para o tipo numpy array.
    vetor_erro_estimacao_parametro_J19 = np.array(lista_erro_estimacao_parametro_J19)

    # Se a variável parametro for igual a string "amplitude".
    if parametro == "amplitude":
        
        # Nomeação do eixo x de acordo com o parâmetro da amplitude.
        plt.xlabel(f'Erro de estimação da {parametro} (ADC Count)', fontsize = 18)

    # Se a variável parametro for igual a string "fase".
    elif parametro == "fase":
        
        # Nomeação do eixo x de acordo com o parâmetro da fase.
        plt.xlabel(f'Erro de estimação da {parametro} (ns)', fontsize = 18)
     
    # Se a variável parametro for igual a string "pedestal".   
    else:
        
        # Nomeação do eixo x de acordo com o parâmetro do pedestal.
        plt.xlabel(f'Erro de estimação do {parametro} (ADC Count)', fontsize = 18)
        
    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)
    
    # A variável n_bins recebe a quantidade de bins presente no histograma.
    n_bins = 100
    
    # A variável x_inf recebe o valor inferior do eixo das abscissas.
    x_inf = -400
    
    # A variável x_sup recebe o valor superior do eixo das abscissas.
    x_sup = 400
    
    # A variável legenda_J7 recebe a legenda do histograma para o janelamento 7.
    legenda_J7 = f'Janelamento 7\nMédia: {round(media_erro_estimacao_parametro_J7, 6)}\nVariância: {round(var_erro_estimacao_parametro_J7,6)}\nDesvio Padrão: {round(desvio_padrao_erro_estimacao_parametro_J7, 6)}'
    
    # A variável legenda_J15 recebe a legenda do histograma para o janelamento 15.
    legenda_J15 = f'Janelamento 15\nMédia: {round(media_erro_estimacao_parametro_J15, 6)}\nVariância: {round(var_erro_estimacao_parametro_J15,6)}\nDesvio Padrão: {round(desvio_padrao_erro_estimacao_parametro_J15, 6)}'
    
    # A variável legenda_J19 recebe a legenda do histograma para o janelamento 19.
    legenda_J19 = f'Janelamento 19\nMédia: {round(media_erro_estimacao_parametro_J19, 6)}\nVariância: {round(var_erro_estimacao_parametro_J19,6)}\nDesvio Padrão: {round(desvio_padrao_erro_estimacao_parametro_J19, 6)}'
    
    # Definição dos histogramas para diferentes janelamentos e uma dada ocupação.
    plt.hist(vetor_erro_estimacao_parametro_J7, bins = n_bins, color='blue', range = [x_inf, x_sup], histtype = 'step', label = legenda_J7)
    plt.hist(vetor_erro_estimacao_parametro_J15, bins = n_bins, color='green', range = [x_inf, x_sup], histtype = 'step', label = legenda_J15)
    plt.hist(vetor_erro_estimacao_parametro_J19, bins = n_bins, color='red', range = [x_inf, x_sup], histtype = 'step', label = legenda_J19)
    
    # Definição do título do histograma.
    plt.title(f"Ocupação {n_ocupacao}", fontsize = 16)
    
    # Definição da legenda do histograma.
    plt.legend(fontsize = 14)

    # Criação de grid.
    plt.grid()

    # Exibição do gráfico.
    plt.show()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO (MAIN) ------------------------------------------------------------- ###

# Definição da função principal (main) do código.
def principal_histograma_erro_estimacao_parametro_OF2_otimizado():
    
    # Impressão de mensagem no terminal.
    print("Opções de parâmetros:\nAmplitude: 1\nFase: 2\nPedestal: 3\n")
    
    # A variável parametro armazena o número do tipo inteiro digitado pelo usuário via terminal.
    parametro = int(input("Digite o número do parâmetro desejado: "))
    
    # A variável valores_parametro é uma lista com os valores aceitáveis para o parametro.
    valores_parametro = list(range(1,4,1))

    # Caso o valor digitado armazenado na variável paraemtro não estiver presente na lista valores_parametro.
    if parametro not in valores_parametro:
    
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
    
    # A variável numero_ocupacao armazena o valor digitado da ocupação desejada no terminal pelo usuário.
    n_ocupacao = float(input("Digite o valor da ocupação desejada: "))

    # A variável valores_ocupacao é uma lista com os valores aceitáveis de ocupação de 0 até 100.
    valores_ocupacao = list(range(0,101,10))

    # Caso o valor digitado armazenado na variável n_ocupacao não estiver presente na lista valores_ocupacao.
    if n_ocupacao not in valores_ocupacao:
    
        # Exibição de uma mensagem de alerta de que a ocupação solicitada é inválida.
        print("\nNúmero de ocupação inválida!\n")
        # A execução do programa é interrompida.
        exit(1) 

    # O tipo da variável n_ocupacao é convertida para inteiro.
    # Obs.: essa conversão possibilita que a leitura do arquivo possa ser feita corretamente.
    n_ocupacao = int(n_ocupacao)
    
    # Impressão de mensagem no terminal.
    print("Opções de histogramas:\nA: histograma para um dado janelamento e ocupação.\nB: histogramas para os janelamentos 7, 15 e 19 para a ocupação desejada.")
    
    # A variável tipo_histograma armazena a string digitada pelo usuário.
    tipo_histograma = str(input("Digite a opção do histograma desejada: "))
    
    # A variável valores_histogramas é uma lista com os valores aceitáveis para a variável tipo_histograma.
    valores_histogramas = ["A", "B"]
    
    # Caso o valor digitado armazenado na variável tipo_histograma não estiver presente na lista valores_histogramas.
    if tipo_histograma not in valores_histogramas:
    
        # Exibição de uma mensagem de alerta de que a opção do tipo de histograma é inválida.
        print("A opção do tipo de histograma digitada é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # Caso a variável tipo_histogramas seja "A".
    if tipo_histograma == "A":
    
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

        # Chamada ordenada das funções.
    
        Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao) 
    
        Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
    
        vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
    
        Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
    
        Matriz_Pulsos_Sinais_Janelado, vetor_fase_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento)   
    
        Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_amplitude_referencia_treino_janelado, vetor_amplitude_referencia_teste_janelado = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado)
    
        Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_fase_referencia_treino_janelado, vetor_fase_referencia_teste_janelado = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado, vetor_fase_referencia_janelado)
    
        lista_erro_estimacao_parametro = metodo_OF2_otimizado(parametro, n_janelamento, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_amplitude_referencia_teste_janelado, vetor_fase_referencia_teste_janelado)

        media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro = dados_estatisticos_erro_estimacao_parametro_OF2_otimizado(lista_erro_estimacao_parametro)
    
        histograma_A_erro_estimacao_parametro_OF2_otimizado(n_ocupacao, parametro, lista_erro_estimacao_parametro, media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro)
    
    # Caso a variável tipo_histograma seja "B".
    else:
        
        # A variável n_janelamento_7 recebe a quantidade do janelamento 7.
        n_janelamento_J7 = 7
        # A variável n_janelamento_15 recebe a quantidade do janelamento 15.
        n_janelamento_J15 = 15
        # A variável n_janelamento_19 recebe a quantidade do janelamento 19.
        n_janelamento_J19 = 19
        
        # Chamada ordenada das funções.
    
        Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao) 
    
        Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
    
        vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
    
        Matriz_Pulsos_Sinais_Janelado_J7, vetor_amplitude_referencia_janelado_J7 = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento_J7)
        Matriz_Pulsos_Sinais_Janelado_J15, vetor_amplitude_referencia_janelado_J15 = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento_J15)
        Matriz_Pulsos_Sinais_Janelado_J19, vetor_amplitude_referencia_janelado_J19 = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento_J19)
    
        Matriz_Pulsos_Sinais_Janelado_J7, vetor_fase_referencia_janelado_J7 = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento_J7)   
        Matriz_Pulsos_Sinais_Janelado_J15, vetor_fase_referencia_janelado_J15 = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento_J15)
        Matriz_Pulsos_Sinais_Janelado_J19, vetor_fase_referencia_janelado_J19 = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento_J19)
    
        Matriz_Pulsos_Sinais_Treino_Janelado_J7, Matriz_Pulsos_Sinais_Teste_Janelado_J7, vetor_amplitude_referencia_treino_janelado_J7, vetor_amplitude_referencia_teste_janelado_J7 = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado_J7, vetor_amplitude_referencia_janelado_J7)
        Matriz_Pulsos_Sinais_Treino_Janelado_J15, Matriz_Pulsos_Sinais_Teste_Janelado_J15, vetor_amplitude_referencia_treino_janelado_J15, vetor_amplitude_referencia_teste_janelado_J15 = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado_J15, vetor_amplitude_referencia_janelado_J15)
        Matriz_Pulsos_Sinais_Treino_Janelado_J19, Matriz_Pulsos_Sinais_Teste_Janelado_J19, vetor_amplitude_referencia_treino_janelado_J19, vetor_amplitude_referencia_teste_janelado_J19 = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado_J19, vetor_amplitude_referencia_janelado_J19)
    
        Matriz_Pulsos_Sinais_Treino_Janelado_J7, Matriz_Pulsos_Sinais_Teste_Janelado_J7, vetor_fase_referencia_treino_janelado_J7, vetor_fase_referencia_teste_janelado_J7 = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado_J7, vetor_fase_referencia_janelado_J7)
        Matriz_Pulsos_Sinais_Treino_Janelado_J15, Matriz_Pulsos_Sinais_Teste_Janelado_J15, vetor_fase_referencia_treino_janelado_J15, vetor_fase_referencia_teste_janelado_J15 = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado_J15, vetor_fase_referencia_janelado_J15)
        Matriz_Pulsos_Sinais_Treino_Janelado_J19, Matriz_Pulsos_Sinais_Teste_Janelado_J19, vetor_fase_referencia_treino_janelado_J19, vetor_fase_referencia_teste_janelado_J19 = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado_J19, vetor_fase_referencia_janelado_J19)
    
        lista_erro_estimacao_parametro_J7 = metodo_OF2_otimizado(parametro, n_janelamento_J7, Matriz_Pulsos_Sinais_Treino_Janelado_J7, Matriz_Pulsos_Sinais_Teste_Janelado_J7, vetor_amplitude_referencia_teste_janelado_J7, vetor_fase_referencia_teste_janelado_J7)
        media_erro_estimacao_parametro_J7, var_erro_estimacao_parametro_J7, desvio_padrao_erro_estimacao_parametro_J7 = dados_estatisticos_erro_estimacao_parametro_OF2_otimizado(lista_erro_estimacao_parametro_J7)
    
        lista_erro_estimacao_parametro_J15 = metodo_OF2_otimizado(parametro, n_janelamento_J15, Matriz_Pulsos_Sinais_Treino_Janelado_J15, Matriz_Pulsos_Sinais_Teste_Janelado_J15, vetor_amplitude_referencia_teste_janelado_J15, vetor_fase_referencia_teste_janelado_J15)
        media_erro_estimacao_parametro_J15, var_erro_estimacao_parametro_J15, desvio_padrao_erro_estimacao_parametro_J15 = dados_estatisticos_erro_estimacao_parametro_OF2_otimizado(lista_erro_estimacao_parametro_J15)
    
        lista_erro_estimacao_parametro_J19 = metodo_OF2_otimizado(parametro, n_janelamento_J19, Matriz_Pulsos_Sinais_Treino_Janelado_J19, Matriz_Pulsos_Sinais_Teste_Janelado_J19, vetor_amplitude_referencia_teste_janelado_J19, vetor_fase_referencia_teste_janelado_J19)
        media_erro_estimacao_parametro_J19, var_erro_estimacao_parametro_J19, desvio_padrao_erro_estimacao_parametro_J19 = dados_estatisticos_erro_estimacao_parametro_OF2_otimizado(lista_erro_estimacao_parametro_J19)
    
        histograma_B_erro_estimacao_parametro_OF2_otimizado(n_ocupacao, parametro, lista_erro_estimacao_parametro_J7, media_erro_estimacao_parametro_J7, var_erro_estimacao_parametro_J7, desvio_padrao_erro_estimacao_parametro_J7, lista_erro_estimacao_parametro_J15, media_erro_estimacao_parametro_J15, var_erro_estimacao_parametro_J15, desvio_padrao_erro_estimacao_parametro_J15, lista_erro_estimacao_parametro_J19, media_erro_estimacao_parametro_J19, var_erro_estimacao_parametro_J19, desvio_padrao_erro_estimacao_parametro_J19)
    
# Chamada da função principal (main) do código.
principal_histograma_erro_estimacao_parametro_OF2_otimizado()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###
# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")