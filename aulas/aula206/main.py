# PyMySQL - um cliente MySQL feito em Python Puro
 # Doc: https://pymysql.readthedocs.io/en/latest/
 # Pypy: https://pypi.org/project/pymysql/
 # GitHub: https://github.com/PyMySQL/PyMySQL
import os

import pymysql
import dotenv

TABLE_NAME = 'pessoas'

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
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            '  `id` INT NOT NULL AUTO_INCREMENT,'
            '  `nome` VARCHAR(45) NOT NULL,'
            '  `idade` INT NOT NULL,'
            '  PRIMARY KEY (`id`))'
            
        )

        # CUIDADO: ISSO LIMPA A TABELA E APAGA TODOS OS DADOS
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        connection.commit()

    with connection.cursor() as cursor:
        sql = f'INSERT INTO {TABLE_NAME} (`nome`, `idade`) VALUES (%s, %s) '
        data = ('Lucas', 30)
            
        result = cursor.execute(sql, data)
        print(result)
    connection.commit()

