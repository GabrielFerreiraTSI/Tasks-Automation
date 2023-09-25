import pyautogui
from time import sleep

# Cadastrar usuário
pyautogui.click(841,775, duration=0.5)
pyautogui.click(651,455, duration=0.5)
pyautogui.click(645,399, duration=0.5)
pyautogui.write("Gabriel")
pyautogui.click(641,427, duration=0.5)
pyautogui.write("35153A")
pyautogui.click(651,455, duration=0.2)

# Entrar na minha conta.
pyautogui.click(645,399, duration=0.5)
pyautogui.write("Gabriel")
pyautogui.click(641,427, duration=0.5)
pyautogui.write("35153A")
pyautogui.click(553,460, duration=0.2)

# Extrair produtos
with open("produtos.txt", "r") as arquivo:
    for linha in arquivo:
        produto = linha.split(",")[0]
        quantidade = linha.split(",")[1]
        preco = linha.split(",")[2]

        # Registrar os produtos
        pyautogui.click(356,386, duration=0.5)
        pyautogui.write(produto)
        pyautogui.click(359,413, duration=0.5)
        pyautogui.write(quantidade)
        pyautogui.click(358,439, duration=0.5)
        pyautogui.write(preco)
        pyautogui.click(276,599, duration=0.2)
        sleep(1)
        