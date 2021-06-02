from tkinter.constants import BOTTOM, CENTER
from webbrowser import BackgroundBrowser
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkBlue2')
layout=[
    [sg.Text('   As seguintes fontes energéticas são viáveis para a sua propriedade:', font=('arial',16))],
     [sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('eolica.png'),sg.Text('   ',background_color='#355167')]
     ], title='Eólica\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20)), 
     sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('geotermica.png'),sg.Text('   ',background_color='#355167')]
     ], title='Geotérmica\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20))],
     [sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('fotovoltaica.png'),sg.Text('   ',background_color='#355167')]
     ], title='Fotovoltaica\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,10)), 
     sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('hidreletrica.png'),sg.Text('   ',background_color='#355167')]
     ], title='Hídrica\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,10))],
     [sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('maremotriz.png'),sg.Text('   ',background_color='#355167')]
     ], title='Maremotriz\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(181,10))]


]

janela = sg.Window('Implantação de Fontes Energéticas', layout) #titulo do janela

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: # verifica se foi clicado no X superior a direita e caso for fecha a interface
        break
    if eventos == 'Enviar dados': #verifica se foi clicado o botao 'enviar dados' e pega os valores que foram inseridos 
        print(valores)
        break