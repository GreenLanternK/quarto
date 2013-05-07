"""
############################################################
Quarto - Tabuleiro
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/02
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from casa import Casa
class Tabuleiro:
    """Campo do jogo onde se joga as pecas"""
    def __init__(self, gui, local):
        self.local = local
        self.casas = []
        self.build(gui)
    def build(self, gui):
        " Constroi uma colecao de dezesseis casas"
        self.casas = [Casa(gui, self, i).build() for i in range(16)]
    @property
    def casa(self):
        "retorna a casa da base"
        return self.local.casa
