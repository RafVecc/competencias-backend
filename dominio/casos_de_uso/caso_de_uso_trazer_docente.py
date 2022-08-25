from uuid import UUID

from dominio.objetos_de_valor import IdDeDocente
from dominio.otds import OTDDocente
from dominio.repositorios import RepositorioAbstratoDocente


class CasoDeUsoTrazerDocente:
    __repositorio_docente: RepositorioAbstratoDocente

    def __init__(self, repositorio_docente: RepositorioAbstratoDocente) -> None:
        self.__repositorio_docente = repositorio_docente

    def executar(self, id_: UUID) -> OTDDocente:
        id_de_docente = IdDeDocente(id_)
        docente = self.__repositorio_docente.trazer_por_id(id_de_docente)
        return OTDDocente.de_entidade(docente)
