import os
from databases import Database
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create a database instance
database = Database(DATABASE_URL)

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

