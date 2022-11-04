from logging import exception
import mysql.connector as mysql

class conn():
    def __init__(self):
        try:
            self.conexion =  mysql.connect(
                user='root', password='', host='localhost', database='colombia', port='3306')
            print('conexion exitosa')
        except Exception as msg:
            print('Error al intentar la conexión: {0}'.format(msg))

    def post_Tweets(self,tweets:list()):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                for i in range(len(tweets)):
                    sql = "INSERT INTO tweet (pub_day, pub_month, pub_year, tema_d, id_city) values ({0},{1},{2},'{3}',{4})"
                    cursor.execute(sql.format(tweets[i].pub_day,tweets[i].pub_month,tweets[i].pub_year,tweets[i].tema,tweets[i].id_city))
                self.conexion.commit()
            except Exception as msg:
                print("Error al intentar guardar: {0}".format(msg))
                    
    def get_tweets(self) -> list:
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'select * from tweet')
                return cursor.fetchall()
            except exception as e:
                print(e)
                return []

    def get_cities(self) -> list:
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'select * from city')
                return cursor.fetchall()
            except exception as e:
                print(e)
                return []