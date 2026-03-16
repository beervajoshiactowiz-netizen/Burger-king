import mysql.connector

def make_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='actowiz',
        database='burgerking_db'
    )
    return conn
def create_table(table_name):
    q=f"""
        create table if not exists {table_name} (
        id  INT PRIMARY KEY AUTO_INCREMENT,
        Outletname  VARCHAR(100)  NOT NULL,
        OutletAddress  VARCHAR(100)  NOT NULL,
        pincode int  NOT NULL,
        landmark TEXT ,
        OutletCity VARCHAR(100)  NOT NULL,
        OutletState VARCHAR(100),
        Phone  bigint,
        timings  VARCHAR(500),
        MapUrl  VARCHAR(500),
        OutletUrl VARCHAR(500)
        )
        """
    conn = make_connection()
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    conn.close()

def insert_into_db(table_name: str, data: list):

    rows = [item.model_dump() for item in data]

    # build query from first item's keys
    cols = ", ".join(rows[0].keys())
    placeholders = ", ".join(['%s'] * len(rows[0]))
    q = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    values = [tuple(row.values()) for row in rows]
    conn = make_connection()
    cursor = conn.cursor()
    cursor.executemany(q, values)
    conn.commit()