import sqlite3

def create_tables():
    conn = sqlite3.connect('vehicles.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS ValidVehicle')
    cursor.execute('DROP TABLE IF EXISTS BannedVehicle')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ValidVehicle (
            plate_number TEXT PRIMARY KEY,
            state TEXT,
            vehicle_type TEXT,
            vehicle_color TEXT,
            vehicle_make TEXT,
            vehicle_model TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BannedVehicle (
            plate_number TEXT PRIMARY KEY,
            state TEXT,
            vehicle_type TEXT,
            vehicle_color TEXT,
            vehicle_make TEXT,
            vehicle_model TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("database created!")