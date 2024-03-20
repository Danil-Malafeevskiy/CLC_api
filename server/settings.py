import os

ORIGINS = os.environ.get("ORIGINS", "http://127.0.0.1:80,http://localhost:80").split(
    ","
)

PG_USER = os.environ.get("PG_USER", "postgres")
PG_PASSWORD = os.environ.get("PG_PASSWORD", "password")
PG_HOST = os.environ.get("PG_HOST", "py-gpn-pg")
PG_PORT = os.environ.get("PG_PORT", "5432")
PG_DB = os.environ.get("PG_DB", "backend")
DATABASE_URL = (
    f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
)
ENABLE_SQLALCHEMY_LOGGING = (
    os.environ.get("ENABLE_SQLALCHEMY_LOGGING", "False").lower() == "true"
)