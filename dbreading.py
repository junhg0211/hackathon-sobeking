import pymysql
import json
from datetime import date

from util import get_const

def init() :
    connection = pymysql.connect(
        host=get_const('database.host'),
        password=get_const('database.password'),
        user=get_const('database.user'),
        database=get_const('database.database'),
        charset=get_const('database.charset')
    )

    cursor = connection.cursor(pymysql.cursors.DictCursor)
    return cursor, connection

def main() :
    cursor, connection = init()
    sql = "SELECT * FROM consumption;"

    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    for i in range(len(rows)):
        rows[i]['consume_at'] = rows[i]['consume_at'].strftime("%Y-%m-%d")
    FILE_NAME = "./date_data.json"
    f = open(FILE_NAME, 'w', encoding='utf-8')
    f.write(json.dumps(rows, ensure_ascii=False))
    f.close()

if __name__ == '__main__':
    main()
