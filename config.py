import os

DB_USERNAME = "admin"
DB_PASSWORD = "w=dibltr6DlBA_u$ihIz"
DB_HOST = "database-1.cdg6e6o80ngc.us-east-2.rds.amazonaws.com"
DB_PORT = "3306"
DB_NAME = "database-1"

# Asynchronous database URL
SQLALCHEMY_DATABASE_URL = f"mysql+asyncmy://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:pass@localhost/mydb")

settings = Settings()