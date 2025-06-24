from imports import *
import pyautogui as pg
import pyperclip as pp

def data(dt, dias_para_reduzir): 
    try:
        # Converte a string de data para objeto datetime
        data_obj = datetime.strptime(dt.strip(), "%d/%m/%Y")
        # Reduz a quantidade de dias definida
        data_menos = data_obj - timedelta(days=dias_para_reduzir)
        # Converte de volta para string no formato brasileiro
        nova_data_str = data_menos.strftime("%d/%m/%Y")
        print(f"Data original: {dt} -> Nova data: {nova_data_str}")
        # Digita a nova data no campo atual da tela
        pg.write(nova_data_str)
        return nova_data_str
    except ValueError:
        print(f"Erro: Formato de data inválido: {dt}. Use dd/mm/aaaa.")
        return None

def auto(v, dias_para_reduzir, reduzir_data=True):
    # Clicar na posição da janela do sistema (ajuste conforme sua tela)
    pg.moveTo(2085, 475)
    time.sleep(0.5)
    pg.click()

    # Preencher o campo do prefixo
    pg.press("home")
    pg.write(v.prefixo.upper())
    time.sleep(0.3)

    # Ir para o campo da data (2 TABs)
    pg.press(["tab", "tab"])
    time.sleep(0.5)

    # Copiar a data atual da tela
    pg.hotkey("ctrl", "c")
    dt = pp.paste()
    print(f"Data copiada da tela: {dt}")

    # Corrigir a data com base no número de dias a reduzir
    if reduzir_data:
        data(dt, dias_para_reduzir)  # A função já escreve a nova data
    else:
        pg.write(dt)

    # Preencher o horário
    pg.write(v.horario.strftime('%H:%M'))

    # Preencher o horímetro
    if len(v.horimetro) == 6: 
        pg.write(v.horimetro)
    else:  
        pg.write(v.horimetro)
        pg.press("tab")

    # Preencher o campo do posto, baseado no posto selecionado
    match v.posto:
        case "CL04": 
            pg.write(pr.CL04[0])
            pg.write(pr.CL04[1])
            pg.press("tab")
            time.sleep(0.3)
            pg.write(pr.CL04[2])
        case "S500": 
            pg.write(pr.S500[0])
            pg.write(pr.S500[1])
            pg.press("tab")
            time.sleep(0.3)
            pg.write(pr.S500[2])
        case "S10":
            pg.write(pr.S10[0])
            pg.write(pr.S10[1])
            pg.press("tab")
            time.sleep(0.3)
            pg.write(pr.S10[2])
        case _:
            pg.write("Código inválido")

    # Avança 2 TABs até o campo da quantidade
    pg.press(["tab", "tab"])
    pg.write(str(v.quantidade))

    # Se o hodômetro for 0, apenas move até o botão de salvar
    if v.hodometro == 0 or v.hodometro == "":
        pg.moveTo(2575, 405)  # Ajuste essa posição conforme seu sistema
    else: 
        # Avança 4 TABs até o campo hodômetro
        pg.press(["tab", "tab", "tab", "tab"])
        pg.write(str(v.hodometro))
        # Depois move até o botão salvar
        pg.moveTo(2575, 405)

    time.sleep(0.5)
    pg.click()
