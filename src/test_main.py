from main import validar_respostas, resolver_respostas


def test_validar_respostas():
    # Lista de respostas para ser injetada na função
    teste_respostas1 = [255, 255, 0, 255, 255]  # Deve Retornar "C"
    teste_respostas2 = [0, 128, 212, 255, 200]  # Deve retornar "A"
    teste_respostas3 = [10, 20, 65, 30, 41]  # Deve retornar "*"

    # Variável para teste
    resultado = validar_respostas(teste_respostas1)
    esperado = "C"
    assert resultado == esperado


def test_resolver_respostas(monkeypatch, captura_saida):
    entrada_valores = '255 0 255 255 255'
    esperado = "B\n"  # Saída esperada para a entrada acima

    def mock_input():
        return entrada_valores

    # Realiza a substituição da função input() para o mock_input().
    monkeypatch.setattr('builtins.input', mock_input)

    resolver_respostas(1)
    # Captura a saida padrão durante a execução da função resolver_respostas().
    resultado = captura_saida.readouterr()
    assert resultado.out == esperado


if __name__ == '__main__':
    import pytest

    pytest.main([__file__, '-s'])
