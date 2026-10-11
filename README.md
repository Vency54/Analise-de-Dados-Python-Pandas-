# Análise do Investimento Público em Educação (% do PIB)

Projeto em Python para tratar, analisar estatisticamente e visualizar dados de investimento público em educação como percentual do Produto Interno Bruto (PIB), considerando o período de 2000 a 2021.

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
- **OpenPyXL** — mecanismo utilizado pelo Pandas para ler e gravar arquivos Excel (`.xlsx`).

## Estrutura dos arquivos

Coloque a planilha original e o script Python na mesma pasta. Ao executar o script, serão gerados os seguintes arquivos:

```text
.
├── Investimento_pib_direto.xlsx
├── seu_script.py
├── Investimento_limpo.xlsx
├── evolucao_investimentos.png
├── média_investimentos.png
└── comparação_investimentos.png
```

`seu_script.py` representa o nome do arquivo Python utilizado no projeto.

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

Uma variação positiva indica aumento; uma variação negativa indica redução. Essa fórmula exige que o valor inicial de 2000 seja diferente de zero.

### 4. Ano de maior investimento

Para cada categoria, o programa identifica o maior valor da série e informa o ano correspondente.

## Gráficos gerados

### `evolucao_investimentos.png`

Gráfico de linhas que mostra a evolução anual do investimento público em cada categoria de ensino.

### `média_investimentos.png`

Gráfico de barras com a média do investimento de cada categoria durante o período analisado.

### `comparação_investimentos.png`

Gráfico de barras agrupadas que compara os valores de cada categoria nos anos de 2000 e 2021.

Os gráficos são salvos com resolução de **300 DPI**, adequada para relatórios e apresentações. Eles são gravados no diretório de trabalho em que o script é executado.

## Requisitos

- Python 3 instalado.
- Planilha `Investimento_pib_direto.xlsx` disponível na pasta do projeto.

Instale as bibliotecas necessárias pelo terminal:

```bash
python -m pip install pandas matplotlib numpy openpyxl
```

## Como executar

1. Salve o código em um arquivo Python, por exemplo, `analise_investimentos.py`.
2. Coloque `Investimento_pib_direto.xlsx` na mesma pasta.
3. Abra o terminal nessa pasta.
4. Instale as dependências, caso ainda não estejam instaladas.
5. Execute:

```bash
python analise_investimentos.py
```

Ao final, as estatísticas serão exibidas no terminal e os arquivos Excel e PNG serão criados na pasta de execução.

## Observações

- A planilha de entrada precisa ter as colunas na ordem esperada pelo script, pois os nomes são definidos manualmente.
- A base deve conter registros para os anos de 2000 e 2021; caso contrário, a comparação não poderá ser realizada.
- O gráfico de evolução utiliza todas as categorias, o que pode deixar a legenda extensa.
- Os arquivos PNG são atualizados quando o script é executado novamente.
