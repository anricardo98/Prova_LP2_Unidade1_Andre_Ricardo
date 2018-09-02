#declaração das variáveis
total_cadeiras = 29
QE = 12684
vagas_ocupadas = 0
dados = []
coligacao = []
votos_coligacao = {}
qps = {}
eleitos = []

#processo de leitura do arquivo
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        dados.append(line.split(";"))
f.close()

#criação de uma lista para armazenar a informações do partido e coligacação de cada candidato
partido_coligacao = [i[2] for i in dados]

#criação de uma lista de listas que armazena o partido e da coligação
partido_coligacao_separados = [i.split(" - ") for i in partido_coligacao]

#criação de uma lista com a coligação de cada candidato, caso o partido esteja sozinho, consideramos este partido como uma coligacação
for i in partido_coligacao_separados:
	try:
		coligacao.append(i[1])
	except:
		coligacao.append(i[0])

#adicionando mais uma coluna a cada um dos elementos: a coluna com a coligação    
for contador, i in enumerate(dados):
  i.append(coligacao[contador])

#criando um dicionário que armazena como chave o nome da coligação e como valor o número de votos que aquela coligação recebeu
for i in dados:
  if i[4] in votos_coligacao:
    votos_coligacao[i[4]] += int(i[3])
  else:
    votos_coligacao[i[4]] = int(i[3])

#realizando o cálculo do quoeficiente partidario de cada coligação e contabilizando o número de vagas ocupadas no total
for key, value in votos_coligacao.items():
  qps[key] = value//QE
  vagas_ocupadas += value//QE

#criação de uma biblioteca que armazena o número de vagas que cada coligação recebeu após o cálculo do QP.
#como este cálculo ainda não foi realizado, todos os partidos recebem inicialmente 0
vagas_recebidas = {key: 0 for key, value in qps.items()}

#enquanto o número de vagas ocupadas for menor que o número total de cadeiras, realizasse o cálculo da média.
while (vagas_ocupadas < total_cadeiras):
  media = {key:(votos_coligacao[key]/(value + vagas_recebidas[key] + 1)) for (key, value) in qps.items() if value > 0}
  #na linha abaixo, observasse uma função que recebe a chave com a maior média cálculada e atribui +1 a quantidade de cadeiras recebidas
  vagas_recebidas[max(media.keys(), key=(lambda key: media[key]))] += 1
  vagas_ocupadas += 1

#biblioteca que armazena o número total de vagas que cada coligação recebeu
vagas_coligacao = {key: (value + vagas_recebidas[key]) for key, value in qps.items()}

#função que armazena os candidatos eleitos:
#a avaliação é feita por coligação
#primeiro: criasse uma biblioteca com o número de votos do candidatos como chave e todas as informações dele como valor
#segundo: ordena as chaves e armazena o número de votos dos candidatos eleitos
#terceiro: pega os dados de todos os candidatos eleitos
for key, value in vagas_coligacao.items():
  if (value > 0):
    candidatos_partido = {int (i[3]): i for i in dados if (i[4] == key)}
    partido_ordenado = sorted(candidatos_partido, reverse = True)[0:value]
    for i in partido_ordenado:
      eleitos.append(candidatos_partido[i])

#utilizando da mesma lógica do iterador anterior, realizasse a ordenação dos candidatos eleitos pelos seus número de votos
eleitos_voto = {int(i[3]): i[0:4] for i in eleitos}
votos_ordenados = sorted(eleitos_voto, reverse = True)
eleitos_ordenados = [eleitos_voto[i] for i in votos_ordenados]

#escrita no arquivo "eleicao.tsv"
#obs: caso a saída do arquivo apresente problema na impressão (um dado aparece junto ao da linha anterior), substituir o '\r\n' por '\n'
with open("eleicao.tsv", "w", encoding="utf-8") as f:
  for i in eleitos_ordenados:
    f.write("\t".join(i) + '\r\n')

print ("Os candidatos eleitos podem ser encontrados no arquivo eleicao.tsv")
f.close()