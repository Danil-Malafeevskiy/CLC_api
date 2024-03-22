import os

ORIGINS = os.environ.get("ORIGINS", "http://127.0.0.1:3000,http://localhost:3000").split(
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

SECRET_KEY = "05e28ef3b5c76387b2aeb35fdd0121409d86484f42bd1d65093ea76532e657ed"

ACCESS_TOKEN_EXPIRE_MINUTES = 30
