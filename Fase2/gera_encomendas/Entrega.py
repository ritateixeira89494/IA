from algoritmos_procura.common import print_caminho
from base_conhecimento.Local import Local
from base_conhecimento.baseConhecimento import Transporte


# Entrega
# Regista as seguintes informações:
# ‘Id’ da encomenda, ‘id’ do estafeta, data da entrega, meio utilizado, caminho usado


#

class Entrega:
    def __init__(self, encomenda_id: int, estafeta_id: int, data_entrega: object, transporte: Transporte,
                 caminho: [Local]):
        """
        Construtor duma entrega. É chamado ao mesmo tempo que os circuitos são gerados, para saber quais os caminhos de entrega.
        @param encomenda_id: Id da encomenda
        @param estafeta_id: Id do estafeta que entregou.
        @param data_entrega: 
        @param transporte: Veículo utilizado durante a entrega.
        @param caminho: Caminho utilizado durante para a entrega.
        """
        self.encomenda_id = encomenda_id
        self.estafeta_id = estafeta_id
        self.data_entrega = data_entrega
        self.transporte = transporte
        self.caminho = caminho

    def imprime_entrega(self):
        """
        Função utilizada para imprimir uma entrega de forma organizada.
        """
        print("Id da encomenda: ", self.encomenda_id)
        print("Id da estafeta: ", self.estafeta_id)
        print("Data entrega: ", self.data_entrega)
        print("Transporte: ", self.transporte.nome)
        print_caminho(self.caminho)
