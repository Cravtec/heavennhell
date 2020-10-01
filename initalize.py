from db.database import Base
from db.session import engine, session
from db.utils import bootstrap_db

if __name__ == '__main__':
    # create database
    Base.metadata.create_all(engine)
    #
    # Initialize database tables data
    bootstrap_db(session)

