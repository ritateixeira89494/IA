# Estafetas
# São caraterizados por um ID, um nome, e um posto de distribuição, cidade.
# A cidade é uma ‘string’, e é o segundo parâmetro de um Local
class Estafeta:
    def __init__(self, estafeta_id: int, nome: object, cidade: object):
        """
        Construtor do estafeta.
        @param estafeta_id: Id único que identifica o estafeta nas atribuições.
        @param nome: Nome do estafeta (string).
        @param cidade: Cidade do estafeta. Usada para calcular o ponto de partida das entregas (string).
        """
        self.estafeta_id = estafeta_id
        self.nome = nome
        self.cidade = cidade
