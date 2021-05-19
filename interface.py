from tkinter.constants import CENTER
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkBlue2')
layout = [
    [sg.Text('Demanda em KW do local'), sg.Input(key='kw', text_color='#DADA3E')],
    [sg.Text('Classe de Consumo')],
    [sg.Radio('Residencial', "RADIO1", default=True), sg.Radio('Rural', "RADIO1", default=False), 
        sg.Radio('Industrial', "RADIO1", default=False)],
    [sg.Text('Radiação'), sg.Input(key='radiacao', text_color='#DADA3E')],
    [sg.Text('Proximidade com o mar (m)'), sg.Input(key='proximidadeMar', text_color='#DADA3E')],
    [sg.Text('Longitude'), sg.Input(key='longitude', text_color='#DADA3E')],
    [sg.Text('Altitude'), sg.Input(key='altitude', text_color='#DADA3E')],
    [sg.Text('Área disponível (m2)'), sg.Input(key='area', text_color='#DADA3E')],
    [sg.Text('Disponibilidade hídrica'), sg.Input(key='dispHidrica', text_color='#DADA3E')],
    [sg.Text('Temperatura no interior da terra'), sg.Input(key='temperaturaInterna', text_color='#DADA3E')],
    [sg.Text('Há fontes de minas e lagos de água quente?')],
    [sg.Radio('Sim', "RADIO2", default=True), sg.Radio('Não', "RADIO2", default=False)],
    [sg.Button('Enviar dados', button_color='#DADA3E')]
]

janela = sg.Window('Implantação de fontes energéticas', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enviar dados':
        radiacao = (valores['radiacao'])
        print(valores)