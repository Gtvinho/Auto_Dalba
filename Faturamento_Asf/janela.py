import tkinter as tk
from tkinter import messagebox
import principal
def exibir_valores():
    resposta = messagebox.askyesno("Confirmar", "Deseja continuar com o processamento das notas?")
    
    if resposta:
        try:
            nota_inicial = int(entry_nota_inicial.get())
            nota_final = int(entry_nota_final.get())
            notas_ignorar = entry_notas_ignorar.get()
            numeros_lista = list(map(int, notas_ignorar.split(';')))
            
            root.iconify()

            principal.gerar_notas(nota_inicial, nota_final, numeros_lista)
            
            messagebox.showinfo("Sucesso", "Notas processadas com sucesso!")
            root.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para as notas.")
    else:
        print("O usuário cancelou o processamento.")

root = tk.Tk()
root.title("Notas - Entradas")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_nota_inicial = tk.Label(frame, text="Nota Inicial:")
label_nota_inicial.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_nota_inicial = tk.Entry(frame)
entry_nota_inicial.grid(row=0, column=1, padx=10, pady=5)

label_nota_final = tk.Label(frame, text="Nota Final:")
label_nota_final.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_nota_final = tk.Entry(frame)
entry_nota_final.grid(row=1, column=1, padx=10, pady=5)

label_notas_ignorar = tk.Label(frame, text="Notas a Ignorar:")
label_notas_ignorar.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_notas_ignorar = tk.Entry(frame)
entry_notas_ignorar.grid(row=2, column=1, padx=10, pady=5)

btn_exibir = tk.Button(frame, text="Continuar", command=exibir_valores)
btn_exibir.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()