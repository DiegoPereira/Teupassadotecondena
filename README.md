# Teu passado te condena

## Considerações iniciais

Este projeto não tem a intenção de acusar ou denegrir a imagem de qualquer empresa. O objetivo da ferramenta é auxiliar os auditores a identificar o grau de desconfiança nas empresas que tenham participado de licitações a partir de fatores que são comuns em esquemas irregulares. Embora as análises do aplicativo possam facilitar a identificação de empresas que tenham semelhanças a outras que são comprovadamente inidôneas, esses resultados não têm o poder de afirmar que as empresas analisadas realmente cometeram alguma fraude. Fica a cargo dos auditores continuarem a investigação para garantir que as empresas com baixa confiança realmente tenham cometido alguma irregularidade.

## Proposta
A ideia do projeto é criar um modelo de classificação usando _Machine Leaning_ que se baseie nas características de empresas que são comprovadamente inidôneas para tentar ranquear outras empresas a respeito de seu grau de desconfiança.


## Impacto social
O principal beneficiado com essa ferramenta seŕá o gestor/auditor que já realiza essa tarefa manualmente e sem nenhum critério a seguir além de uma lista de nomes de empresas. Com essa aplicação auxiliaremos na ordem de escolha das empresas a serem analisadas e facilitando o trabalho dessas pessoas.

## Fatores estudados e variáveis utilizadas
Usamos os dados do SAGRES e do CEIS, proveniênte do Portal da Transparência do Governo Federal. Fizemos o tratamento dos dados para podermos usar melhor no nosso modelo, além de criarmos novas tabelas pois, necessitávamos de uma combinação de dados que não existia em apenas em uma tabela.


As variáveis que foram utilizadas para criar o modelo foram as seguintes:

| Nome da variável                  | Descrição   |
|-----|-----|
|qtdAditivosPorCPFCNPJ              | Quantidade de aditivos por CPF ou CNPJ |
|qtdContratos                       | Quantidade de contratos          |
|qtdContratos_ganhos                | Quantidade de contratos ganhos  |
|vl_TotalContrato                   | Valor total do contrato         |
|valor_total_pregao                 | Valor total em pregões          |
|valor_total_convite                | Valor total em convites         |
|valor_total_tomada                 | Valor total em tomadas          |
|participacoes_pregao               | Participações em pregões        |    
|participacoes_tomada               | Participações em tomadas        |
|participacoes_convite              | Participações por convite       |
|participacoes_total                | Participação total              |


## Usando a API

É possível realizar consultas ao API (REST) do Teu Passado Te Condena para obter o ranking crescente ou decrescente das empresas com base em um índice de confiabilidade da empresa calculado a partir dos fatores analisados ou mais informações sobre uma empresa. Para utilizar o API é necessário seguir alguns passos:

1. Para levantar o serviço é necessário executar o arquivo python server.py localizado no diretório api. Por default a aplicação executará na porta 5000.

2. Realizar uma requisição HTTP para algumas das seguintes rotas:

| Rota                  | Descrição   |
|-----|-----|
| /busca/cpf_cnpj/<id> | Retorna as informações sobre as prestações de serviço da detentora do número de cadastro de pessoa física ou jurídica especificado |
| ranking/<ordem> | Ranking das empresas ordenadas a partir da nota de confiabilidade gerada a partir do aprendizado de máquinas. A ordem pode ser "crescente" ou "decrescente" |
