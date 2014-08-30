# -*- encoding: utf-8 -*-

class Elementos():
    def __init__(self):
        self.series = {0: u'Não metal',
                       1: u'Gas nobre',
                       2: u'Metal alcalino',
                       3: u'Metal alcalinoterroso',
                       4: u'Semi metal',
                       5: u'Halogênio',
                       6: u'Metal representativo',
                       7: u'Metal de transição',
                       8: u'Lantanídio',
                       9: u'Actinídeo'}
        self.classes_magneticas = {0: u'Ferromagnético',
                                   1: u'Antiferromagnético',
                                   2: u'Paramagnético',
                                   3: u'Diamagnético',
                                   4: u'Ferrimagnético'}
        elementos = [{'numero': 1,
                      'massa': 1.00794,
                      'nome': u"Hidrogênio",
                      'simbolo': 'H',
                      'serie': 0,  # Não metal
                      'densidade': 0.0899,  #kg/m3
                      'dureza': 0.0,  # escala Mohs
                      'fusao': 14.025,  # kelvin
                      'ebulicao': 20.268,  # kelvin
                      'h_fusao': 0.05868,  # kJ/mol
                      'h_ebulicao': 0.44936,  # kJ/mol
                      'volume_molar': 11.42 * 10 ** -6,  # m3/mol
                      'pressao_vapor': 209.0,  # Pa a 23K
                      'velocidade_do_som': 1270.0,  # m/s a 20 C
                      'classe_magnetica': 3,  # Diamagnetica
                      'susceptibilidade_magnetica': -2.2 * 10 ** -9,
                      'eletronegatividade': 2.2,  # escala pauling
                      'calor_especifico': 14304.0,  # J/kg.K
                      'condutividade_eletrica': 10 ** 6,  # S/m
                      'condutividade_termica': 0.1815},  # W/m.K

                     {'numero': 2,
                      'massa': 4.002602,
                      'nome': u"Hélio",
                      'simbolo': 'He',
                      'serie': 1,  # Gas nobre
                      'densidade': 0.1785,  #kg/m3
                      'dureza': 0.0,  # escala Mohs
                      'fusao': 0.95,  # kelvin
                      'ebulicao': 4.22,  # kelvin
                      'h_fusao': 5.23,  # kJ/mol
                      'h_ebulicao': 0.0845,  # kJ/mol
                      'volume_molar': 21.0 * 10 ** -6,  # m3/mol
                      'pressao_vapor': 100.0,  # Pa a 1,23K
                      'velocidade_do_som': 972.0,  # m/s a 20 C
                      'classe_magnetica': 3,  # Diamagnetica
                      'susceptibilidade_magnetica': None,  # PERSQUISAR ESTE VALOR
                      'eletronegatividade': None,  # PERSQUISAR ESTE VALOR
                      'calor_especifico': 5193.0,  # J/kg.K
                      'condutividade_eletrica': None,  # PERSQUISAR ESTE VALOR
                      'condutividade_termica': 0.152},  # W/m.K

                     {'numero': 3,
                      'massa': 6.941,
                      'nome': u"Lítio",
                      'simbolo': 'Li',
                      'serie': 2,  # Metal alcalino
                      'densidade': 535,  #kg/m3
                      'dureza': 0.6,  # escala Mohs
                      'fusao': 453.0,  # kelvin
                      'ebulicao': 1615.0,  # kelvin
                      'h_fusao': 3.0,  # kJ/mol
                      'h_ebulicao': 145.92,  # kJ/mol
                      'volume_molar': 13.02 * 10 ** -6,  # m3/mol
                      'pressao_vapor': 1.63,  # Pa a 1,23K
                      'velocidade_do_som': 6000.0,  # m/s a 20 C
                      'classe_magnetica': 2,  # Paramagnetico
                      'susceptibilidade_magnetica': None,  # PERSQUISAR ESTE VALOR
                      'eletronegatividade': 0.98,  # escala Pauling
                      'calor_especifico': 3582.0,  # J/kg.K
                      'condutividade_eletrica': 10.8 * 10 ** 6,  # S/m
                      'condutividade_termica': 84.7},  # W/m.K

                     # {'numero': 1,
                     #  'massa': 1.00794,
                     #  'nome': u"Hidrogênio",
                     #  'simbolo': 'H',
                     #  'serie': 0,
                     #  'densidade': 0.0899,  #kg/m3
                     #  'dureza': 0.0,  # escala Mohs
                     #  'fusao': 14.025,  # kelvin
                     #  'ebulicao': 20.268,  # kelvin
                     #  'h_fusao': 0.05868,  # kJ/mol
                     #  'h_ebulicao': 0.44936,  # kJ/mol
                     #  'volume_molar': 11.42 * 10 ** -6,  # m3/mol
                     #  'pressao_vapor': 209.0,  # Pa a 23K
                     #  'velocidade_do_som': 1270.0,  # m/s a 20 C
                     #  'classe_magnetica': 3,
                     #  'susceptibilidade_magnetica': -2.2 * 10 ** -9,
                     #  'eletronegatividade': 2.2,  # escala pauling
                     #  'calor_especifico': 14304.0,  # J/kg.K
                     #  'condutividade_eletrica': 10 ** 6,  # S/m
                     #  'condutividade_termica': 0.1815},  # W/m.K
                    ]
        self.list = elementos

    def as_dict(self, propriedade='numero'):
        d = {}
        for i in self.list:
            d[i[propriedade]] = i
        return d
