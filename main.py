from random import choice
import schema
from experta import *

class Solar(Fact):
    latitude = Field(lambda longitude:
                        isinstance(longitude, float) and abs(longitude)<=90, mandatory=True)

class Geotermica(Fact):
    temperatura_subtarranea = Field(float, mandatory=True)

class Maremotriz(Fact):
    diferenca_mare = Field(lambda diferenca_mare:
                            isinstance(diferenca_mare, float) and diferenca_mare>=0) #valor em metros
    proximidade_mar = Field(float, mandatory=True) #valor em quilometros

class Eolica(Fact):
    velocidade_vento = Field(lambda velocidade_vento: isinstance(velocidade_vento, float)
                                and velocidade_vento>=0, mandatory=True)

class Hidrica(Fact):
    parametro1 = Field(int, mandatory=True)

class AnaliseViabilidade(KnowledgeEngine):
    @Rule(Maremotriz(diferenca_mare=P(lambda d: d>=7),proximidade_mar=P(lambda p: p<=2)))
    def regra_maremotriz(self):
        print("Maremotriz é top")

    @Rule(Eolica(velocidade_vento=P(lambda v: v>25)))
    def regra_eolica(self):
        print("Eolica é top")

    @Rule(Solar(altitude=P(lambda h: h<4000), latitude=P(lambda y: abs(y)<45)))
    def regra_solar(self):
        print("Solar é top")

engine = AnaliseViabilidade()
engine.reset()
engine.declare(Maremotriz(diferenca_mare=8.0,proximidade_mar=0.08))
engine.declare(Eolica(velocidade_vento=30.0))
engine.declare(Solar(altitude=1000, latitude=-10.0))
engine.run()