matriz = []
qtd_preto = 0
alternativas = ["A", "B", "C", "D", "E"]
entrada = """
3
0 255 255 255 255
255 255 255 255 0
255 255 127 255 255
4
200 200 200 0 200
200 1 200 200 1
1 2 3 4 5
255 5 200 130 205
0
"""

linhas_entrada = entrada.strip().split('\n')
i = 0
while i < len(linhas_entrada):
    n = int(linhas_entrada[i])
    i += 1
    for _ in range(n):
        linha = list(map(int, linhas_entrada[i].split()))
        matriz.append(linha)
        i += 1

# for i in range(int(n)):
#     linhas = input().split()
#     linhas = list(map(int, linhas))
#     matriz.append(linhas)


while qtd_preto < 1:
    for linhas in matriz:
        qtd_preto = 0
        for i, numero in enumerate(linhas):
            if numero <= 127:
                qtd_preto += 1
                resultado_aluno = alternativas[i]
            if qtd_preto > 1:
                resultado_aluno = "*"
        print(resultado_aluno)