import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


arquivo = "Investimento_pib_direto.xlsx"

df = pd.read_excel(arquivo)

df.columns = [
    "Ano",
    "Todos os Níveis de Ensino",
    "Educação Básica",
    "Educação Infantil",
    "Ensino Fundamental - Anos Iniciais",
    "Ensino Fundamental - Anos Finais",
    "Ensino Médio",
    "Educação Superior"
]

"""
Formatando o Data frame
"""

df["Ano"] = pd.to_numeric(df["Ano"], errors="coerce")
df = df.dropna(subset=["Ano"])
df["Ano"] =  df["Ano"].astype(int)

df = df.reset_index(drop=True)

df.to_excel("Investimento_limpo.xlsx", index=False)

print("\nPrimeiras 5 linhas")
print(df.head())
print("\nResumo do data frame")
print(df.info())

colunas = df.columns.drop("Ano")

"""
Média, mediana, máximo e mínimo
"""

print("\nMédia:")
print(df[colunas].mean().round(2))

print("\nMediana:")
print(df[colunas].median().round(2))

print("\nMáximo:")
print(df[colunas].max().round(2))

print("\nMínimo:")
print(df[colunas].min().round(2))

"""
Variância, desvio padrão e amplitude
"""

amplitude = df[colunas].max() - df[colunas].min()

print("\nVariância:")
print(df[colunas].var().round(4))

print("\nDesvio Padrão:")
print(df[colunas].std().round(4))

print("\nAmplitude:")
print(amplitude.round(2))

"""
Diferença entre 2000 e 2021
"""

inicio = df.loc[df["Ano"] == 2000, colunas].iloc[0]
fim = df.loc[df["Ano"] == 2021, colunas].iloc[0]

diferenca = fim - inicio
variacao = (diferenca / inicio) * 100

print("\nDiferença entre 2000 e 2021:")
print(diferenca.round(2))

print("\nVariação percentual relativa:")
print(variacao.round(2).astype(str) + "%")

"""
Ano de maior investimento em cada categoria
"""

for coluna in colunas:
    indice_maximo = df[coluna].idxmax()

    ano = df.loc[indice_maximo,"Ano"]
    valor = df.loc[indice_maximo,coluna]

    print(f"\n{coluna}:")
    print(f"Ano de maio investimento:{ano}")
    print(f"Percentual do PIB: {valor:.6f}%")

"""
 Gráfico 1: evolução do investimento por nível de ensino
"""

plt.figure(figsize=(12,6))


for coluna in colunas:
    plt.plot(
        df["Ano"],
        df[coluna],
        label=coluna
    )

plt.title("Investimento público em educação (% do PIB)")
plt.xlabel("Ano")
plt.ylabel("Percentual do PIB (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("evolucao_investimentos.png", dpi=300, bbox_inches="tight")


"""
Gráfico 2: média de investimento por nível de ensino
"""

medias = df[colunas].mean()

plt.figure(figsize=(12, 6))

plt.bar(medias.index, medias.values)

plt.title("Média do investimento por nível de ensino (2000–2021)")
plt.xlabel("Nível de ensino")
plt.ylabel("Média do percentual do PIB (%)")

plt.xticks(rotation=45,ha="right")
plt.grid(axis="y")

plt.tight_layout()

plt.savefig("média_investimentos.png", dpi=300, bbox_inches="tight")

"""
Gráfico 3: comparação entre 2000 e 2021
"""

posicoes = np.arange(len(colunas))
largura = 0.35

plt.figure(figsize=(12, 6))


plt.bar(posicoes - largura/2, inicio.values,
        largura, label="2000")

plt.bar(posicoes + largura/2, fim.values,
        largura, label="2021")

plt.title("Investimento público em educação: 2000 x 2021")
plt.xlabel("Nível de ensino")
plt.ylabel("Percentual do PIB (%)")

plt.xticks(posicoes, colunas,rotation=45, ha="right")
plt.legend(title="Ano")
plt.grid(axis="y")
plt.tight_layout()

plt.savefig("comparação_investimentos.png", dpi=300, bbox_inches="tight")


