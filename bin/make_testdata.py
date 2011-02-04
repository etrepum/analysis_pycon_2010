#!/usr/bin/env python
import sys
import random
import sqlite3

def main():
    db = sqlite3.connect(sys.argv[1])
    cur = db.cursor()
    COLS = 'timestamp', 'user_id', 'bucket', 'dollars'
    cur.execute('CREATE TABLE testdata(' +
                ','.join(COLS) + ')')
    EPOCH = 1262322000
    for i in xrange(1000000):
        bucket = random.randrange(2)
        row = [
            EPOCH + random.randrange(14 * 86400),
            (0,10000)[bucket] + random.randrange(10000),
            ('control','test')[bucket],
            random.randrange(10 * (1 + bucket)),
        ]
        cur.execute('INSERT INTO testdata VALUES(?,?,?,?)',
                    row)
    db.commit()

if __name__ == '__main__':
    main()
