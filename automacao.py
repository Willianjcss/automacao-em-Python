import pyautogui
import time
import pandas

# pyautogui.click
# pyautogui.write
# pyautogui.press
# pyautogui.hotkey
# pyautogui.scroll
pyautogui.PAUSE = 0.5

# Passo 1 -Entrar no sistema
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

# Entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

# Passo 2 - Fazer login
pyautogui.click(x=669, y=448)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('williancunegundes03@gmail.com')


# Digitar senha
pyautogui.press('tab')
pyautogui.write('trembolona')

pyautogui.click(x=946, y=643)

time.sleep(3)

# Passo 3 - Importar a base de dados
tabela = pandas.read_csv('produtos.csv')
print(tabela)


# Passo 4 - cadastrar o produto
for linha in tabela.index:
    # codigo
    pyautogui.click(x=643, y=303)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    # marca
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    # tipo
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    # categoria
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    # preco
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    # custo
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    # obs
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    # clicar no botão enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)
