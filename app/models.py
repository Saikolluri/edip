from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Regulation(Base):
    __tablename__ = "regulations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    jurisdiction = Column(String, index=True)
    industry = Column(String, index=True)
    description = Column(Text)

class BusinessAction(Base):
    __tablename__ = "business_actions"

    id = Column(Integer, primary_key=True, index=True)
    action_type = Column(String, index=True)
    industry = Column(String, index=True)
    location = Column(String, index=True)

