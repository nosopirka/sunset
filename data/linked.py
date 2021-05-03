import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Linked(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'links'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return ' '.join(['<Linked>', self.id, self.text])