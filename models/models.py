from geoalchemy2 import Geography
from geoalchemy2.shape import from_shape
from shapely.geometry import Polygon, Point, shape

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Operacao(Base):
    __tablename__ = "opr_operacao"

    id = Column(Integer, primary_key=True, index=True)
    inicio_plantio = Column(Date, index=True)
    fim_plantio = Column(Date, index=True)
    inicio_colheita = Column(Date, index=True)
    fim_colheita = Column(Date, index=True)
    estado = Column(String, index=True)
    municipio = Column(String, index=True)

    solo_id = Column(Integer, ForeignKey("sol_solo.id"))
    solo = relationship("Solo", back_populates="operacao")

    irrigacao_id = Column(Integer, ForeignKey("irg_irrigacao.id"))
    irrigacao = relationship("Irrigacao", back_populates="operacao")

    cultivo_id = Column(Integer, ForeignKey("clt_cultivo.id"))
    cultivo = relationship("Cultivo", back_populates="operacao")

    grao_semente_id = Column(Integer, ForeignKey("gsm_grao_semente.id"))
    grao_semente = relationship("GraoSemente", back_populates="operacao")

    ciclo_id = Column(Integer, ForeignKey("ccl_ciclo.id"))
    ciclo = relationship("Ciclo", back_populates="operacao")

    gleba_id = Column(Integer, ForeignKey("opr_gleba.id"))
    gleba = relationship("Gleba", back_populates="operacao")

    empreendimento_id = Column(Integer, ForeignKey("emp_empreendimento.id"))
    empreendimento = relationship("Empreendimento", back_populates="operacao")

    propriedade = relationship("Propriedade", back_populates="operacao")


class Solo(Base):
    __tablename__ = "sol_solo"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)

    operacao = relationship("Operacao", back_populates="solo")

class Irrigacao(Base):
    __tablename__ = "irg_irrigacao"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)

    operacao = relationship("Operacao", back_populates="irrigacao")


class Cultivo(Base):
    __tablename__ = "clt_cultivo"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)

    operacao = relationship("Operacao", back_populates="cultivo")


class GraoSemente(Base):
    __tablename__ = "gsm_grao_semente"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)

    operacao = relationship("Operacao", back_populates="grao_semente")


class Ciclo(Base):
    __tablename__ = "ccl_ciclo"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)

    operacao = relationship("Operacao", back_populates="ciclo")


class Gleba(Base):
    __tablename__ = "opr_gleba"

    id = Column(Integer, primary_key=True, index=True)
    poligono = Column(Geography('POLYGON'), nullable=False)

    operacao = relationship("Operacao", back_populates="gleba")


class Empreendimento(Base):
    __tablename__ = "emp_empreendimento"

    id = Column(Integer, primary_key=True, index=True)
    finalidade = Column(String, index=True)
    atividade = Column(String, index=True)
    modalidade = Column(String, index=True)
    produto = Column(String, index=True)
    variedade = Column(String, index=True)
    cesta = Column(String, index=True)
    zoneamento = Column(String, index=True)

    operacao = relationship("Operacao", back_populates="empreendimento")

class Propriedade(Base):
    __tablename__ = "ppr_propriedade"

    id = Column(Integer, primary_key=True, index=True)
    sncr = Column(String, index=True)
    nirf = Column(String, index=True)
    car = Column(String, index=True)

    operacao_id = Column(Integer, ForeignKey("opr_operacao.id"))
    operacao = relationship("Operacao", back_populates="propriedade")
