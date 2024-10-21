from alembic.config import Config
from alembic import command

# Path to your alembic.ini configuration file
alembic_cfg = Config("alembic.ini")

# Run the alembic upgrade command
command.upgrade(alembic_cfg, "head")
