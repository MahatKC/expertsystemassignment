from tkinter.constants import BOTTOM, CENTER
from webbrowser import BackgroundBrowser
from PySimpleGUI import PySimpleGUI as sg
import backend
# nos if e else abaixo é verificado com o resultado quais fontes sao viaveis, quando a fonte é viavel a foto aparecerá colorida, mas se nao for a foto aparecerá em preto e branco
if backend.viabilidade['maremotriz']:
    maremotriz_img='maremotriz.png'
    maremotriz_bg='#355167'
    maremotriz_title_color='#DADA3E'
else:
    maremotriz_img='maremotrizbw.png'
    maremotriz_bg='#A9A9A9'
    maremotriz_title_color='#000000'

if backend.viabilidade['eolica']:
    eolica_img='eolica.png'
    eolica_bg='#355167'
    eolica_title_color='#DADA3E'
else:
    eolica_img='eolicabw.png'
    eolica_bg='#A9A9A9'
    eolica_title_color='#000000'
# A energia fotovoltaica sempre é viavel
fotovoltaica_img='fotovoltaica.png'
fotovoltaica_bg='#355167'
fotovoltaica_title_color='#DADA3E'
popupSolar = False # porem pode ocorrer de ela nao ter rentabilidade otima, neste caso é exibido uma mensagem ao usuario
if not backend.viabilidade['solar']:
    popupSolar = True

if backend.viabilidade['geotermica']:
    geotermica_img='geotermica.png'
    geotermica_bg='#355167'
    geotermica_title_color='#DADA3E'
else:
    geotermica_img='geotermicabw.png'
    geotermica_bg='#A9A9A9'
    geotermica_title_color='#000000'

if backend.viabilidade['hidrica']:
    hidreletrica_img='hidreletrica.png'
    hidreletrica_bg='#355167'
    hidreletrica_title_color='#DADA3E'
else:
    hidreletrica_img='hidreletricabw.png'
    hidreletrica_bg='#A9A9A9'
    hidreletrica_title_color='#000000'

popText = 'Na presente condição, fontes fotovoltaicas não apresentam\nrentabilidade ótima, mas ainda são viáveis' # texto utilizado na mensagem warning
sg.theme('DarkBlue2')
layout=[ # layout exibido quando a energia fotovoltaica nao tem rentabilidade otima
    [sg.Text('                       Abaixo, as fontes energéticas em destaque são viáveis para a sua propriedade:', font=('arial',16))], 
     [sg.Frame(layout=[   #imagem e nome da fonte energetica
         [sg.Text('   ',background_color=eolica_bg)],   #pega as informações do if e else que serao exibidas
         [sg.Text('   ',background_color=eolica_bg),sg.Image(eolica_img),sg.Text('   ',background_color=eolica_bg)]
     ], title='Eólica\n',title_color=eolica_title_color, font=('arial',20),border_width=0, background_color=eolica_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20)), 
     sg.Frame(layout=[   #imagem e nome da fonte energetica
         [sg.Text('   ',background_color=geotermica_bg)],   
         [sg.Text('   ',background_color=geotermica_bg),sg.Image(geotermica_img),sg.Text('   ',background_color=geotermica_bg)]
     ], title='Geotérmica\n',title_color=geotermica_title_color, font=('arial',20),border_width=0, background_color=geotermica_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20)),
     sg.Frame(layout=[   #imagem e nome da fonte energetica
         [sg.Text('   ',background_color=maremotriz_bg)],   
         [sg.Text('   ',background_color=maremotriz_bg),sg.Image(maremotriz_img),sg.Text('   ',background_color=maremotriz_bg)]
     ], title='Maremotriz\n',title_color=maremotriz_title_color, font=('arial',20),border_width=0, background_color=maremotriz_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20))],
     [sg.Text('                                        '), sg.Frame(layout=[   #imagem e nome da fonte energetica / espaços em branco para alocar melhor a imgem na tela
         [sg.Text('                                                                    ',background_color=fotovoltaica_bg),  sg.Image('warning.png', tooltip=popText, background_color=fotovoltaica_bg)], # mensagem de aviso
         [sg.Text('   ',background_color=fotovoltaica_bg),sg.Image(fotovoltaica_img),sg.Text('   ',background_color=fotovoltaica_bg)]
     ], title='Fotovoltaica\n',title_color=fotovoltaica_title_color, font=('arial',20),border_width=0, background_color=fotovoltaica_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,0)), 
     sg.Frame(layout=[   #imagem e nome da fonte energetica
         [sg.Text('   ',background_color=hidreletrica_bg)],   
         [sg.Text('   ',background_color=hidreletrica_bg),sg.Image(hidreletrica_img),sg.Text('   ',background_color=hidreletrica_bg)]
     ], title='Hídrica\n',title_color=hidreletrica_title_color, font=('arial',20),border_width=0, background_color=hidreletrica_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,0))]
]

