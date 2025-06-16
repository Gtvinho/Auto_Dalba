import tkinter as tk
import principal

# Função que será chamada ao clicar no botão
def continuar():
    root.iconify()  # Minimiza a janela
    qnt_notas = int(entry_qnt_notas.get())  # Obtém o valor digitado
    print(f"Quantidade de notas: {qnt_notas}")
    principal.salvar_notas(qnt_notas)
    
    # Minimiza a janela após clicar no botão
   

# Criação da janela principal
root = tk.Tk()
root.title("Janela de Notas")  # Título da janela

# Aumenta o tamanho da janela
root.geometry("400x300")  # Largura de 400px e altura de 300px (ajuste conforme necessário)

# Label e Entry para o parâmetro qnt_notas
label_qnt_notas = tk.Label(root, text="Quantidade de Notas:")
label_qnt_notas.pack(pady=10)

entry_qnt_notas = tk.Entry(root)
entry_qnt_notas.pack(pady=5)

# Botão de continuar
botao_continuar = tk.Button(root, text="Continuar", command=continuar)
botao_continuar.pack(pady=20)

# Inicia o loop principal da interface
root.mainloop()
