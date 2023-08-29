n = input()
matriz = []
qtd_preto = 0
alternativas = ["A", "B", "C", "D", "E"]

for i in range(int(n)):
    linhas = input().split()
    linhas = list(map(int, linhas))
    matriz.append(linhas)

while qtd_preto < 1 and int(n) > 0:
    for linhas in matriz:
        qtd_preto = 0
        for i, numero in enumerate(linhas):
            if numero <= 127:
                qtd_preto += 1
                resultado_aluno = alternativas[i]
                pass
            if qtd_preto > 1:
                resultado_aluno = "*"
        print(resultado_aluno)
