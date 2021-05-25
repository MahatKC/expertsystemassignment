from tkinter.constants import CENTER
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkBlue2')
layout = [
    [sg.Text('Demanda em KW do local'), sg.Input(key='kw', text_color='#DADA3E', size=(19, 1)),
    sg.Text('Proximidade com o mar (Km) '), sg.Input(key='proximidadeMar', text_color='#DADA3E', size=(10, 1))],
    [sg.Text('Diferença entre maré alta e baixa (m)'), sg.Input(key='desnivel', text_color='#DADA3E', size=(10, 1)),
    sg.Text('Velocidade do vento (Km/h)'), sg.Input(key='velocidadeVento', text_color='#DADA3E', size=(12, 1))],
    [sg.Text('Latitude '), sg.Input(key='latitude', text_color='#DADA3E', size=(11, 1)),
    sg.Text('Altitude  '), sg.Input(key='altitude', text_color='#DADA3E', size=(11, 1)),
    sg.Text('Área disponível (m2)'), sg.Input(key='area', text_color='#DADA3E', size=(18, 1))],
    [sg.Text('Disponibilidade hídrica'), sg.Input(key='dispHidrica', text_color='#DADA3E')],
    [sg.Text('Temperatura no interior da terra (°C'), sg.Input(key='temperaturaInterna', text_color='#DADA3E')],
    [sg.Button('   Enviar dados   ', button_color='#DADA3E')]
]

janela = sg.Window('Implantação de fontes energéticas', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enviar dados':
        print(valores)