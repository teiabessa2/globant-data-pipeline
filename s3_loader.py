import boto3
import io


def load_to_s3(df, bucket, key):
    """
    Carrega um DataFrame para o S3 em formato CSV.

    Parâmetros:
    df     : DataFrame (pandas ou polars convertido para pandas)
    bucket : nome do bucket S3
    key    : caminho/arquivo dentro do bucket (ex: 'data/arquivo.csv')
    """
    # Converter o DataFrame para CSV em memória
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)

    # Criar cliente S3
    s3 = boto3.client("s3")

    # Fazer upload para o bucket
    s3.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())

    print(f"Arquivo enviado para s3://{bucket}/{key}")
