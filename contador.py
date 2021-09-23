# -*- coding: utf-8 -*-
'''
Bootcamp Engenharia de Dados Carrefour
Desafio Dataproc: executar um job PySpark chamado contador.py em um cluster 
Dataproc do Google Cloud Service para contar as 10 palavras mais usadas no 
arquivo livro.txt; submeter o resultado para umas pasta no github.
'''

import re
from pyspark import SparkContext, SparkConf

'''
No processamento do arquivo texto para o RDD mapeado é necessário: 
1) transformar tudo para minúsculo: o contador não será case sensitive
2) remover pontuação: não contar caracteres especiais
3) fazer o split por espaço em branco para separar as palvras
4) remover espaços em branco: não contar os espaços encontrados
'''

#cria a instância 'sc'
#carrega o arquivo livro.txt e realiza um split para listar as palavras no RDD "wordsRDD"
sc = SparkContext("local", "Bootcamp Engenharia de Dados Carrefour")
wordsRDD = sc.textFile("gs://{SEU_BUCKET}/livro.txt"")
wordsRDDmap = wordsRDD.flatMap(lambda line: [re.sub(re.compile(r'[^a-zA-Z0-9\s]'),"",wordsRDD) for wordsRDD in line.lower().split(" ")]).filter(lambda s:len(s)>0)

#mapeia cada palavra e cria a tupla chave/valor (word, 1); 
#método redubeByKey() agrega todas as chaves e soma os valores;
#ordena as palavras mais frequentes em ordem decrescente.
wordCounts = wordsRDDmap.map(lambda word: (word, 1)).reduceByKey(lambda a,b: a+b).sortBy(lambda a:a[1], ascending=False)

#salva o resultado, conforme solicitado no desafio
wordCounts.saveAsTextFile("gs://{SEU_BUCKET}/resultado")

#cria novo RDD e salva arquivo contendo apenas as top 10 palavras
top10words = sc.parallelize(wordCounts.take(10))
top10words.saveAsTextFile("gs://{SEU_BUCKET}/Top10words")