from json import loads
from requests import get
from pandas import DataFrame
from utils import Utils


class GitHub_Api():
    def __init__(self, usuario):
        self.usuario = usuario

    def requisisao_api(self):
        with get(f'https://api.github.com/users/{self.usuario}/repos') as api:
            if api.status_code == 200:
                dados_api = loads(api.content)
                return dados_api
            else:
                return api.raise_for_status()

    def mostrar_tudo(self):
        dados_api = self.requisisao_api()
        dado = DataFrame(dados_api)['name']
        print(dado)


cont_tempo = Utils.contador_temporal()

cont_tempo.inicio()
repositorio = GitHub_Api('tupiribas')
repositorio.mostrar_tudo()
cont_tempo.fim()

print(f'Tempo: {cont_tempo.tempo_total():.2f}')
