from datasource.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, Uuid
from typing import List
from sqlalchemy.dialects.postgresql import ARRAY
import uuid

class Game(Base):
    __tablename__ = "games"
 
    id: Mapped[uuid.UUID] = mapped_column(nullable=False, primary_key=True)
    board: Mapped[List[List[int]]] = mapped_column(ARRAY(Integer, dimensions=2))

