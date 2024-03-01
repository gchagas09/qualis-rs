def remove_duplicatas(lista):
    # Converte a lista em um conjunto para remover duplicatas
    conjunto_sem_duplicatas = set(lista)

    # Converte o conjunto de volta em uma lista
    lista_sem_duplicatas = list(conjunto_sem_duplicatas)

    lista_sem_duplicatas = sorted(lista_sem_duplicatas, key=len, reverse=True)

    return lista_sem_duplicatas


# Exemplo de uso da função
minha_lista = ["suplementação universitária",
"horário especial",
"Dispensa para realização de curso",
"servidor estudante",
"Dispensa para capacitação",
"dispensado do trabalho",
"realização de provas",
"freqüência a aulas",
"curso de atualização",
"regularmente matriculado",
"redução da carga horária",
"licença para qualificação",
"Licenças para Qualificação",
"redução total da carga horária",
"VANTAGENS AO FUNCIONÁRIO ESTUDANTE",
"redução parcial da carga horária",
"redução de carga horária",
"afastamento para qualificação",
"horário especial ao servidor estudante",
"LICENÇA PARA ESTUDOS",
"cursos de atualização",
"VANTAGENS DO FUNCIONÁRIO ESTUDANTE",
"funcionário estudante",
"promoção de nível",
"adicional de pós-graduação",
"realização de curso técnico",
"promoção vertical",
"gratificação de qualificação",
"adicional de qualificação",
"curso regular acima daquele exigido",
"nova escolaridade",
"promoção por escolaridade",
"curso regular acima daquele exigido",
"Gratificação de Incentivo a Titulação",
"Gratificação de Incentivo a Título",
"incentivo ao aumento no nível escolaridade",
"incentivo de qualificação",
"progressão por NÍVEIS de qualificação",
"vantagem adicional por escolaridade",
"incentivo à qualificação",
"promoção por titulação",
"mudança de nível por formação",
"gratificação de titulação",
"gratificação de incentivo de escolaridade",
"Gratificação Escolaridade",
"GRATIFICÃO POR CURSO SUPERIOR",
"ADICIONAL POR ESCOLARIDADE",
"promoção por merecimento",
"promoção por desempenho",
"avaliação de desempenho",
"avaliação de merecimento",
"critério de merecimento",
"desempenho conceitual",
"promoção por merecimento",
"auxílio escolar",
"bolsas de estudo",
"bolsa para capacitação",
"incentivo para capacitação",
"bolsa de estudo",
"auxílio financeiro para estud",
"custear o valor equivalente",
"auxílio para capacitação",
"servidor regularmente matriculado",
"CUSTEIO DE CURSO SUPERIOR",
"Auxílio para Formação",
"acesso a qualificação",
"matriculado e cursando",
"participação em curso de técnico, graduação",
"participação em curso de capacitação",
"ressarcimento total ou parcial de despesas",
"certificado de escolaridade do ensino formal",
"não tenha sido exigido para ingresso",
"certificado de cursos",
"cursos promovidos pela Administração Pública",
"Promoção Pela Qualificação Profissional",
"Titulação Por Grau Agregado",
"formação comprovada",
"titulação comprovada",
"correlação com as atribuições",
"correlação do curso",
"mudança de nível",
"níveis correspondem às titulações",
"progressão em níveis",
"programa de aprimoramento técnico-profissional",
"matriculados em curso superior",
"freqüência a cursos superiores",
"ausente para assistir às aulas",
"ausência para assistir às aulas",
"gratificação especial de Qualificação",
"gratificação de qualificação",
"Gratificação pela Escolaridade",
"gratificação de escolaridade",
"gratificação por graduação",
"adicional por aprimoramento",
"estímulo à qualificação",
"gratificação por qualificação",
"ADICIONAL DE ESCOLARIDADE",
"GRATIFICAÇÃO POR ESCOLARIDADE",
"Progressão Por Aperfeiçoamento",
"licença para participar de cursos",
"Gratificação Escolaridade",
"cursos de atualização e aperfeiçoamento",
"Gratificação por Nível Cultural",
"capacitação e aperfeiçoamento",
"participar de treinamentos",
"Auxílio Aperfeiçoamento",
"Adicional por Grau de Titulação",
"participação em curso técnico, de graduação",
"gratificação para os cargos com exigência de nível superior",
"NÍVEIS DE VALORIZAÇÃO, DE ACORDO COM A ESCOLARIDADE",
"Auxílio de Qualificação Profissional",
"qualificação por instrução"]

for i in range(len(minha_lista)):
    minha_lista[i] = minha_lista[i].lower()
lista_sem_duplicatas = remove_duplicatas(minha_lista)



print(lista_sem_duplicatas)