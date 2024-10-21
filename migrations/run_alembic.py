from alembic.config import Config
from alembic import command
from dotenv import load_dotenv
import os

# Load environment variables from .env file (optional)
load_dotenv()

# Create an Alembic configuration object
alembic_cfg = Config("alembic.ini")

# Get the DATABASE_URL from environment variables and set it in the Alembic configuration
DATABASE_URL = os.getenv("DB_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set!")
alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)

# Run the Alembic command (e.g., revision, upgrade, downgrade)
command.revision(alembic_cfg, autogenerate=True, message="")
