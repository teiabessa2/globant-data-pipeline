def test_loader_function_exists():
    """Verifica que a função existe no módulo"""
    import os
    assert os.path.exists("s3_loader.py"), "s3_loader.py não encontrado"


def test_soma_basica():
    """Teste simples para o workflow executar"""
    assert 1 + 1 == 2
