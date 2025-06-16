import parametros as pam
import pyautogui as pg
import time

def imprimir_funcao(arquivo, cod_cliente, produto, operacao, cen_custo, fase_ob, aplicacao, cod_trecho, equipe, observacao):
    print("Iniciando a função imprimir_funcao...")
    
    # Get product details
    produto = pam.produtos.get(produto)
    print(f"Produto obtido: {produto}")
    
    # Mover e clicar na interface
    print("Movendo para as coordenadas (1560, 510) e dando um duplo clique...")
    pg.moveTo(1560, 510)
    pg.doubleClick()
    pg.write(fase_ob)
    print(f"Escrevendo fase_ob: {fase_ob}")
    time.sleep(0.3)
    
    # Selecionar o campo de código do cliente
    print("Movendo para as coordenadas (55, 325) e clicando...")
    pg.moveTo(55, 325)
    pg.click()
    pg.write(cod_cliente)
    print(f"Escrevendo cod_cliente: {cod_cliente}")
    time.sleep(0.3)
    
    # Preencher campos com tabulação
    pg.press('tab')
    pg.write(produto)
    print(f"Escrevendo produto: {produto}")
    time.sleep(0.3)
    
    pg.press('tab')
    pg.write(operacao)
    print(f"Escrevendo operacao: {operacao}")
    time.sleep(0.3)
    
    pg.write(cen_custo)
    print(f"Escrevendo cen_custo: {cen_custo}")
    time.sleep(0.3)
    
    pg.press(['tab', 'tab'])
    pg.write(aplicacao)
    print(f"Escrevendo aplicacao: {aplicacao}")
    time.sleep(0.3)
    
    pg.press(['tab', 'tab'])
    pg.write(cod_trecho)
    print(f"Escrevendo cod_trecho: {cod_trecho}")
    time.sleep(0.3)
    
    pg.write(observacao)
    print(f"Escrevendo observacao: {observacao}")
    time.sleep(0.3)
    
    pg.press(['tab', 'tab', 'tab'])
    pg.write(equipe)
    print(f"Escrevendo equipe: {equipe}")
    time.sleep(2)
    
    if len(equipe) > 4:
        print("Equipe com mais de 4 caracteres, pressionando return, tab e tab...")
        pg.press(['return', 'tab', 'tab', 'tab', 'tab', 'tab'])
    else:
        print("Equipe com 4 ou menos caracteres, pressionando tab, return e tab...")
        pg.press('tab')
        time.sleep(2)
        pg.press(['return', 'tab', 'tab', 'tab', 'tab', 'tab'])
    
    pg.write(observacao)
    print(f"Reescrevendo observacao: {observacao}")
    
    print("Função concluída.")
