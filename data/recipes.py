import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase

class Recipe(SqlAlchemyBase):
    __tablename__ = 'recipes'
    recipe_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    ingredients = sqlalchemy.Column(sqlalchemy.String)
    instructions = sqlalchemy.Column(sqlalchemy.String)
    image = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
