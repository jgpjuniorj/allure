# conftest.py

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="QC",
        help="Define o ambiente de execução: QC, UAT ou PRD"
    )

import pytest

@pytest.fixture
def env(request):
    """
    Fixture que retorna o valor do parâmetro --env passado ao pytest.
    Uso em testes:
        def test_algo(env):
            assert env in ("QC", "UAT", "PRD")
    """
    return request.config.getoption("--env")