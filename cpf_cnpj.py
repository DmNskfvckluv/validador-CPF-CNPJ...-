from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def criar_documento(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(documento)
        elif len(doc_str) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('documento invalido!!')


class DocCpf:
    def __init__(self, documento):
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF invalido!!')

    def __str__(self):
        return self.format()

    def valida_cpf(self, documento):
        validador_cpf = CPF()
        return validador_cpf.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ invalido!!')

    def __str__(self):
        return self.format()

    def valida_cnpj(self, documento):
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
