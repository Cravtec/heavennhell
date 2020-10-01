from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# engine = create_engine("sqlite:///heavennhell.sqlite", echo=True)
engine = create_engine("sqlite:///heavennhell.sqlite")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
