from __future__ import with_statement
import sys
import os
from alembic import context
from sqlalchemy import create_engine
from sqlalchemy import pool
from sqlalchemy.ext.declarative import declarative_base
from logging.config import fileConfig

# добавьте это:
from app import models  # импортируйте модель (Base), где описаны все таблицы
from app.database import Base  # импортируйте ваш Base

# Здесь Base.metadata будет содержать все метаданные для миграций
target_metadata = Base.metadata

# Сохранение текущей конфигурации и скрипта для дальнейшего использования
config = context.config

# Автоматическая настройка соединения с базой данных и метаданных
def run_migrations_online():
    # Настройка подключения к базе данных
    engine = create_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool
    )

    # Запуск миграций
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Вызов функции миграции
run_migrations_online()
