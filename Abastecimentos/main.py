from imports import *
import pyautogui

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Lançamento de Abastecimentos")
        self.root.geometry("500x500")  # Tamanho da janela aumentado

        self.veiculos = []
        self.horario_inicial = datetime.strptime("07:00", "%H:%M")
        self.dias_para_reduzir = 1  # Valor padrão

        # Combobox para quantidade de dias
        tk.Label(root, text="Dias a reduzir na data:").grid(row=0, column=0, sticky="e")
        self.combo_dias = ttk.Combobox(root, values=["1", "2", "3"], state="readonly")
        self.combo_dias.grid(row=0, column=1)
        self.combo_dias.current(0)

        # Combobox para Posto
        tk.Label(root, text="Posto:").grid(row=1, column=0, sticky="e")
        self.combo_posto = ttk.Combobox(root, values=pr.posto, state="readonly")
        self.combo_posto.grid(row=1, column=1)
        self.combo_posto.current(0)

        # Entradas de dados
        tk.Label(root, text="Prefixo:").grid(row=2, column=0, sticky="e")
        self.entry_prefixo = tk.Entry(root)
        self.entry_prefixo.grid(row=2, column=1)

        tk.Label(root, text="Quantidade (litros):").grid(row=3, column=0, sticky="e")
        self.entry_quantidade = tk.Entry(root)
        self.entry_quantidade.grid(row=3, column=1)

        tk.Label(root, text="Horímetro:").grid(row=4, column=0, sticky="e")
        self.entry_horimetro = tk.Entry(root)
        self.entry_horimetro.grid(row=4, column=1)

        tk.Label(root, text="Hodômetro:").grid(row=5, column=0, sticky="e")
        self.entry_hodometro = tk.Entry(root)
        self.entry_hodometro.grid(row=5, column=1)

        self.btn_adicionar = tk.Button(root, text="Adicionar Veículo", command=self.adicionar_veiculo)
        self.btn_adicionar.grid(row=6, column=0, pady=10)

        self.btn_salvar_tudo = tk.Button(root, text="Salvar Todos", command=self.salvar_todos_com_confirmacao)
        self.btn_salvar_tudo.grid(row=6, column=1, pady=10)

        self.label_status = tk.Label(root, text="Veículos adicionados: 0")
        self.label_status.grid(row=7, column=0, columnspan=2)

    def adicionar_veiculo(self):
        data = self.combo_dias.get()
        posto = self.combo_posto.get()
        prefixo = self.entry_prefixo.get().strip()
        quantidade = self.entry_quantidade.get().strip()
        horimetro = self.entry_horimetro.get().strip()
        hodometro = self.entry_hodometro.get().strip()

        if not prefixo or not quantidade:
            messagebox.showwarning("Erro", "Preencha pelo menos prefixo e quantidade.")
            return

        horario_veiculo = self.horario_inicial + timedelta(minutes=15 * len(self.veiculos))
        veiculo = Veiculo(prefixo, quantidade, horimetro, hodometro, horario_veiculo, posto, data)
        self.veiculos.append(veiculo)

        messagebox.showinfo("Sucesso", f"Veículo {prefixo} adicionado com horário {horario_veiculo.strftime('%H:%M')} e posto {posto}.")

        self.entry_prefixo.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_horimetro.delete(0, tk.END)
        self.entry_hodometro.delete(0, tk.END)

        self.label_status.config(text=f"Veículos adicionados: {len(self.veiculos)}")

    def salvar_todos_com_confirmacao(self):
        if not self.veiculos:
            messagebox.showwarning("Aviso", "Nenhum veículo para salvar.")
            return
        self.dias_para_reduzir = int(self.combo_dias.get())  # Captura o valor do combo dias
        self._salvar_veiculo_idx(0)

    def _salvar_veiculo_idx(self, idx):
        time.sleep(0.3)
        pyautogui.moveTo(2490,725)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        if idx >= len(self.veiculos):
            messagebox.showinfo("Sucesso", "Todos os veículos foram salvos.")
            self.veiculos.clear()
            self.label_status.config(text="Veículos adicionados: 0")
            return

        v = self.veiculos[idx]

        print(f"\n--- Veículo #{idx+1} ---")
        print(f"Posto: {v.posto}")
        print(f"Prefixo: {v.prefixo}")
        print(f"Quantidade: {v.quantidade}")
        print(f"Horímetro: {v.horimetro}")
        print(f"Hodômetro: {v.hodometro}")
        print(f"Horário: {v.horario.strftime('%H:%M')}")
        print("------------------------\n")

        # Verifica se o veículo foi editado para decidir se reduz a data
        reduzir_data = True if not getattr(v, 'editado', False) else False
        auto.auto(v, self.dias_para_reduzir, reduzir_data=reduzir_data)

        time.sleep(1)

        msg = (f"Confira os dados do veículo #{idx+1}:\n\n"
               f"Posto: {v.posto}\n"
               f"Prefixo: {v.prefixo}\n"
               f"Quantidade: {v.quantidade}\n"
               f"Horímetro: {v.horimetro}\n"
               f"Hodômetro: {v.hodometro}\n"
               f"Horário: {v.horario.strftime('%H:%M')}\n\n"
               "Clique 'Sim' para confirmar e salvar,\n"
               "'Não' para alterar os dados.")

        resposta = messagebox.askyesno("Confirmação", msg)

        if resposta:
            print(f"Veículo salvo: {v}")
            self._salvar_veiculo_idx(idx + 1)
        else:
            self.editar_veiculo(idx)

    def editar_veiculo(self, idx):
        v = self.veiculos[idx]

        def salvar_edicao():
            v.posto = entry_posto_edit.get()
            v.prefixo = entry_prefixo_edit.get().strip()
            v.quantidade = entry_quantidade_edit.get().strip()
            v.horimetro = entry_horimetro_edit.get().strip()
            v.hodometro = entry_hodometro_edit.get().strip()
            v.editado = True  # Marca que o veículo foi editado para não reduzir data
            pyautogui.moveTo(2535, 695)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(0.3)
            top_edit.destroy()
            self._salvar_veiculo_idx(idx)

        top_edit = tk.Toplevel(self.root)
        top_edit.title(f"Editar veículo #{idx+1}")

        tk.Label(top_edit, text="Posto:").grid(row=0, column=0, sticky="e")
        entry_posto_edit = ttk.Combobox(top_edit, values=pr.posto, state="readonly")
        entry_posto_edit.grid(row=0, column=1)
        entry_posto_edit.set(v.posto)

        tk.Label(top_edit, text="Prefixo:").grid(row=1, column=0, sticky="e")
        entry_prefixo_edit = tk.Entry(top_edit)
        entry_prefixo_edit.grid(row=1, column=1)
        entry_prefixo_edit.insert(0, v.prefixo)

        tk.Label(top_edit, text="Quantidade (litros):").grid(row=2, column=0, sticky="e")
        entry_quantidade_edit = tk.Entry(top_edit)
        entry_quantidade_edit.grid(row=2, column=1)
        entry_quantidade_edit.insert(0, v.quantidade)

        tk.Label(top_edit, text="Horímetro:").grid(row=3, column=0, sticky="e")
        entry_horimetro_edit = tk.Entry(top_edit)
        entry_horimetro_edit.grid(row=3, column=1)
        entry_horimetro_edit.insert(0, v.horimetro)

        tk.Label(top_edit, text="Hodômetro:").grid(row=4, column=0, sticky="e")
        entry_hodometro_edit = tk.Entry(top_edit)
        entry_hodometro_edit.grid(row=4, column=1)
        entry_hodometro_edit.insert(0, v.hodometro)

        tk.Button(top_edit, text="Salvar Alterações", command=salvar_edicao).grid(row=5, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()
