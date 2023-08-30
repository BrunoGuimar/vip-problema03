# vip-problema03

O professor John decidiu aplicar apenas testes de múltipla escolha aos seus alunos. Em cada teste, cada pergunta terá cinco alternativas (A, B, C, D e E), e o professor distribuirá uma folha de respostas para cada aluno. Ao final do teste, as folhas de respostas serão digitalizadas e processadas digitalmente para obter a nota do teste de cada aluno. Inicialmente, ele pediu a um sobrinho, que conhece programação de computadores, para escrever um programa para extrair as alternativas marcadas pelos alunos nas folhas de respostas. O sobrinho escreveu um bom software, mas não conseguiu terminar porque precisa estudar para o concurso ICPC.

Durante o processamento, as folhas de respostas são digitalizadas em tons de cinza entre 0 (preto total) e 255 (branco total). Após detectar a posição dos cinco retângulos correspondentes a cada uma das alternativas de uma pergunta, o software calcula a média do nível de cinza do pixel para cada retângulo, retornando um valor inteiro correspondente a cada alternativa. Se o retângulo foi preenchido corretamente, o valor médio é zero (preto total). Se o retângulo foi deixado em branco, o valor médio é 255 (branco total). Assim, idealmente, se os valores médios para cada alternativa de uma pergunta forem (255, 0, 255, 255, 255), sabemos que o aluno marcou a alternativa B para essa pergunta. No entanto, como as folhas de respostas são processadas individualmente, o valor médio de cinza para um retângulo completamente preenchido não é necessariamente 0 (pode ser maior), e o valor para um retângulo não preenchido não é necessariamente 255 (pode ser menor). O professor John determinou que os níveis médios de cinza dos retângulos seriam divididos em duas classes: aqueles com valores iguais ou menores que 127 são considerados pretos e aqueles com valores acima de 127 serão considerados brancos.

Obviamente, nem todas as questões de todas as folhas de respostas estão marcadas corretamente. Pode acontecer que um aluno cometa um erro e marque mais de uma alternativa para a mesma pergunta, ou não marque nenhuma alternativa. Nesses casos, a resposta à pergunta deve ser desconsiderada.

Agora, o professor John precisa de um voluntário para escrever um programa que, dado os valores médios de cinza dos cinco retângulos correspondentes às alternativas de uma pergunta, determine qual alternativa foi marcada, ou se a resposta à pergunta deve ser desconsiderada.

Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro N, indicando o número de perguntas na folha de respostas (1 ≤ N ≤ 255). Cada uma das N linhas seguintes descreve a resposta a uma pergunta e contém cinco inteiros A, B, C, D e E, indicando os valores médios de cinza para cada alternativa (0 ≤ A, B, C, D, E ≤ 255).

O último caso de teste é seguido por uma linha contendo apenas o número zero.

Saída
Para cada caso de teste de entrada, o seu programa deve imprimir N linhas, cada linha correspondendo a uma pergunta. Se a resposta à pergunta foi preenchida corretamente na folha de respostas, a linha deve conter a alternativa selecionada ('A', 'B', 'C', 'D' ou 'E'). Caso contrário, a linha deve conter o caractere '*' (asterisco).

# Checklist

Construir a matriz atráves dos inputs. [ X ]

Armazenar a posição que estiver a 'resposta' do aluno "A", "B", "C", "D" ou "E". [ X ]

Desenvolver uma forma de percorrer o array e validar se é <= 127 "respondido" ou > 127 "em branco". [ X ]

Validar a funcionalidade do código no site. [ X ]
