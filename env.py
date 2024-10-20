# env.py inside the alembic directory
import os
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Import your config file
from config import settings  # Replace with your config module

# this is the Alembic Config object, which provides access to the values within the .ini file
config = context.config

# Override the sqlalchemy.url from your configuration
config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if context.is_offline_mode():
    connectable = config.get_main_option("sqlalchemy.url")
else:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )
