def test_example(env):
    # Exemplo simples: valida se env está entre valores esperados
    assert env in ("QC", "UAT", "PRD")
    # Aqui você pode usar `env` para direcionar endpoints, bases de dados etc.
