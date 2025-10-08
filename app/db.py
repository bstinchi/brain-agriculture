# Aqui eu crio a conexão com o banco usando SQLModel (que usa SQLAlchemy por baixo)
# Eu escolhi SQLModel porque facilita modelos combinando Pydantic + SQLAlchemy,
# o que economiza código mantendo clareza.

from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL') or 'postgresql+asyncpg://brain:brainpass@localhost:5432/braindb'

# Engine assíncrono
engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    # Função para criar tabelas caso não existam (turbo-mode, não é migration)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
