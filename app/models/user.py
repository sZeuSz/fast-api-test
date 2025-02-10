from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, Date
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.enums import UserType, PersonType, GenderType, EducationType, EthnicityType, SocialLinkType, DesabilityType, JuristicPersonType

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_type = Column(Enum(UserType), nullable=False)
    person_type = Column(Enum(PersonType), nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    cell_phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_profile_completed = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    gender = Column(Enum(GenderType), nullable=True)
    ethnicity = Column(Enum(EthnicityType), nullable=True)
    education = Column(Enum(EducationType), nullable=True)

    physical_person = relationship("PhysicalPerson", back_populates="user", uselist=False)
    juristic_person = relationship("JuristicPerson", back_populates="user", uselist=False)
    social_links = relationship("SocialLinks", back_populates="user")
    addresses = relationship("Address", back_populates="user")

class PhysicalPerson(Base):
    __tablename__ = "physical_persons"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    cpf = Column(String, unique=True, nullable=False)
    rg = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    disability = Column(Enum(DesabilityType), default=False)

    user = relationship("User", back_populates="physical_person")

class JuristicPerson(Base): 
    __tablename__ = "juristic_persons"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    cnpj = Column(String, unique=True, nullable=False)
    company_name = Column(String, nullable=False)
    fantasy_name = Column(String, nullable=True)
    legal_representative = Column(String, nullable=False)
    legal_representative_cpf = Column(String, nullable=False)
    foundation_date = Column(Date, nullable=False)
    juristic_person_type = Column(Enum(JuristicPersonType), nullable=False)

    user = relationship("User", back_populates="juristic_person")

class SocialLinks(Base):
    __tablename__ = "social_links"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(Enum(SocialLinkType), nullable=False)
    url = Column(String, nullable=False)

    user = relationship("User", back_populates="social_links")

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    postal_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(String, nullable=False)
    neighborhood = Column(String, nullable=False)
    complement = Column(String, nullable=True)
    zone = Column(String, nullable=True)

    user = relationship("User", back_populates="addresses")
