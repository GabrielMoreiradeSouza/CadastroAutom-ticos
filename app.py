# Instalar bibliotecas
# Usar as bibliotecas no meu código
# Iniciar a automação
# Abrir o navegador
# Entrar no site
# Autenticar no site
# Carregar o arquivo que contem os dados a serem inseridos
# Cadastrar os alunos
# -> Repetir os passos acima até cadastrar todos os alunos

import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.6
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write('https://aula01.simplificapython.com.br/')
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=802, y=665)
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("simplificapython")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
tabela = pandas.read_csv("alunos.csv")
for linha in tabela.index:
    pyautogui.click(x=770, y=383)
    nome = tabela.loc[linha, "Nome"]
    pyautogui.write(nome)
    pyautogui.press("tab")
    email = tabela.loc[linha, "Email"]
    pyautogui.write(email)
    pyautogui.press("tab")
    endereco = tabela.loc[linha, "Endereco"]
    pyautogui.write(endereco)
    pyautogui.press("tab")
    telefone = tabela.loc[linha, "Telefone"]
    pyautogui.write(telefone)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.scroll(5000)
