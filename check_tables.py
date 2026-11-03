import psycopg2


def check_tables():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="xo",
        user="postgres",
        password=13184243
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_type = 'BASE TABLE';
    """)

    tables = cursor.fetchall()

    print("Таблицы в базе данных:")

    if tables:
        for table in tables:
            print(table[0])
    else:
        print("Таблиц нет.")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    check_tables()