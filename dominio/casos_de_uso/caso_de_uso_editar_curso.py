from dominio.otds import OTDCurso
from dominio.repositorios import RepositorioAbstratoCurso


class CasoDeUsoEditarCurso:
    __repositorio_curso: RepositorioAbstratoCurso

    def __init__(self, repositorio_curso: RepositorioAbstratoCurso) -> None:
        self.__repositorio_curso = repositorio_curso

    def executar(self, otd_curso: OTDCurso) -> OTDCurso:
        curso = otd_curso.para_entidade()
        self.__repositorio_curso.trazer_por_id(curso.id)
        self.__repositorio_curso.salvar(curso)
        return otd_curso
