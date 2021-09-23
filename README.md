Código criado para conclusão do bootcamp junto a plataforma da Digital Innovation One consiste em:

1) Desenvolver um código em Python a ser executado como um job no ambiente PySpark da cloud Google Cloud Services
2) O job deve contar todas as palavras contidas em um arquivo .txt
3) A saída do job será analisada e submetida ao repositório atual do GitHub.

<p align="center"><img src="./DIO-Carrefour.png" width="500"></p>

## Desafio GCP Dataproc

O desafio faz parte do bootcamp Banco Carrefour Data Engineer na plataforma da Digital Innovation One:

__*Criando um ecossistema Hadoop totalmente gerenciado com Google Cloud Platform*__

O desafio consiste em efetuar um processamento de dados utilizando o produto Dataproc do GCP. Esse processamento irá efetuar a contagem das palavras de um livro e informar quantas vezes cada palavra aparece no mesmo.

---

### Etapas do Desafio

1. Criar um bucket no Cloud Storage
1. Atualizar o arquivo ```contador.py``` com o nome do Bucket criado nas linhas que contém ```{SEU_BUCKET}```.
1. Fazer o upload dos arquivos ```contador.py``` e ```livro.txt``` para o bucket criado (instruções abaixo)
    - https://cloud.google.com/storage/docs/uploading-objects

1. Utilizar o código em um cluster Dataproc, executando um Job do tipo PySpark chamando ```gs://{SEU_BUCKET}/contador.py```
1. O Job irá gerar uma pasta no bucket chamada ```resultado```. Dentro dessa pasta o arquivo ```part-00000``` irá conter a lista de palavras e quantas vezes ela é repetida em todo o livro.

### Entrega do Resultado

1. Criar um repositório no GitHub.
2. Criar um arquivo chamado ```resultado.txt```. Dentro desse arquivo, colocar as 10 palavras que mais são usadas no livro, de acordo com o resultado do Job.
3. Inserir os arquivo ```resultado.txt``` e ```part-00000``` no repositório e informar na plataforma da Digital Innovation One.

---

### Minha solução

Um ambiente Jupyter Notebook foi utilizado na Google Cloud para praticar comandos no Spark e analisar o problema sugerido no desafio.
Importei a biblioteca 're' para realizar operação de expressão regular, removendo os caracteres especais do texto, como ,.:! entre outros.
Analisando a saída do código mais simplificado do instrutor do desafio, nota-se vários caracteres especiais junto de palavras formando um única string.
Assim foi necessário usar a regex para correção.
Todas as palavras foram transformadas para minúsculas, evitando erros de contangem.
Foi aplicado um filtro para remover os espaços em branco da contagem, pois há mais de 1000 espaços inseridos no texto que são contados como palavras na ausência do filtro.
Alguns comentários referentes a linhas específicas do código estão descritos no arquivo ```contador.py```.
Diferentemente do ambiente do Jupyter Notebook, para o job rodar sem erro no cluster do GCS foi necessário definir a instância 'sc' explicitamente.