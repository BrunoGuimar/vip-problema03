import main

# def resolver_respostas(qtd_linhas):
#     for _ in range(int(qtd_linhas)):
#         linhas = input().split()
#         linhas = list(map(int, linhas))
#         print(validar_respostas(linhas))
#     return

# def validar_respostas(respostas):
#     indice_alternativa = [indice for indice, valor in enumerate(respostas) if valor <= 127]
#     if len(indice_alternativa) == 1:
#         return chr(indice_alternativa[0] + ord('A'))
#     else:
#         return "*"

def test_validar_respostas():
    respostas_caso1 = [0, 255, 255, 255, 255]
    respostas_caso2 = ""
    respostas_caso3 = "241 217 255 4 128"

    resultado = main.validar_respostas(respostas_caso1)
    esperado = "A"

    assert resultado == esperado