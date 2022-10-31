import mysql.connector as mysql

class conn():
    def __init__(self):
        try:
            self.conexion =  mysql.connect(
                user='root', password='', host='localhost', database='colombia', port='3306')
            print('conexion exitosa')
        except Exception as msg:
            print('Error al intentar la conexión: {0}'.format(msg))

    def get_departments(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('select * from departamento')
                departments = cursor.fetchall()
                return departments
            except Exception as msg:
                print('Error al intentar la conexión: {0}'.format(msg))