# Aqui estão os modelos da camada de domínio (persistência).
# Eu meparei modelos e schemas para respeitar separação de responsabilidades.

from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date

class Culture(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    # Relação many-to-many via tabela associativa será criada manualmente

class Producer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    identifier: str  # CPF ou CNPJ
    name: str

    farms: List['Farm'] = Relationship(back_populates='producer')

class FarmCultureLink(SQLModel, table=True):
    farm_id: Optional[int] = Field(default=None, foreign_key='farm.id', primary_key=True)
    culture_id: Optional[int] = Field(default=None, foreign_key='culture.id', primary_key=True)
    harvest_year: int

class Farm(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    producer_id: int = Field(foreign_key='producer.id')
    name: str
    city: str
    state: str
    total_area: float
    arable_area: float
    vegetation_area: float

    producer: Optional[Producer] = Relationship(back_populates='farms')
    cultures: List[Culture] = Relationship(back_populates='farms', link_model=FarmCultureLink)

# Back-populate list on Culture
Culture.farms = Relationship(back_populates='cultures', link_model=FarmCultureLink)
