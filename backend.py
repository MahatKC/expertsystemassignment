#trabalho por Leonardo Vanzin, Mateus Karvat e Roberta Aparecida

#inicialmente, são importadas as bibliotecas necessárias
from experta import *
import interface

valores_convertidos = {
    'proximidadeMar': float(interface.valores['proximidadeMar']),
    'desnivel': float(interface.valores['desnivel']),
    'velocidadeVento': float(interface.valores['velocidadeVento']),
    'latitude': float(interface.valores['latitude']),
    'area': float(interface.valores['area']),
    'temperaturaInterna': float(interface.valores['temperaturaInterna'])
}

viabilidade = {
    'maremotriz': False,
    'eolica': False,
    'solar': False,
    'geotermica': False,
    'hidrica': False
}

#então, criaremos os fatos utilizado para as regras do SE
#no Experta, cada fato é um classe individual com parâmetros próprios
#criaremos um fato distinto para cada possível fonte energética de nosso problema
class Solar(Fact):
    # ao declarar uma variável, pode-se restringir seu tipo, seu valor, e definir se ela é
    # obrigatória ou não
    # aqui, temos um variável float obrigatória cujo valor em módulo deve ser menor que 90
    latitude = Field(lambda longitude:
                        isinstance(longitude, float) and abs(longitude)<=90, mandatory=True)

class Geotermica(Fact):
    # aqui, a declaração da variável não tem restrição de valores, logo sua declaração é mais simples
    # e não requer o uso e uma função lambda
    temperatura_subterranea = Field(float, mandatory=True) #em graus celsius

class Maremotriz(Fact):
    # para esta classe, a diferenca_mare só será relevante caso o usuário esteja próximo do mar
    # logo, este parâmetro não é obrigatório e a inserção de um fato que não o contenha na base
    # de conhecimento será aceita
    diferenca_mare = Field(lambda diferenca_mare:
                            isinstance(diferenca_mare, float) and diferenca_mare>=0) #em metros
    proximidade_mar = Field(float, mandatory=True) #em km

class Eolica(Fact):
    velocidade_vento = Field(lambda velocidade_vento: isinstance(velocidade_vento, float)
                                and velocidade_vento>=0, mandatory=True) #em km/h

class Hidrica(Fact):
    area_reservatorio = Field(lambda area_reservatorio:
                            isinstance(area_reservatorio, float) and area_reservatorio>=0, 
                            mandatory=True) #em km²

# o motor de inferência deve ser declarado como uma classe própria, dentro da qual serão definidas
# as regras
class AnaliseViabilidade(KnowledgeEngine):
    
    # cada regra usa um annotation @rule, dentro do qual os possíveis valores dos fatos são especificados
    # acessamos o fato desejado e determinamos uma função lambda para tal valor, indicando seus possíveis valores
    # quando uma regra acessa mais de um parâmetro, ela só será validada caso todas as restrições sejam atendidas
    # neste caso, a função regra_maremotriz só será executada caso o parâmetro diferenca_mare for maior ou igual a 7 e
    # o parametro promixidade_mar menor ou igual a 2. do contrário, nada ocorrerá
    @Rule(Maremotriz(diferenca_mare=P(lambda d: d>=7),proximidade_mar=P(lambda p: p<=2)))
    def regra_maremotriz(self):
        print("Maremotriz é top")
        viabilidade['maremotriz'] = True

    @Rule(Eolica(velocidade_vento=P(lambda v: v>25)))
    def regra_eolica(self):
        print("Eolica é top")
        viabilidade['eolica'] = True

    @Rule(Solar(latitude=P(lambda y: abs(y)<50)))
    def regra_solar(self):
        print("Solar é top")
        viabilidade['solar'] = True

    @Rule(Geotermica(temperatura_subterranea=P(lambda t: t>150)))
    def regra_geotermica(self):
        print("Geotermica é top")
        viabilidade['geotermica'] = True

    @Rule(Hidrica(area_reservatorio=P(lambda a: a>3.0)))
    def regra_hidrica(self):
        print("Hidrica é top")
        viabilidade['hidrica'] = True

# após declarar o motor, as regras e os fatos, é preciso instanciá-los
engine = AnaliseViabilidade()
# o motor é reinicializado para aceitar novos fatos (limpando quaisquer valores existentes na cache após uma execução anterior)
engine.reset()
# cada um dos fatos é declarado individualmente, podendo-se passar múltiplos parâmetros para um mesmo fato de uma vez só
engine.declare(Maremotriz(diferenca_mare=valores_convertidos['desnivel'],
                            proximidade_mar=valores_convertidos['proximidadeMar']))
engine.declare(Eolica(velocidade_vento=valores_convertidos['velocidadeVento']))
engine.declare(Solar(latitude=valores_convertidos['latitude']))
engine.declare(Hidrica(area_reservatorio=valores_convertidos['area']))
engine.declare(Geotermica(temperatura_subterranea=valores_convertidos['temperaturaInterna']))
# por fim, o motor é executado
engine.run()

print(viabilidade)