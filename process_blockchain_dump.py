import gzip
import csv
import datetime as dt
import pandas as pd


def load_blockchain():
    keys = 'id time difficulty fee_total generation guessed_miner'.split()
    rows = []
    with gzip.open('blockdata.txt.gz', 'rt') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data = {k: row[k] for k in keys}

            data['fee_total'] = int(data['fee_total'])
            data['generation'] = int(data['generation'])

            data['day'] = dt.datetime.strptime(data['time'].split()[0], '%Y-%m-%d')

            rows.append(data)
    return pd.DataFrame.from_records(rows)

if __name__ == '__main__':
    df = load_blockchain()
    df.to_csv('blockchain_data.csv', index=False)
