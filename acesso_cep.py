import requests


class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError('CEP invalido!!')

    def __str__(self):
        return self.format()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessa_via_cep(cep):
        url = 'https://viacep.com.br/ws/{}/json'.format(cep)
        r = requests.get(url)
        dados = r.json()
        bairro = dados.get('bairro')
        cidade = dados.get('localidade')
        uf = dados.get('uf')
        return bairro, cidade, uf
