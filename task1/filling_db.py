#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import csv, sqlite3
from timer import Timer


def cached(func):
    cache = {}

    def new_func(x, cur, con, i, log):
        table = {'Original Crime Type Name': 'crime_type', 'Disposition': 'disposition', 'Address Type': 'address_type'}
        if i[x] not in cache:
            cache[i[x]] = len(cache) + 1
            log.write(f'[+] new record in table "{table[x]}"\n')
            func(x, cur, con, i, log)

        return cache[i[x]]

    return new_func


@cached
def insert_crime_type(col_name, cur, con, i, log):
    cur.execute(f'insert into crime_type (type) values ("{i[col_name]}");')
    con.commit()


@cached
def insert_disposition(col_name, cur, con, i, log):
    cur.execute(f'insert into disposition (code) values ("{i[col_name]}");')
    con.commit()


@cached
def insert_address_type(col_name, cur, con, i, log):
    cur.execute(f'insert into address_type (type) values ("{i[col_name]}");')
    con.commit()


def insert_crime(log, i, cur, con, id_crime_type, id_disposition, id_address_type):
    cur.execute(f'INSERT INTO Crime (Id_Crime_Type, Report_Date, Call_Date, Offense_Date, Call_Time, Call_Date_Time,'
                f' Id_Disposition, Address, City, State, Agency_Id, Id_Address_Type, Common_Location)'
                f' VALUES ({id_crime_type},"{i["Report Date"]}","{i["Call Date"]}","{i["Offense Date"]}",'
                f'"{i["Call Time"]}","{i["Call Date Time"]}",{id_disposition},"{i["Address"]}",'
                f'"{i["City"]}","{i["State"]}","{i["Agency Id"]}",{id_address_type},'
                f'"{i["Common Location"]}")')

    con.commit()
    log.write('[+] new record in table "Crime"\n')


def filling_db(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    with open("log.txt", "a") as log:
        with Timer(cur, log):
            with open('police-department-calls-for-service.csv', 'r') as fin:
                dr = csv.DictReader(fin)
                for i in dr:
                    id_crime_type = insert_crime_type('Original Crime Type Name', cur, con, i, log)
                    id_disposition = insert_disposition('Disposition', cur, con, i, log)
                    id_address_type = insert_address_type('Address Type', cur, con, i, log)

                    insert_crime(log, i, cur, con, id_crime_type, id_disposition, id_address_type)
                    # pass

                con.close()

'''
Такая проверка нужна для того, чтобы скрипт не выполнялся при импорте.
Если скрипт является главным исполняющим файлом то в __name__ запишется "__main__".
А при импорте запишется имя файла, соответственно главная функция(filling_db) не выполнится
'''
if __name__ == '__main__':
    filling_db("comment_section.db")
