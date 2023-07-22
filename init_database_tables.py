from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError


def init_db():
    """
    Initialize the database by creating tables based on the defined models.
    Steps to take:
    1. Define the  database connection details below.
    2. Import models you want to create in the database.
    3. Run script.
    """

    # Import the models that you want to Initialize in the database
    from model import Model

    # Database connection details
    user = ""
    password = ""
    host = ""
    port = ""
    database_name = ""

    # Create a SQLAlchemy base class
    Base = declarative_base()

    # Create the database engine
    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{database_name}',
        echo=True
    )

    # Create a scoped session
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

    # Set the query property of the base class to use the session
    Base.query = db_session.query_property()

    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully.")
    except SQLAlchemyError as e:
        print("Error creating database tables:", str(e))

    finally:
        db_session.close()


if __name__ == '__main__':
    init_db()
