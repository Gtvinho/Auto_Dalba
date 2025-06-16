import pyautogui as pg
import time
def gerar_notas( nota_inicial, nota_final, lista_ignorar ): 
    time.sleep(1)
    nota_total = nota_inicial - nota_final 
    x = 0
    nota_atual = nota_inicial 
    while ( nota_total >= 0): 
        

        if nota_atual in lista_ignorar: 
            print(f"A variável {nota_atual} não fatura ou já foi faturada.")
            print("Setinha para cima")
            pg.press('up')
        
        else:
            if x == 1: 
                time.sleep(1)
                pg.press('up')
            
            #Deve filtar ? 1140 130
            #Clicar uma vez na primeira pra selecionar a janlea ? 
            #Deve dar uma seta para cima na primeira ? 
            print("seleciona a tela do totvs")
            pg.moveTo(1140,130)
            pg.click()
            time.sleep(1)
            print("Move para outras acoes")
            pg.moveTo(390, 160)
            time.sleep(1)
            print("Clica ")
            pg.click()
            time.sleep(2)

            print("Move para gerar NF")
            pg.moveTo(390, 300)
            time.sleep(1.5)
            print("Clica")
            pg.click()
            print("Move para caixa")
            pg.moveTo(845, 500)
            time.sleep(1.5)
            pg.click()
            print("escreve 015")
            pg.write("015")
            print("Move para selecionar os pedidos/romaneio")
            pg.moveTo(900, 675)
            time.sleep(1.5)
            print("Clica")
            pg.click()
            print("tecla END")
            pg.press("end")
            print("tecla ENTER")
            pg.press("return")
            print("Move para confirma")
            pg.moveTo(1110, 530)
            time.sleep(1.5)
            print("Clica")
            pg.click()            
            print("Move para confirma")
            pg.moveTo(1260, 385)
            time.sleep(1.5)
            print("Clica")
            pg.click()
            print("Move para confirmar automatico")
            pg.moveTo(1175, 630)
            time.sleep(1.5)
            print("Clica")
            pg.click()
            print("Move para canto de X para fechar pdf")
            pg.moveTo(1900, 15)
            time.sleep(1.5)
            print("Esperar 15 segundos")
            time.sleep(15.5)
            print("Clica")
            pg.click()
            print("Esperar 2 segundos")
            time.sleep(2.5)
            print(f"A variável {nota_atual} Faturada.")
        print("||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||")
        nota_total = nota_total - 1
        nota_atual = nota_atual - 1
        x = 1
