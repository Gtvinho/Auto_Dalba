import time 
import pyautogui as pg

def salvar_notas(qnt_notas):
    x = 0 
    time.sleep(2)
    while qnt_notas != 0: 
        pg.moveTo(2485,325)
        pg.click()
        time.sleep(0.5)
        for _ in range(2):  
            pg.moveTo(1940,560)
            pg.click()
            pg.moveTo(810,670)
            pg.click()
            time.sleep(3)
            input("Pressione Enter para continuar...")
        pg.moveTo(1995,420)
        pg.doubleClick()
        pg.hotkey('ctrl','c')
        pg.hotkey('ctrl','c')
        pg.moveTo(2000,580)
        pg.click()
        time.sleep(1)
        pg.moveTo(1940,560)
        pg.click()
        pg.moveTo(810,670)
        pg.click()
        input("Pressione Enter para continuar...")
        time.sleep(0.3)
        pg.moveTo(3020,95)
        pg.click()
        if x == 0:
            time.sleep(2)
            pg.moveTo(2510,400) 
            pg.click()
            pg.write("C:\\NOTA FISCAL\\Marmeleiro")
            time.sleep(0.5)
            pg.moveTo(2320,735)
            pg.click()
            x = 1
        time.sleep(0.5)
        pg.hotkey('ctrl','v')
        pg.press("return")
        print(f"Nota {qnt_notas} baixada")  # Corrigido usando f-string
        time.sleep(0.5)
        pg.hotkey('ctrl', 'w')
        time.sleep(0.5)
        pg.hotkey('ctrl', 'w')
        qnt_notas = qnt_notas - 1
