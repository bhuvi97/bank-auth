import os

DB_USERNAME = os.getenv("DB_USERNAME", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "<PASSWORD>")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = "3306"
DB_NAME = os.getenv("DB_NAME", "users")

# Asynchronous database URL
SQLALCHEMY_DATABASE_URL = f"mysql+asyncmy://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:pass@localhost/mydb")

settings = Settings()