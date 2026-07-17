import aiosqlite


DB_NAME = "database.db"


async def create_db():

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT
        )
        """)


        await db.execute("""
        CREATE TABLE IF NOT EXISTS applications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            roblox TEXT,
            age TEXT,
            about TEXT,
            status TEXT
        )
        """)


        await db.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            name TEXT PRIMARY KEY,
            value TEXT
        )
        """)


        await db.commit()



async def add_application(
        user_id,
        roblox,
        age,
        about
):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            INSERT INTO applications
            (user_id, roblox, age, about, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user_id,
                roblox,
                age,
                about,
                "Ожидание"
            )
        )

        await db.commit()
