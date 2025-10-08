# Schemas (Pydantic) usados nos endpoints e validações.
# Eu gosto de manter coisas de validação separadas dos modelos de banco.

from typing import List, Optional
from pydantic import BaseModel, field_validator, Field, ValidationError 
from pydantic import constr 

class CultureCreate(BaseModel):
    # CORREÇÃO: Usando Field para aplicar as restrições de string. Isso resolve o erro 'Call expression not allowed'.
    name: str = Field(strip_whitespace=True, min_length=1)

class FarmCultureCreate(BaseModel):
    culture_name: str
    harvest_year: int

class FarmCreate(BaseModel):
    name: str
    city: str
    state: str
    total_area: float
    arable_area: float
    vegetation_area: float
    cultures: Optional[List[FarmCultureCreate]] = []

    # Validação de regra de negócio: soma de áreas
    # CORREÇÃO: Substituí o @validator pelo @field_validator, a forma correta e moderna.
    @field_validator('vegetation_area', mode='after')
    @classmethod
    def areas_not_exceed_total(cls, v, info):
        # Em Pydantic v2, eu acesso os valores anteriores usando info.data
        total = info.data.get('total_area')
        arable = info.data.get('arable_area')
        
        # Se os campos essenciais não vierem, eu não valido.
        if total is None or arable is None:
            return v
        
        # Faço a checagem com uma pequena tolerância de ponto flutuante (1e-9).
        if (arable + v) > total + 1e-9:
            raise ValueError('A soma da área agricultável e de vegetação não pode ultrapassar a área total')
        return v

class ProducerCreate(BaseModel):
    identifier: str  # CPF ou CNPJ
    name: str
    farms: Optional[List[FarmCreate]] = []

    # Validação simples de CPF/CNPJ (apenas formato; ver validators.py para regras completas).
    # Eu só quero garantir que o campo não está vazio.
    # CORREÇÃO: Substituí o @validator pelo @field_validator. 'mode=before' é ideal para limpeza (strip).
    @field_validator('identifier', mode='before')
    @classmethod
    def identifier_must_not_be_empty(cls, v):
        # Tenho que converter v para string, caso não seja (vindo de JSON, geralmente é, mas previno o erro).
        if not isinstance(v, str):
            raise TypeError('Identifier must be a string')

        v_stripped = v.strip()
        if not v_stripped:
            raise ValueError('CPF ou CNPJ é obrigatório')
        return v_stripped # Retorno o valor limpo
        
# Responses
# Estes são os Schemas que uso para enviar dados de volta para o cliente (Read models).
class CultureRead(BaseModel):
    id: int
    name: str

class FarmRead(BaseModel):
    id: int
    name: str
    city: str
    state: str
    total_area: float
    arable_area: float
    vegetation_area: float
    # Estou garantindo que a lista de culturas é sempre uma lista, mesmo que vazia.
    cultures: List[CultureRead] = []

class ProducerRead(BaseModel):
    id: int
    identifier: str
    name: str
    # Aqui também garanto que a lista de fazendas sempre é uma lista.
    farms: List[FarmRead] = []
