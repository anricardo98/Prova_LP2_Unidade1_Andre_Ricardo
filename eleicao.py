total_cadeiras = 29
QE = 12684
dados = []
aux = []
coligacao = []
contador = 0

with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        dados.append(line.split(";"))

partido_coligacao = [i[2] for i in dados]

partido_coligacao_separados = [i.split(" - ") for i in partido_coligacao]

for i in partido_coligacao_separados:
	try:
		coligacao.append(i[1])
	except:
		coligacao.append(i[0])

coligacao_set = set(coligacao)

votos_validos = 29 * 12684











