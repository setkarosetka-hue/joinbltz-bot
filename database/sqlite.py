async def set_setting(name, value):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            INSERT INTO settings(name, value)
            VALUES(?, ?)
            ON CONFLICT(name)
            DO UPDATE SET value=excluded.value
            """,
            (name, value)
        )

        await db.commit()



async def get_setting(name):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            "SELECT value FROM settings WHERE name=?",
            (name,)
        )

        result = await cursor.fetchone()

        if result:
            return result[0]

        return None
