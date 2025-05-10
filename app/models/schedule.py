from datetime import date

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.db.base import Base


class Schedule(Base):
    __tablename__ = "schedule"

    id: Mapped[int] = mapped_column(primary_key=True)
    medicine_name: Mapped[str] = mapped_column(comment="Название медикамента")
    periodicity: Mapped[int] = mapped_column(comment="Периодичность приема")
    receipt_duration_endless: Mapped[bool] = mapped_column(
        default=False, comment="Постоянный прием"
    )
    receipt_duration_end: Mapped[date | None] = mapped_column(
        default=None, nullable=True, comment="Конец приема"
    )
    user_id: Mapped[int] = mapped_column(comment="ID пациента")
