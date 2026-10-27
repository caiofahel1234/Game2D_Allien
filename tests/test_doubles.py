# tests/test_doubles.py
from tests.doubles import StubSemDesconto
from src.desconto import Pedido


def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100.0



def test_pedido_com_mock_desconto(mocker):
   
    mock_desconto = mocker.Mock()
    

    mock_desconto.calcular.return_value = 10
    
    # 3. Injetar no Pedido
    pedido = Pedido(mock_desconto)
    resultado = pedido.total(100)
    

    assert resultado == 90
    mock_desconto.calcular.assert_called()
    mock_desconto.calcular.assert_called_once_with(100)
    assert mock_desconto.calcular.call_count == 1