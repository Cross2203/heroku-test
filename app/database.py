from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://test_ad7y_user:htxkY2k0BXvMNGAqFYcoY5PrCq6E1pyi@dpg-cpn28tuehbks7380omkg-a.oregon-postgres.render.com/test_ad7y"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()