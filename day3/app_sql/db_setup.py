from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from employee import Base

#setup database
engine = create_engine('sqlite:///employees_db.sqlite', echo= True) # create db if not exit

Base.metadata.create_all(engine) # create the tables for model classes

#setup things for transactions like CRUD operation

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
