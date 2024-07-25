from playhouse.migrate import *
from models.models import db

migrator = PostgresqlMigrator(db)

with db.atomic():
    db.execute_sql("ALTER TABLE devices ALTER COLUMN password TYPE VARCHAR(100);")
