import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    age: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)

    def __repr__(self):
        return f"<USER: {self.username}>"
