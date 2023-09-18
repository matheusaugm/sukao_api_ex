from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# importando os elementos definidos no modelo
from model.base import Base
from model.produto import Produto
from database import DB_CONFIG

# URL de acesso ao banco (essa é uma URL de acesso ao PostgreSQL local)
db_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"

# Cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Cria um criador de sessão SQLAlchemy
Session = sessionmaker(bind=engine)

# Cria o banco se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)

# Cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)

# Agora você pode criar instâncias de sessão quando precisar
# Exemplo de como criar uma sessão:
# session = Session()
# ...
# session.commit()
# session.close()
