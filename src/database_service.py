from sqlalchemy import text
from typing import Optional

from config import db


class DatabaseService:
    def fetch(self, sql: str):
        result = db.session.execute(text(sql))
        return result.mappings()

    def execute(self, sql: str, bindings: Optional[dict] = None):
        if bindings:
            db.session.execute(text(sql), bindings)
        else:
            db.session.execute(text(sql))

        db.session.commit()
