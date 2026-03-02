import pandas as pd
import polars as pl


def exemplo_ingest():
    # Criar um DataFrame com pandas
    df_pd = pd.DataFrame({
        "nome": ["Ana", "Bruno", "Carlos"],
        "idade": [23, 35, 29]
    })

    print("DataFrame com pandas:")
    print(df_pd)

    # Converter para polars
    df_pl = pl.DataFrame(df_pd)

    print("\nDataFrame convertido para polars:")
    print(df_pl)

    # Fazer uma operação simples com polars
    media_idade = df_pl["idade"].mean()
    print(f"\nMédia das idades: {media_idade}")
    return media_idade


if __name__ == "__main__":
    exemplo_ingest()
