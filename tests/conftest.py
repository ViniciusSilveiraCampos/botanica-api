import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from fast_zero.app import app
from fast_zero.database import get_session
from fast_zero.model import table_registry, User


@pytest.fixture
def client(session):

    # Tudo que depende do banco de dados em produção.
    # Durante o momento de teste será sobreescrito para a utilização da função de teste.
    def fake_session():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = fake_session
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:',
                           connect_args={'check_same_thread': False},
                           poolclass=StaticPool)
    # Definindo para que ele não crie uma nova thread ao testar
    # pois enquanto ele roda, ele está testando.
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture()
def user(session):
    user = User(username='Teste',
                email="Teste@test.com",
                password="123teste")
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
