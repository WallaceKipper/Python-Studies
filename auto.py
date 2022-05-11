import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
#Abrir o Navegador
#pyautogui.press("winleft")
#pyautogui.write("chrome")
#pyautogui.press("enter")
#pyautogui.alert("Vai Começar, aperta ok e não mexa em nada")
pyautogui.hotkey('ctrl','t')
#Abrir o driver
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")
time.sleep(15)
#Baixar a base de dados atualizado
pyautogui.click(418, 301, clicks=2)
time.sleep(2)
pyautogui.click(418, 301, clicks=1)
time.sleep(2)
pyautogui.click(1156, 189, clicks=1)
time.sleep(1)
pyautogui.click(984, 582, clicks=1)
#Importar a base de dados
import pandas as pd
df = pd.read_excel(r'C:\Users\Wallace\Downloads/Vendas - Dez.xlsx')
faturamento = df['Valor Final'].sum()
qtde_produtos = df['Quantidade'].sum()
#Abrir aba do Gmail
pyautogui.hotkey('ctrl', 't')
pyautogui.write("mail.google.com")
pyautogui.press('enter')
time.sleep(15)
pyautogui.click(95, 212, clicks=1)
time.sleep(30)
pyautogui.write('wallacecbatista@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
ass = 'Relatório de Vendas de Ontem'
pyperclip.copy(ass)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
texto = f"""
Prezados, Bom Dia
O Faturamento de ontem foi de: R${faturamento:,.2f}
A Quantidade de produtos foi de: {qtde_produtos:,}
abs
Wallace"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")