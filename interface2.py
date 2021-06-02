from tkinter.constants import BOTTOM, CENTER
from webbrowser import BackgroundBrowser
from PySimpleGUI import PySimpleGUI as sg
import backend

if backend.viabilidade['maremotriz']:
    maremotriz_img='maremotriz.png'
    maremotriz_bg='#355167'
    maremotriz_title_color='#DADA3E'
else:
    maremotriz_img='maremotrizbw.png'
    maremotriz_bg='#A9A9A9'
    maremotriz_title_color='#000000'

if backend.viabilidade['maremotriz']:
    maremotriz_img='maremotriz.png'
    maremotriz_bg='#355167'
    maremotriz_title_color='#DADA3E'
else:
    maremotriz_img='maremotrizbw.png'
    maremotriz_bg='#A9A9A9'
    maremotriz_title_color='#000000'


sg.theme('DarkBlue2')
layout=[
    [sg.Text('                       Abaixo, as fontes energéticas em destaque são viáveis para a sua propriedade:', font=('arial',16))],
     [sg.Frame(layout=[   
         [sg.Text('   ',background_color='#A9A9A9')],   
         [sg.Text('   ',background_color='#A9A9A9'),sg.Image('eolicabw.png'),sg.Text('   ',background_color='#A9A9A9')]
     ], title='Eólica\n',title_color='#000000', font=('arial',20),border_width=0, background_color='#A9A9A9', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20)), 
     sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('geotermica.png'),sg.Text('   ',background_color='#355167')]
     ], title='Geotérmica\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20)),
     sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('maremotriz.png'),sg.Text('   ',background_color='#355167')]
     ], title='Maremotriz\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20))],
     [sg.Text('                                        '), sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('fotovoltaica.png'),sg.Text('   ',background_color='#355167')]
     ], title='Fotovoltaica\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,0)), 
     sg.Frame(layout=[   
         [sg.Text('   ',background_color='#355167')],   
         [sg.Text('   ',background_color='#355167'),sg.Image('hidreletrica.png'),sg.Text('   ',background_color='#355167')]
     ], title='Hídrica\n',title_color='#DADA3E', font=('arial',20),border_width=0, background_color='#355167', title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,0))]
]

janela = sg.Window('Implantação de Fontes Energéticas', layout, size=(1050,680), location=(150,10)) #titulo do janela

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: # verifica se foi clicado no X superior a direita e caso for fecha a interface
        break
    if eventos == 'Enviar dados': #verifica se foi clicado o botao 'enviar dados' e pega os valores que foram inseridos 
        print(valores)
        break