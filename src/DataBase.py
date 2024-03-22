from sqlalchemy import create_engine
from BaseUser import Base
from sqlalchemy.orm import sessionmaker


class DataBase:
    def __init__(self, db_url):
        self.__engine = create_engine(db_url, echo=False)
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
        if self.find(model, expressions):
            obj = self.__session.query(model).filter(expressions).all()[0]
            self.__session.delete(obj)
            return
        print("THERE IS NO SUCH OBJECT IN THE DATABASE")

    def get_object(self, model, expressions):
        if self.find(model, expressions):
            obj = self.__session.query(model).filter(expressions).all()[0]
            return obj
        print("THERE IS NO SUCH OBJECT IN THE DATABASE")
        return None

    def commit(self):
        self.__session.commit()
