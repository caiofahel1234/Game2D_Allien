from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod 
    def calcular(self, valor):
        pass

class DescontoNormal(Desconto):
    def calcular (self, valor):
        return valor * 0.1

class DescontoVip(Desconto):
    def calcular (self, valor):
        return valor * 0.2

class DescontoPremium(Desconto):
    def calcular (self, valor):
        return valor * 0.3

class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError
class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError
    
class IVip:
    def validar_usuario_vip(self, usuario):
        raise NotImplementedError

class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto
    def total(self,valor):
        return valor - self.desconto.calcular(valor)


def aplicar_desconto(desconto: Desconto, valor: float) -> float:
    return desconto.calcular(valor)

def aplicar_cupom(desconto: Desconto, codigo: str) -> str:
    return "Cupom: " + codigo + " Aplicado"



if __name__ == "__main__":
    valor = 100

    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVip())

    print("Normal: ", pedido_normal.total(valor))
    print("VIP: ", pedido_vip.total(valor) )