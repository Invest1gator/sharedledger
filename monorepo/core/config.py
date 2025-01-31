# monorepo/core/config.py
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost/dbname")
