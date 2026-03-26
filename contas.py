import math, time, os
import pandas as pd

if not os.path.exists("contas.csv"):
    df = pd.DataFrame(columns=['categoria_ganhos', 'categoria_despesas', 'nome', 'valor', 'tipo'])
    df.to_csv("contas.csv", index=False)
else:
    try:
        df = pd.read_csv("contas.csv")
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=['categoria_ganhos', 'categoria_despesas', 'nome', 'valor', 'tipo'])

df = pd.read_csv("contas.csv")
df = df.dropna(how="all")

df["categoria_despesas"] = df["categoria_despesas"].fillna("")
df["categoria_ganhos"] = df["categoria_ganhos"].fillna("")
df["nome"] = df["nome"].fillna("")
df["tipo"] = df["tipo"].fillna("")

df["tipo"] = df["tipo"].fillna("")
df.loc[df["tipo"] == "despesa", "categoria_ganhos"] = ""

while True:
    print("1. Adicionar despesa")
    print("2. Adicionar ganhos")
    print("3. saldo")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("---------- ADICIONAR DESPESA ----------")
        time.sleep(1)
        entrada = input("Valor da despesa: ") 
        valor = float(entrada.replace(',', '.'))
        tipo = input("tipo (sempre despesa): ")
        nome = input("Nome da despesa: ")
        categoria = input("Categoria da despesa: ")

        nova_linha = {
            "valor": valor,
            "tipo": "despesa",
            "nome": nome,
            "categoria_despesas": categoria
        }

        df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
        df.to_csv("contas.csv", index=False)

        print("Despesa adicionada com sucesso!")

    elif opcao == 2:
        print("---------- ADICIONAR GANHOS ----------")
        time.sleep(1)
        entrada = input("Valor do ganho: ") 
        valor = float(entrada.replace(',', '.'))
        nome = input("Fonte: ")
        categoria = input("Categoria do ganho: ")

        nova_linha = {
            "valor": valor,
            "nome": nome,
            "tipo": "ganho",
            "categoria_ganhos": categoria
        }

        df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
        df.to_csv("contas.csv", index=False)

        print("Ganhos adicionados com sucesso!")

    elif opcao == 3:
        print("---------- SALDO ----------")
        time.sleep(1)
        total_despesas = df_despesas["valor"].sum()
        total_ganhos = df_ganhos["valor"].sum()
        saldo = total_ganhos - total_despesas

        print("\n ----- RESUMO FINANCEIRO -----")
        print(f"Total de despesas: R${total_despesas:.2f}")
        print(f"Total de ganhos: R${total_ganhos:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")
        print("Gostaria de saber por categoria? (s/n)")

        resposta = input().lower()

        print("---------- Despesas por Categoria ----------")
        if resposta == 's':
            despesas_categoria = df[df["tipo"]=="despesa"].groupby("categoria_despesas")["valor"].sum()
            ganhos_categoria = df[df["tipo"]=="ganho"].groupby("categoria_ganhos")["valor"].sum()

            print("\n ----- Despesas por Categoria -----")
            for cat, val in despesas_categoria.items():
                if cat != "":
                    print(f"{cat}: R${val:.2f}")

            print("\n ----- Ganhos por Categoria -----")
            for cat, val in ganhos_categoria.items():
                if cat != "":
                    print(f"{cat}: R${val:.2f}")

    elif opcao == 4:
        print("Saindo do programa...")
        break