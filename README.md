# Hackfest: Contra a corrupção
## Projeto: Teu passado te condena

--------------------------------------------------------------------

## Considerações iniciais e avisos
***
Neste projeto não temos intenção nenhuma de acusar ou sugerir que qualquer empresa citada seja corrupta ou faça uso de atos ilicitos. Esta ferramenta é apenas para o auxilio a auditóres/gestores na parte de investigação com relação a ordem das empresas, o ranking é apenas ilustrativo e faz uso de <i>Machine Learning</i> com os dados passados de empresas realmente corruptas para gerar as pontuações das empresas com o intervalo de confiança X. Não temos qualquer ligação com as empresas ou seus donos e não queremos prejudicar em qualquer modo suas imagens e/ou integridade.



## Proposta
***
Nossa ideia para esse projeto é criar um modelo de classificação usando <i>Machine Leaning</i>, com os dados de empresas comprovadamente irregulares ou corruptas, tentar identificar padrões com novas empresas, e classifica-las em um ranking através de uma porcentagem de similaridade dada pelo nosso modelo.


## Impacto social
***
O principal beneficiado com essa ferramenta seŕá o gestor/auditor que já realiza essa tarefa manualmente e sem nenhum critério a seguir além de uma lista de nomes de empresas. Com essa aplicação auxiliaremos na ordem de escolha das empresas a serem analisadas e facilitando o trabalho dessas pessoas.

## Fatores estudados e variáveis utilizadas
***
Usamos os dados do SAGRES e do CEIS, proveniênte do Portal da Transparência do Governo Federal. Fizemos o tratamento dos dados para podermos usar melhor no nosso modelo, além de criarmos novas tabelas pois, necessitávamos de uma combinação de dados que não existia em apenas em uma tabela.


As variáveis que foram utilizadas para criar o modelo foram as seguintes:
***
* Nome da variável              | Descrição
  ----------------------------- | ---------------------------------------------------------------------------------
    I                           | Iron
    A                           | Arnaldo
    C                           | Caio
    R                           | Raquel
    L                           | Luiz
    D                           | Diego
    I                           | Igor
    D                           | Diogo    
 