layout2=[ # layout exibido quando a energia fotovoltaica possui rentabilidade otima
    [sg.Text('                       Abaixo, as fontes energéticas em destaque são viáveis para a sua propriedade:', font=('arial',16))], 
     [sg.Frame(layout=[   #imagem e nome da fonte energetica
         [sg.Text('   ',background_color=eolica_bg)],   #pega as informações do if e else que serao exibidas
         [sg.Text('   ',background_color=eolica_bg),sg.Image(eolica_img),sg.Text('   ',background_color=eolica_bg)]
     ], title='Eólica\n',title_color=eolica_title_color, font=('arial',20),border_width=0, background_color=eolica_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20)), 
     sg.Frame(layout=[   #imagem e nome da fonte energetica
         [sg.Text('   ',background_color=geotermica_bg)],   
         [sg.Text('   ',background_color=geotermica_bg),sg.Image(geotermica_img),sg.Text('   ',background_color=geotermica_bg)]
     ], title='Geotérmica\n',title_color=geotermica_title_color, font=('arial',20),border_width=0, background_color=geotermica_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20)),
     sg.Frame(layout=[   #imagem e nome da fonte energetica
         [sg.Text('   ',background_color=maremotriz_bg)],   
         [sg.Text('   ',background_color=maremotriz_bg),sg.Image(maremotriz_img),sg.Text('   ',background_color=maremotriz_bg)]
     ], title='Maremotriz\n',title_color=maremotriz_title_color, font=('arial',20),border_width=0, background_color=maremotriz_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,20))],
     [sg.Text('                                        '), sg.Frame(layout=[   #imagem e nome da fonte energetica / espaços em branco para alocar melhor a imgem na tela
         [sg.Text('                                                                    ',background_color=fotovoltaica_bg)],
         [sg.Text('   ',background_color=fotovoltaica_bg),sg.Image(fotovoltaica_img),sg.Text('   ',background_color=fotovoltaica_bg)]
     ], title='Fotovoltaica\n',title_color=fotovoltaica_title_color, font=('arial',20),border_width=0, background_color=fotovoltaica_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,0)), 
     sg.Frame(layout=[   #imagem e nome da fonte energetica
         [sg.Text('   ',background_color=hidreletrica_bg)],   
         [sg.Text('   ',background_color=hidreletrica_bg),sg.Image(hidreletrica_img),sg.Text('   ',background_color=hidreletrica_bg)]
     ], title='Hídrica\n',title_color=hidreletrica_title_color, font=('arial',20),border_width=0, background_color=hidreletrica_bg, title_location=sg.TITLE_LOCATION_BOTTOM, pad=(10,0))]
]

if popupSolar: # seleciona qual layout sera exibido
    janela = sg.Window('Implantação de Fontes Energéticas', layout, size=(1050,680), location=(150,10)) #titulo do janela
else:
    janela = sg.Window('Implantação de Fontes Energéticas', layout2, size=(1050,680), location=(150,10)) #titulo do janela

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED: # verifica se foi clicado no X superior a direita e caso for fecha a interface
        break
    
