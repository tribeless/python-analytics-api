from decouple import config as decouple_config # type: ignore

DATABASE_URL = decouple_config("DATABASE_URL", default="", cast=str) 