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

    id = Column("opr_id", Integer, primary_key=True, index=True)
    inicio_plantio = Column("opr_inicio_plantio", Date, index=True)
    fim_plantio = Column("opr_fim_plantio", Date, index=True)
    inicio_colheita = Column("opr_inicio_colheita", Date, index=True)
    fim_colheita = Column("opr_fim_colheita", Date, index=True)
    estado = Column("opr_estado", String, index=True)
    municipio = Column("opr_municipio", String, index=True)

    solo_id = Column("opr_sol", Integer, ForeignKey("sol_solo.sol_id"))
    solo = relationship("Solo", back_populates="operacao")

    irrigacao_id = Column("opr_irg", Integer, ForeignKey("irg_irrigacao.irg_id"))
    irrigacao = relationship("Irrigacao", back_populates="operacao")

    cultivo_id = Column("opr_clt", Integer, ForeignKey("clt_cultivo.clt_id"))
    cultivo = relationship("Cultivo", back_populates="operacao")

    grao_semente_id = Column("opr_gsm", Integer, ForeignKey("gsm_grao_semente.gsm_id"))
    grao_semente = relationship("GraoSemente", back_populates="operacao")

    ciclo_id = Column("opr_ccl", Integer, ForeignKey("ccl_ciclo.ccl_id"))
    ciclo = relationship("Ciclo", back_populates="operacao")

    gleba_id = Column("opr_glb", Integer, ForeignKey("glb_gleba.glb_id"))
    gleba = relationship("Gleba", back_populates="operacao")

    empreendimento_id = Column("opr_emp", Integer, ForeignKey("emp_empreendimento.emp_id"))
    empreendimento = relationship("Empreendimento", back_populates="operacao")

    propriedade = relationship("Propriedade", back_populates="operacao")


class Solo(Base):
    __tablename__ = "sol_solo"

    id = Column("sol_id", Integer, primary_key=True, index=True)
    descricao = Column("sol_descricao", String, index=True)

    operacao = relationship("Operacao", back_populates="solo")

class Irrigacao(Base):
    __tablename__ = "irg_irrigacao"

    id = Column("irg_id", Integer, primary_key=True, index=True)
    descricao = Column("irg_descricao", String, index=True)

    operacao = relationship("Operacao", back_populates="irrigacao")


class Cultivo(Base):
    __tablename__ = "clt_cultivo"

    id = Column("clt_id", Integer, primary_key=True, index=True)
    descricao = Column("clt_descricao", String, index=True)

    operacao = relationship("Operacao", back_populates="cultivo")


class GraoSemente(Base):
    __tablename__ = "gsm_grao_semente"

    id = Column("gsm_id", Integer, primary_key=True, index=True)
    descricao = Column("gsm_descricao", String, index=True)

    operacao = relationship("Operacao", back_populates="grao_semente")


class Ciclo(Base):
    __tablename__ = "ccl_ciclo"

    id = Column("ccl_id", Integer, primary_key=True, index=True)
    descricao = Column("ccl_descricao", String, index=True)

    operacao = relationship("Operacao", back_populates="ciclo")


class Gleba(Base):
    __tablename__ = "glb_gleba"

    id = Column("glb_id", Integer, primary_key=True, index=True)
    poligono = Column("glb_poligono", Geography('POLYGON'), nullable=False)

    operacao = relationship("Operacao", back_populates="gleba")


class Empreendimento(Base):
    __tablename__ = "emp_empreendimento"

    id = Column("emp_id", Integer, primary_key=True, index=True)
    finalidade = Column("emp_finalidade", String, index=True)
    atividade = Column("emp_atividade", String, index=True)
    modalidade = Column("emp_modalidade", String, index=True)
    produto = Column("emp_produto", String, index=True)
    variedade = Column("emp_variedade", String, index=True)
    cesta = Column("emp_cesta", String, index=True)
    zoneamento = Column("emp_zoneamento", String, index=True)

    operacao = relationship("Operacao", back_populates="empreendimento")

class Propriedade(Base):
    __tablename__ = "ppr_propriedade"

    id = Column("ppr_id", Integer, primary_key=True, index=True)
    sncr = Column("ppr_sncr", String, index=True)
    nirf = Column("ppr_nirf", String, index=True)
    car = Column("ppr_car", String, index=True)

    operacao_id = Column("ppr_opr", Integer, ForeignKey("opr_operacao.opr_id"))
    operacao = relationship("Operacao", back_populates="propriedade")
