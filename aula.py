from abc import ABC, abstractmethod

class ConstrutorRelatorio(ABC):
    def __init__(self):
        self.relatorio = ""

    @abstractmethod
    def documento(self):
        pass

    def obter_relatorio(self):
        return self.relatorio

class RelatorioHtml(ConstrutorRelatorio):
    def __init__ (self):
        self.relatorio =""

    def documento(self):
        self.relatorio += "DocumentoHTML"

    def obter_relatorio(self):
        return self.relatorio

class  RelatorioCrystalReport(ConstrutorRelatorio):
    def __init__ (self):
        self.relatorio =""

    def documento(self):
        self.relatorio += "DocumentoCR"

    def obter_relatorio(self):
        return self.relatorio
    
class RelatorioPDF:
    def __init__ (self):
        self.relatorio =""

    def documento(self):
        self.relatorio += "DocumentoPDF"

    def obter_relatorio(self):
        return self.relatorio

class DiretorRelatorio:
    def __init__(self,construtor: ConstrutorRelatorio):
        self.construtor = construtor

    def construir_relatorio(self):
        self.construtor.documento()
        return self.construtor.obter_relatorio()
    
if __name__ == "__main__":
    formatos = {
        "HTML":RelatorioHtml(),
        "Crystal Report":RelatorioCrystalReport(),
        "PDF":RelatorioPDF()
    }
    
    for nome, construtor in formatos.items():
        diretor = DiretorRelatorio(construtor)
        relatorio = diretor.construir_relatorio()
        print(f"Relatorio {nome}, {relatorio}")