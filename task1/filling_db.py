import csv, sqlite3
from timer import Timer

con = sqlite3.connect("comment_section.db")
cur = con.cursor()


def cached(func):
    cache = {}

    def new_func(x):
        table = {'Original Crime Type Name': 'crime_type', 'Disposition': 'disposition', 'Address Type': 'address_type'}
        if i[x] not in cache:
            cache[i[x]] = len(cache) + 1
            log.write(f'[+] new record in table "{table[x]}"\n')
            func(x)

        return cache[i[x]]

    return new_func


@cached
def insert_crime_type(col_name):
    cur.execute(f'insert into crime_type (type) values ("{i[col_name]}");')
    con.commit()


@cached
def insert_disposition(col_name):
    cur.execute(f'insert into disposition (code) values ("{i[col_name]}");')
    con.commit()


@cached
def insert_address_type(col_name):
    cur.execute(f'insert into address_type (type) values ("{i[col_name]}");')
    con.commit()


def insert_crime():
    cur.execute(f'INSERT INTO Crime (Id_Crime_Type, Report_Date, Call_Date, Offense_Date, Call_Time, Call_Date_Time,'
                f' Id_Disposition, Address, City, State, Agency_Id, Id_Address_Type, Common_Location)'
                f' VALUES ({id_crime_type},"{i["Report Date"]}","{i["Call Date"]}","{i["Offense Date"]}",'
                f'"{i["Call Time"]}","{i["Call Date Time"]}",{id_disposition},"{i["Address"]}",'
                f'"{i["City"]}","{i["State"]}","{i["Agency Id"]}",{id_address_type},'
                f'"{i["Common Location"]}")')

    con.commit()
    log.write('[+] new record in table "Crime"\n')


with open("log.txt", "a") as log:
    with Timer(cur, log):
        with open('police-department-calls-for-service.csv', 'r') as fin:
            dr = csv.DictReader(fin)
            for i in dr:
                id_crime_type = insert_crime_type('Original Crime Type Name')
                id_disposition = insert_disposition('Disposition')
                id_address_type = insert_address_type('Address Type')

                insert_crime()
                # pass

            con.close()
