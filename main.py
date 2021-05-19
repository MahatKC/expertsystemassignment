from random import choice
import schema
from experta import *

"""
class Light(Fact):
    #Info about the traffic light.
    pass
"""

class Demanda(Fact):
    kwh_demand = Field(lambda kwh_demand: isinstance(kwh_demand, int) and kwh_demand>=0, mandatory=True)

class Classe_Consumo(Fact):
    #0 -> residencial
    #1 -> rural
    #2 -> industrial
    classe_consumo = Field(lambda classe_consumo: 
                        isinstance(classe_consumo, int) and classe_consumo in (0,1,2), mandatory=True)

class Radiacao(Fact):
    radiacao = Field(int, mandatory=True)

class Longitude(Fact):
    longitude = Field(lambda longitude:
                        isinstance(longitude, float) and longitude>=-90 and longitude<=90, mandatory=True)

class Altitude(Fact):
    altitude = Field(lambda altitude:
                        isinstance(altitude, int) and altitude>=-500 and altitude<=9000, mandatory=True)

class Area_Disponivel(Fact):
    area = Field(lambda area: isinstance(area, int) and area>=0, mandatory=True)

class Disponbilidade_Hidrica(Fact):
    disponibilidade = Field(int, mandatory=True)

class Temperatura_Subterranea(Fact):
    temperatura = Field(float, mandatory=True)

class Fontes_Quentes(Fact):
    fontes_quentes = Field(bool, mandatory=True)
"""
class RobotCrossStreet(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
        print("Walk")

    @Rule(Light(color='red'))
    def red_light(self):
        print("BAum")

    @Rule(AS.light << Light(color=L('yellow') | L('blinking-yellow')))
    def cautious(self, light):
        print("Be cautious because light is", light["color"])
"""
"""
engine = RobotCrossStreet()
engine.reset()
engine.declare(Light(color=choice(['red'])))
engine.run()
"""