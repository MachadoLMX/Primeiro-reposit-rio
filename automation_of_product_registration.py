# Passo a passo do projetoCAHA000251    Camisa  
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas (Ctrl + C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 2

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=905, y=505)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=700, y=624) # clique no botao de login
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# Passo 3: Importar a base de produtos pra cadastrar

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
#PARA(FOR) cada linha DA(IN) minha tabela - LOOPING
for linha in tabela.index:
    # clicar no campo de código
    
    pyautogui.click(x=755, y=358)
    
    # pegar da tabela o valor do campo que a gente quer preencher
    # Para transformar algo em texto precisa transformar em string
    
    # preencher o campo 
    codigo = str(tabela.loc[linha, "codigo"])  # string = texto
    pyautogui.write(codigo)
    pyautogui.press("tab")  #passar para o proximo campo

    # preencher o campo marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    

    # preencher o campo tipo    2   19.95   5.0 

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # preencher o campo categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # preencher o campo praco_unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    # preencher o campo custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # preencher o campo obs
    obs = str(tabela.loc[linha, "obs"])
    if obs !="nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
        
 # cadastra o produto (botao enviar)
    pyautogui.press("enter")


    # dar scroll de tudo1 pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
