import mysql.connector
import time

def main():
    mydb = mysql.connector.connect(host='mydb', port='3306', user='root', password='notpassword', database='campus', auth_plugin='mysql_native_password')
    cursor = mydb.cursor()
    
    cursor.execute('SELECT name FROM events')
    f = open("lookup.yml", "w")
    f.write("version: \"3.1\"\nnlu:\n  - lookup: event  \n    examples: |\n")
    temp = []

    for event in cursor:
        event = str(event)[2:-3]
        if event not in temp:
            temp.append(event)
            f.write('      - ' + event + '\n')

    f.close()
    cursor.close()
    mydb.close()

if __name__ == '__main__':
    #time.sleep(10)
    main()
