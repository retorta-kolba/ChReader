import psycopg2

class ChannelStorer:
    def __init__(self, conn):
        self.conn = conn

    def add_channel(self, telegram_id, name):
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO channels (telegramid, name) VALUES (%s, %s) RETURNING id", (telegram_id, name))
            for i in cur:
                return i[0]
        
  
if __name__ == "__main__":       
    try:
        conn = psycopg2.connect("dbname='chreader' user='chreader' host='localhost' password='chreader'")
    except:
        print("I am unable to connect to the database")



    ChannelStorer(conn).add_channel(2, "test")
    conn.commit()