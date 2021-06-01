from tkinter.constants import CENTER
from PySimpleGUI import PySimpleGUI as sg

ajudaLatitude = 'Este atributo pode ser obtido via Google Maps, \nclicando com o botão direito na coordenada.\nO primeiro valor apresentado refere-se à latitude!' #mensagem que aparece no botao de interrogacao
sg.theme('DarkBlue2')
layout = [   #definicao da aparencia da interface junto com o conteudo que sera exibido
    [sg.Text('Proximidade com o mar (Km)           '), sg.Input(key='proximidadeMar', text_color='#DADA3E', size=(15, None))],
    [sg.Text('Diferença entre maré alta e baixa (m)'), sg.Input(key='desnivel', text_color='#DADA3E', size=(15, None))],
    [sg.Text('Velocidade do vento (Km/h)              '), sg.Input(key='velocidadeVento', text_color='#DADA3E', size=(15, None))],
    [sg.Text('Latitude (notação decimal)'), 
    sg.Image('help-circle.png', tooltip=ajudaLatitude), # botao de interrogacao que aparece uma mensagem ao deixar o mouse em cima
    sg.Input(key='latitude', text_color='#DADA3E', size=(15, None))],
    [sg.Text('Área para reservatório (m2)              '), sg.Input(key='area', text_color='#DADA3E', size=(15, None))],
    [sg.Text('Temperatura no interior da terra (°C) '), sg.Input(key='temperaturaInterna', text_color='#DADA3E', size=(15, None))],
    [sg.Button('Enviar dados', pad=(100, 0), button_color='#DADA3E', size=(18, None))]
]


janela = sg.Window('Implantação de fontes energéticas', layout) #titulo do janela

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: # verifica se foi clicado no X superior a direita e caso for fecha a interface
        break
    if eventos == 'Enviar dados': #verifica se foi clicado o botao 'enviar dados' e pega os valores que foram inseridos 
        print(valores)
        break