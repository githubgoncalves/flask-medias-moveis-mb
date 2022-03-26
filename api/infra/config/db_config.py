import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

#file_path = os.path.abspath(os.getcwd())+"\database.db"

path = Path(__file__).resolve().parent / "database.db"
file_path = os.path.abspath(path)

class DBConnectionHandler:
    """ Sqlalchemy database connection """

    def __init__(self):
        self.__connection_string = 'sqlite:///'+file_path
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :parram - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member