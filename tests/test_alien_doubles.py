# tests/test_alien_doubles.py

# 1. Exemplo de STUB para Configurações do Jogo
class StubSettings:
    """Stub que simula as configurações sem precisar carregar arquivos reais."""
    def __init__(self):
        self.ship_speed = 5.0
        self.screen_width = 1200
        self.screen_height = 800

def test_nave_com_stub_settings():
    settings = StubSettings()
    assert settings.ship_speed == 5.0
    assert settings.screen_width == 1200


# 2. Exemplo de MOCK para simular Interação (ex: som, renderizador ou tela)
def test_atualizacao_com_mock_screen(mocker):
    # Criamos um mock para simular a tela do Pygame/Game
    mock_screen = mocker.Mock()
    
    # Simulamos uma chamada de renderização
    mock_screen.fill((230, 230, 230))
    
    # Verificamos se o método fill foi chamado com a cor esperada
    mock_screen.fill.assert_called_once_with((230, 230, 230))