import os
from logging.config import fileConfig
from alembic import context
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()

# Alembic Config object, which provides access to the values within the .ini file
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Get the application name from the environment variable
app_name = os.getenv("APP_NAME", "core")  # Default to "core" if not set
print(f"APP_NAME: {app_name}")  # Debug için ekleyin
# Set the migration directory based on the application name
script_location = f"src/{app_name}/migrations"
print(f"Script Location: {script_location}")  # Debug için ekley
config.set_main_option("script_location", script_location)

# Set the database URL from the environment variable
DATABASE_URL = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Üst dizini Python modül yoluna ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import your SQLAlchemy Base and models
from monorepo.core.database import Base

# Set the target metadata for autogenerate support
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = config.attributes.get('connection', None)

    if connectable is None:
        from sqlalchemy import create_engine
        connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()