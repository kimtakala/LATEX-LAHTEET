from config import SCHEMA_NAME


class TagRepository:

    def __init__(self, database_service) -> None:
        self.database_service = database_service

    def delete(self, source_id, tag_name):
        sql = f"""
            DELETE FROM
            {SCHEMA_NAME}.tag
            WHERE source_id = :source_id
            AND name = :tag_name
        """
        self.database_service.execute(
            sql, {"source_id": source_id, "tag_name": tag_name}
        )

    def create(self, tag):
        tag.validate()

        sql = f"""
            INSERT INTO {SCHEMA_NAME}.tag
                (source_id, name) VALUES
                (:source_id, :name)
            ON CONFLICT DO NOTHING
        """

        self.database_service.execute(
            sql,
            {
                "source_id": tag.source_id,
                "name": tag.name,
            },
        )
