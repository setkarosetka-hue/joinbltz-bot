import aiosqlite

DB_NAME = "database.db"


async def create_db():
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS applications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username TEXT,
            age TEXT,
            about TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            name TEXT PRIMARY KEY,
            value TEXT
        )
        """)

        await db.commit()


async def add_application(user_id, username, age, about):
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            INSERT INTO applications(user_id, username, age, about)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, username, age, about)
        )

        await db.commit()


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
