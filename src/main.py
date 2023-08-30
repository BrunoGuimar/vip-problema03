# Função responsável por montar e processar as respostas dos alunos.
def resolver_respostas(qtd_linhas):
    for _ in range(int(qtd_linhas)):
        linhas = input().split()
        linhas = list(map(int, linhas))
        print(validar_respostas(linhas))
    return


# Função responsável por fazer a validação das respostas e retornar a alternativa marcada.
def validar_respostas(respostas):
    indice_alternativa = [indice for indice, valor in enumerate(respostas) if valor <= 127]
    if len(indice_alternativa) == 1:
        return chr(indice_alternativa[0] + ord('A'))
    else:
        return "*"


# Loop de inicialização forçada com condição para finalizar execução quando for passado 0 ao input.
while True:
    qtd_linhas = input()
    if int(qtd_linhas) == 0:
        break
    resolver_respostas(qtd_linhas)
