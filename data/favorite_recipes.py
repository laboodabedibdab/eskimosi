import sqlalchemy
from .db_session import SqlAlchemyBase

class FavoriteRecipe(SqlAlchemyBase):
    __tablename__ = 'favorite_recipes'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.user_id"))
    recipe_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("recipes.recipe_id"))
