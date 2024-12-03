from pathlib import Path
from sqlalchemy import text

from config import db, app, SCHEMA_NAME


def setup_db():
    # Tyhjennä skeema
    sql = f"""
        DROP SCHEMA IF EXISTS {SCHEMA_NAME} CASCADE;
        CREATE SCHEMA {SCHEMA_NAME};
    """
    db.session.execute(text(sql))

    # Luo uusi skeema tiedoston /src/schema.sql pohjalta
    path = Path(__file__).parent / "schema.sql"
    with path.open() as fp:
        sql = fp.read()
        db.session.execute(text(sql))

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
