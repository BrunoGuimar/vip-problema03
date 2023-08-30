alternativas = ["A", "B", "C", "D", "E"]


def checar_resposta(resposta):
    qtd_preto = 0
    resultado_aluno = ""
    for i, numero in enumerate(resposta):
        if numero <= 127:
            qtd_preto += 1
            resultado_aluno = alternativas[i]
        if qtd_preto > 1:
            resultado_aluno = "*"
            return resultado_aluno
    return resultado_aluno


def procurar_resposta(qtd_linhas):
    for _ in range(int(qtd_linhas)):
        linhas = input().split()
        linhas = list(map(int, linhas))
        print(checar_resposta(linhas))
    return


while True:
    qtd_linhas = input()
    if int(qtd_linhas) == 0:
        break
    procurar_resposta(qtd_linhas)




