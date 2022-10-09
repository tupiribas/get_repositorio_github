import requests


class GitHub_Api():
    def __init__(self, usuario):
        self.usuario = usuario

    def requisisao_api(self):
        resp = requests.get(
            f'https://api.github.com/users/{self.usuario}/repos')

        if resp.status_code == 200:
            return resp.json()
        else:
            return 'Não foi possível acessar este repositório.'

    def mostrar_tudo(self):
        dados_api = self.requisisao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)


repositorio = GitHub_Api('tupiribas')
print(repositorio.requisisao_api())
