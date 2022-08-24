from django.test import TestCase

from aplicacao.models import ModeloDocente
from aplicacao.repositorios import RepositorioDocente
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_docente import FabricaTesteModeloDocente
from testes.fabricas.dominio.entidades import FabricaTesteDocente


class TestRepositorioDocente(TestCase):
    def setUp(self) -> None:
        self.repositorio_docente = RepositorioDocente()

    def test_trazer_QUANDO_modelos_existem_ENTAO_traz_docentes(self) -> None:
        quantidade = 2
        [FabricaTesteModeloDocente.create() for _ in range(quantidade)]

        docentes = self.repositorio_docente.trazer()

        self.assertEqual(len(docentes), quantidade)

    def test_salvar_QUANDO_docente_informado_ENTAO_salva_docente(self) -> None:
        docente = FabricaTesteDocente.build()

        self.repositorio_docente.salvar(docente)

        ModeloDocente.objects.get(pk=docente.id.valor)
