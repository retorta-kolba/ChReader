import psycopg2

class ChannelStorer:
    def __init__(self, conn):
        self.conn = conn

    def add_channel(self, telegram_id, channel_name, channel_title='', last_read_id=0):
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO channels (telegramid, ShortName, name, LastReadMessageId) VALUES (%s, %s, %s, %s) RETURNING id", (telegram_id, channel_name, channel_title, last_read_id))
            for i in cur:
                return i[0]
        
  
if __name__ == "__main__":       
    try:
        conn = psycopg2.connect("dbname='chreader' user='chreader' host='localhost' password='chreader'")
    except:
        print("I am unable to connect to the database")



    ChannelStorer(conn).add_channel(2, "test")
    conn.commit()