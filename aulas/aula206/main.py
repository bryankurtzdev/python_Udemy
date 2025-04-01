# PyMySQL - um cliente MySQL feito em Python Puro
 # Doc: https://pymysql.readthedocs.io/en/latest/
 # Pypy: https://pypi.org/project/pymysql/
 # GitHub: https://github.com/PyMySQL/PyMySQL
import os

import pymysql
import dotenv

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS `pessoas` ('
            '  `id` INT NOT NULL AUTO_INCREMENT,'
            '  `nome` VARCHAR(45) NOT NULL,'
            '  `idade` INT NOT NULL,'
            '  PRIMARY KEY (`id`))'
            
        )
        connection.commit()
        print(cursor)
