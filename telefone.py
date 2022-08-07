import re

class Telefone:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError('Numero incorreto!!')

    def __str__(self):
        return self.format()

    def valida_telefone(self, telefone):
        padrao = '([0-9]{2, 3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            raise ValueError('numero invalido!!')

    def format(self):
        padrao = '([0-9]{2, 3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.telefone)
        if resposta.group(1) != None:
            numero_formatado = f'+{resposta.group(1)}' \
                               f'({resposta.group(2)})' \
                               f'{resposta.group(3)}-' \
                               f'{resposta.group(4)}'
            return numero_formatado
        else:
            numero_formatado = f'({resposta.group(2)})' \
                               f'{resposta.group(3)}-' \
                               f'{resposta.group(4)}'
            return numero_formatado
