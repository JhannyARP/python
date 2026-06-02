# ARQUIVO: test_notas.py
import unittest


# Este bloco contém as funções principais que serão testadas. Elas foram trazidas
# diretamente para este arquivo para garantir independência total de execução.

def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.

    Args:
    notas (list): Uma lista contendo as notas dos estudantes (floats ou ints).

    Returns:
    float: O valor da média resultante ou 0.0 se a lista estiver vazia.
    """
    tamanho_lista_de_notas = len(notas)

    if tamanho_lista_de_notas == 0:
        return 0.0

    soma_notas = 0
    for nota in notas:
        soma_notas += nota

    calculo_da_media = soma_notas / tamanho_lista_de_notas
    return calculo_da_media


def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica se a média obtida atinge o critério mínimo de aprovação institucional.

    Args:
    media (float): A média final obtida pelo estudante.
    media_minima (float, opcional): A nota de corte para aprovação. O padrão é 7.0.

    Returns:
    str: 'Aprovado' se a média for maior ou igual à mínima, caso contrário 'Reprovado'.
    """
    if media >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"


# Classe que herda de unittest.TestCase para estruturar a execução dos testes.
# Cada método interno representa um cenário específico exigido pelo enunciado.

class TestNucleoAcademico(unittest.TestCase):
    """
    Suíte de testes automatizados para validação e estresse do núcleo acadêmico.
    """

    def test_condicao_normal_aprovacao(self):
        """Valida o cenário padrão de sucesso para um estudante aprovado."""
        notas_aprovado = [8.0, 7.0, 9.0]
        media = calcular_media(notas_aprovado)
        self.assertEqual(media, 8.0)
        self.assertEqual(verificar_aprovacao(media), "Aprovado")

    def test_condicao_normal_reprovacao(self):
        """Valida o cenário padrão de falha para um estudante reprovado."""
        notas_reprovado = [5.0, 4.0, 6.0]
        media = calcular_media(notas_reprovado)
        self.assertEqual(media, 5.0)
        self.assertEqual(verificar_aprovacao(media), "Reprovado")

    def test_caso_extremo_lista_vazia(self):
        """Valida a resiliência do sistema diante de dados ausentes (lista vazia)."""
        notas_vazias = []
        media = calcular_media(notas_vazias)
        self.assertEqual(media, 0.0)
        self.assertEqual(verificar_aprovacao(media), "Reprovado")

    def test_acionamento_limitador_corte_zero(self):
        """Testa os limites paramétricos com a média mínima no valor absoluto 0."""
        media_baixa = 0.5
        status_corte_zero = verificar_aprovacao(media_baixa, media_minima=0.0)
        self.assertEqual(status_corte_zero, "Aprovado")

# Garante que o framework unittest processe e exiba os resultados no terminal
# apenas se este arquivo for executado diretamente.

if __name__ == '__main__':
    unittest.main()