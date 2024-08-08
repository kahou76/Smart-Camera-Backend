import sqlite3

class LocalDB:
    def __init__(self, db_name='vehicles.db'):
        self.db_name = db_name
    
    def _connect(self):
        return sqlite3.connect(self.db_name)
    
    def add_vehicle(self, plate_number, state, vehicle_type, vehicle_color, vehicle_make, vehicle_model, table):
        with self._connect() as conn:
            cursor = conn.cursor()
            if self.is_vehicle_info_correct(plate_number, state, vehicle_type, vehicle_color, vehicle_make, vehicle_model, table):
                return False
            else:
                cursor.execute(f'''
                    INSERT INTO {table} (plate_number, state, vehicle_type, vehicle_color, vehicle_make, vehicle_model)  
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (plate_number, state, vehicle_type, vehicle_color, vehicle_make, vehicle_model))
                conn.commit()
            return True
    
    def delete_vehicle(self, plate_number, table):
        with self._connect() as conn:
            cursor = conn.cursor()
            if not self.is_vehicle_existed(plate_number, table):
                return False
            else:
                cursor.execute(f'DELETE FROM {table} WHERE plate_number = ?', (plate_number,))
                conn.commit()
                return True
            
    def is_vehicle_existed(self, plate_number, table):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
                SELECT * FROM {table} WHERE
                plate_number = ?
            ''', (plate_number,))
            return True if cursor.fetchone() else False
    
    def is_vehicle_info_correct(self, plate_number, state, vehicle_type, vehicle_color, vehicle_make, vehicle_model, table):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
                SELECT * FROM {table} WHERE
                plate_number = ? and state = ? and vehicle_type = ? and vehicle_color = ? and vehicle_make = ? and vehicle_model = ?
            ''', (plate_number, state, vehicle_type, vehicle_color, vehicle_make, vehicle_model))
            return True if cursor.fetchone() else False