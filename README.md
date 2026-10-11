# Análise do Investimento Público em Educação (% do PIB)

Projeto em Python para tratar, analisar estatisticamente e visualizar dados de investimento público em educação como percentual do Produto Interno Bruto (PIB), por nível de ensino, no período de 2000 a 2021.

## Fonte dos dados

Os dados utilizados neste projeto foram obtidos no portal oficial do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (**Inep**), na página de [Indicadores Financeiros Educacionais](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-financeiros-educacionais).

A planilha utilizada no projeto é `Investimento_pib_direto.xlsx`, referente ao indicador **Percentual do investimento direto em relação ao Produto Interno Bruto (PIB), por nível de ensino — 2000 a 2021**.

O Inep disponibiliza diferentes indicadores financeiros educacionais. Confira o título do arquivo baixado na página oficial e utilize a planilha correspondente ao indicador analisado neste projeto.

## Objetivos

- Ler os dados de uma planilha Excel.
- Padronizar os nomes das colunas e limpar os registros inválidos de ano.
- Exportar uma versão limpa da base de dados.
- Calcular estatísticas descritivas para cada nível de ensino.
- Identificar o ano de maior investimento em cada categoria.
- Comparar os valores de investimento entre 2000 e 2021.
- Gerar gráficos em formato PNG.

## Tecnologias utilizadas

- **Python**
- **Pandas** — leitura, limpeza e análise dos dados.
- **Matplotlib** — criação dos gráficos.
- **NumPy** — criação das posições das barras no gráfico comparativo.
- **OpenPyXL** — leitura e gravação de arquivos Excel (`.xlsx`).

## Estrutura dos arquivos

Depois de clonar o repositório e colocar a planilha de entrada na pasta do projeto, a estrutura será semelhante a esta:

```text
.
├── Investimento_pib_direto.xlsx
├── analise_investimentos.py
└── README.md
```

Os arquivos de saída — planilha limpa e gráficos — são gerados quando o script é executado. `analise_investimentos.py` é um exemplo de nome para o script; substitua-o pelo nome real do arquivo, se for diferente.

## Categorias analisadas

- Todos os Níveis de Ensino
- Educação Básica
- Educação Infantil
- Ensino Fundamental - Anos Iniciais
- Ensino Fundamental - Anos Finais
- Ensino Médio
- Educação Superior

## Análises realizadas

### 1. Limpeza e preparação dos dados

O programa lê a planilha `Investimento_pib_direto.xlsx`, define nomes para as colunas e converte a coluna `Ano` para valores numéricos. Linhas sem um ano válido são removidas, os anos são convertidos para inteiros e o índice do DataFrame é reorganizado.

A base tratada é exportada para `Investimento_limpo.xlsx`.

### 2. Estatística descritiva

Para cada categoria de ensino, o programa calcula:

- **Média:** valor médio de investimento no período.
- **Mediana:** valor central dos dados ordenados.
- **Máximo:** maior percentual registrado.
- **Mínimo:** menor percentual registrado.
- **Variância:** medida da dispersão dos valores em relação à média.
- **Desvio padrão:** medida da dispersão na mesma unidade dos dados.
- **Amplitude:** diferença entre o maior e o menor valor.

Os resultados são apresentados no terminal. O arredondamento aplicado nas impressões serve para facilitar a leitura dos resultados exibidos.

### 3. Comparação entre 2000 e 2021

O programa calcula, para cada categoria, a diferença entre o valor de 2021 e o de 2000, além da variação percentual relativa:

`((valor de 2021 - valor de 2000) / valor de 2000) * 100`

Uma variação positiva indica aumento; uma variação negativa indica redução. A fórmula pressupõe que o valor inicial de 2000 seja diferente de zero.

### 4. Ano de maior investimento

Para cada categoria, o programa identifica o maior valor da série e informa o ano correspondente.

## Gráficos gerados

### `evolucao_investimentos.png`

Gráfico de linhas que mostra a evolução anual do investimento em cada categoria de ensino.

### `média_investimentos.png`

Gráfico de barras com a média do investimento de cada categoria durante o período analisado.

### `comparação_investimentos.png`

Gráfico de barras agrupadas que compara os valores de cada categoria nos anos de 2000 e 2021.

Os gráficos são salvos com resolução de **300 DPI**, adequada para relatórios e apresentações.

## Como obter o projeto com Git

No terminal, execute:

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO
```

Substitua `URL_DO_REPOSITORIO` pela URL real do repositório no GitHub (ou em outro serviço Git) e `NOME_DO_REPOSITORIO` pelo nome da pasta criada pelo `git clone`.

**Importante:** o `git clone` baixa os arquivos que foram enviados ao repositório. Se a planilha `Investimento_pib_direto.xlsx` não estiver incluída nele, será necessário baixá-la da [página oficial do Inep](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-financeiros-educacionais) e colocá-la na pasta do projeto antes de executar o script.

## Instalação das dependências

É recomendado utilizar Python 3. Com o terminal aberto na pasta do projeto, execute:

```bash
python -m pip install pandas matplotlib numpy openpyxl
```

## Como executar

1. Clone o repositório com `git clone`.
2. Entre na pasta do projeto com `cd`.
3. Confira se a planilha `Investimento_pib_direto.xlsx` está na pasta do script.
4. Instale as dependências.
5. Execute o script, ajustando o nome do arquivo se necessário:

```bash
python analise_investimentos.py
```

As estatísticas serão exibidas no terminal. A planilha limpa e os três gráficos PNG serão gerados no diretório de trabalho.

## Observações

- A planilha de entrada precisa ter as colunas na ordem esperada pelo script, pois os nomes são definidos manualmente.
- A base precisa conter registros para os anos de 2000 e 2021 para realizar a comparação.
- O gráfico de evolução inclui todas as categorias, o que pode deixar a legenda extensa.
- Os arquivos de saída são atualizados quando o script é executado novamente.
- A fonte dos dados é o Inep; este projeto realiza uma análise programática da planilha e não representa, por si só, uma publicação oficial do Instituto.
