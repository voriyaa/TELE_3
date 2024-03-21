from sqlalchemy import create_engine
from BaseUser import Base
from sqlalchemy.orm import sessionmaker


class DataBase:
    def __init__(self, db_url):
        self.__engine = create_engine(db_url)
        self.__session = None

    def create_tables(self):
        Base.metadata.create_all(self.__engine)

    def creat_session(self):
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    def drop_tables(self):
        Base.metadata.drop_all(self.__engine)

    def query(self, model):
        return self.__session.query(model)

    def find(self, model, expressions):
        return len(self.__session.query(model).filter(expressions).all()) != 0

    def insert(self, obj):
        self.__session.add(obj)
        self.__session.commit()

    def delete(self, model, expressions):
        obj = self.__session.query(model).filter(expressions).get(1)
        self.__session.delete(obj)

    def update(self, model, expressions):
        obj = self.__session.query(model).filter(expressions).get(1)
