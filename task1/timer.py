import time
from datetime import datetime
from functools import reduce
import logging


class Timer:
    def __init__(self, cur):
        self.cur = cur
        self.begin = []
        self.end = []
        self.tables = ['Crime', 'crime_type', 'address_type', 'disposition']

    def __enter__(self):
        logging.info('started')

        for table in self.tables:
            self.cur.execute(f"select max(id) from {table}")
            begin_id = self.cur.fetchone()[0]
            if begin_id:
                self.begin.append(begin_id - 1)
            else:
                self.begin.append(0)

        self.start = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):

        for table in self.tables:
            self.cur.execute(f"select max(id) from {table}")
            end_id = self.cur.fetchone()[0]
            if end_id:
                self.end.append(end_id)
            else:
                self.end.append(0)

        count = reduce(lambda x, y: x + y, [v - self.begin[i] for i, v in enumerate(self.end)])

        logging.info(f'finished in {((datetime.now() - self.start).seconds) / 60} min')
        logging.info(f'num of recorded row {count}')
