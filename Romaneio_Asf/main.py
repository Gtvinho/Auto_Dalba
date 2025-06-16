import tkinter as tk
from tkinter import ttk
import parametros as pam
import auto

# Função para abrir ou mudar para a aba
def abrir_ou_mudar_aba(nome_aba, parametros):
    # Verifica se a aba já existe
    for aba in notebook.tabs():
        if notebook.tab(aba, "text") == nome_aba:
            # Se a aba já existir, muda o foco para ela
            notebook.select(aba)
            return

    # Se a aba não existir, cria uma nova aba
    nova_aba = ttk.Frame(notebook)

    # Adiciona um Canvas para permitir rolagem
    canvas = tk.Canvas(nova_aba)
    scrollbar = ttk.Scrollbar(nova_aba, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Cria o Frame que irá conter o conteúdo da aba
    content_frame = ttk.Frame(canvas)

    # Coloca o Frame dentro do Canvas
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Adiciona a barra de rolagem
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Adiciona listas suspensas para cada parâmetro com os rótulos ao lado
    # Cod. Cliente
    label_cod_cliente = tk.Label(content_frame, text="Cod. Cliente:")
    label_cod_cliente.pack(padx=10, pady=5, anchor='w')  # Ancorar à esquerda
    lista_cod_cliente = ttk.Combobox(content_frame, values=parametros["cod_clientes"], state="normal", width=30)
    lista_cod_cliente.set(parametros["cod_clientes"][0])  # Setando valor inicial
    lista_cod_cliente.pack(padx=10, pady=5)

    # Produto
    label_produto = tk.Label(content_frame, text="Produto:")
    label_produto.pack(padx=10, pady=5, anchor='w')  # Ancorar à esquerda
    lista_produto = ttk.Combobox(content_frame, values=list(parametros["produtos"].keys()), state="normal", width=30)
    lista_produto.set(list(parametros["produtos"].keys())[0])  # Setando valor inicial (primeiro nome do produto)
    lista_produto.pack(padx=10, pady=5)

    # Operação
    label_operacao = tk.Label(content_frame, text="Operação:")
    label_operacao.pack(padx=10, pady=5, anchor='w')  # Ancorar à esquerda
    lista_operacao = ttk.Combobox(content_frame, values=parametros["operacoes"], state="normal", width=30)
    lista_operacao.set(parametros["operacoes"][0])  # Setando valor inicial
    lista_operacao.pack(padx=10, pady=5)

    # Cen. Custo
    label_cen_custo = tk.Label(content_frame, text="Cen. Custo:")
    label_cen_custo.pack(padx=10, pady=5, anchor='w')  # Ancorar à esquerda
    lista_cen_custo = ttk.Combobox(content_frame, values=parametros["cen_custos"], state="normal", width=30)
    lista_cen_custo.set(parametros["cen_custos"][0])  # Setando valor inicial
    lista_cen_custo.pack(padx=10, pady=5)

    # Fase Ob
    label_fase_ob = tk.Label(content_frame, text="Fase Ob:")
    label_fase_ob.pack(padx=10, pady=5, anchor='w')  # Ancorar à esquerda
    lista_fase_ob = ttk.Combobox(content_frame, values=parametros["fase_obs"], state="normal", width=30)
    lista_fase_ob.set(parametros["fase_obs"][0])  # Setando valor inicial
    lista_fase_ob.pack(padx=10, pady=5)

    # Aplicação
    label_aplicacao = tk.Label(content_frame, text="Aplicação:")
    label_aplicacao.pack(padx=10, pady=5, anchor='w')  # Ancorar à esquerda
    lista_aplicacao = ttk.Combobox(content_frame, values=parametros["aplicacoes"], state="normal", width=30)
    lista_aplicacao.set(parametros["aplicacoes"][0])  # Setando valor inicial
    lista_aplicacao.pack(padx=10, pady=5)

    # Cod. Trecho
    label_cod_trecho = tk.Label(content_frame, text="Cod. Trecho:")
    label_cod_trecho.pack(padx=10, pady=5, anchor='w')  # Ancorar à esquerda
    lista_cod_trecho = ttk.Combobox(content_frame, values=parametros["cod_trechos"], state="normal", width=30)
    lista_cod_trecho.set(parametros["cod_trechos"][0])  # Setando valor inicial
    lista_cod_trecho.pack(padx=10, pady=5)

    # Equipe
    label_equipe = tk.Label(content_frame, text="Equipe:")
    label_equipe.pack(padx=10, pady=5, anchor='w')  # Ancorar à esquerda
    lista_equipe = ttk.Combobox(content_frame, values=parametros["equipes"], state="normal", width=30)
    lista_equipe.set(parametros["equipes"][0])  # Setando valor inicial
    lista_equipe.pack(padx=10, pady=5)

    # Observação
    label_observacao = tk.Label(content_frame, text="Observação:")
    label_observacao.pack(padx=10, pady=5, anchor='w')  # Ancorar à esquerda

    # Usando o widget Entry para permitir entrada de texto simples
    entrada_observacao = tk.Entry(content_frame, width=30)
    entrada_observacao.pack(padx=10, pady=5)

    # Se desejar, você pode setar um valor inicial para o campo de entrada
    entrada_observacao.insert(0, "Observação inicial")  # Exemplo de texto inicial

    # Cria o botão para imprimir
    botao_imprimir = tk.Button(content_frame, text=f"Imprimir {nome_aba}", 
                                command=lambda: auto.imprimir_funcao(arquivo=None, 
                                                                cod_cliente=lista_cod_cliente.get(),
                                                                produto=lista_produto.get(),
                                                                operacao=lista_operacao.get(),
                                                                cen_custo=lista_cen_custo.get(),
                                                                fase_ob=lista_fase_ob.get(),
                                                                aplicacao=lista_aplicacao.get(),
                                                                cod_trecho=lista_cod_trecho.get(),
                                                                equipe=lista_equipe.get(),
                                                                observacao=entrada_observacao.get()))
    botao_imprimir.pack(padx=10, pady=10)

    # Exibe o conteúdo da aba
    label = tk.Label(content_frame, text=f"Conteúdo da {nome_aba} carregado com sucesso!")
    label.pack(padx=10, pady=10)

    # Atualiza a área do Canvas para que a rolagem funcione
    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Adiciona a aba ao notebook
    notebook.add(nova_aba, text=nome_aba)

    # Muda para a nova aba
    notebook.select(nova_aba)

# Função para fechar a aba
def fechar_aba(aba):
    # Remove a aba do notebook
    notebook.forget(aba)

# Criando a janela principal
root = tk.Tk()
root.title("Sistema de Cadastro")
root.geometry("600x500")  # Define o tamanho fixo da janela principal

# Criando o notebook (com as abas)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Botões para abrir as abas
botao1 = tk.Button(root, text="Aba 1", command=lambda: abrir_ou_mudar_aba("Aba 1", pam.parametros_aba1))
botao1.pack(side="left", padx=10, pady=10)

botao2 = tk.Button(root, text="Aba 2", command=lambda: abrir_ou_mudar_aba("Aba 2", pam.parametros_aba2))
botao2.pack(side="left", padx=10, pady=10)

botao3 = tk.Button(root, text="Aba 3", command=lambda: abrir_ou_mudar_aba("Aba 3", pam.parametros_aba3))
botao3.pack(side="left", padx=10, pady=10)

# Iniciando a interface gráfica
root.mainloop()
