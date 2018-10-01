import psycopg2

class ConnectionFactory:
    @staticmethod
    def get_connection():
        return psycopg2.connect("dbname='chreader' user='chreader' host='localhost' password='chreader'")