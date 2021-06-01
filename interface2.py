from tkinter.constants import BOTTOM
from webbrowser import BackgroundBrowser
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkBlue2')
layout=[
     [sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('eolica.png'),sg.Text('   ',background_color='#355167')]
     ], title='Eólica\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM), sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('eolica.png'),sg.Text('   ',background_color='#355167')]
     ], title='Eólica\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM)]


]

janela = sg.Window('Implantação de Fontes Energéticas', layout) #titulo do janela

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: # verifica se foi clicado no X superior a direita e caso for fecha a interface
        break
    if eventos == 'Enviar dados': #verifica se foi clicado o botao 'enviar dados' e pega os valores que foram inseridos 
        print(valores)
        break