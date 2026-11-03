from datasource.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
import uuid


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(nullable=False, primary_key=True)
    login: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

