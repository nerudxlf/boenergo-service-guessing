import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from src.database import db_connect


class ColorNames(db_connect.Base):
    __tablename__: str = "color_names"
    id = _sql.Column(_sql.Integer, primary_key=True)
    name = _sql.Column(_sql.String(64), nullable=False)
    color = _orm.relationship('Colors', back_populates='color_name', uselist=False)


class Colors(db_connect.Base):
    """tak mnogo colors..."""
    __tablename__: str = "colors"
    id = _sql.Column(_sql.Integer, primary_key=True)
    name_id = _sql.Column(_sql.Integer, _sql.ForeignKey('color_names.id'))
    color_name = _orm.relationship('ColorNames', back_populates='color', uselist=False)
