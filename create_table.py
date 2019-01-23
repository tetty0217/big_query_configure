from google.cloud import bigquery

from gbq_setting import BIGQUERY_CLIENT, DATASET


def create_gbq_table():
    client = BIGQUERY_CLIENT
    schema = [
        bigquery.SchemaField('full_name', 'STRING', mode='REQUIRED'),
        bigquery.SchemaField('age', 'INTEGER', mode='REQUIRED'),
    ]
    table_ref = DATASET.table('tetty_table')
    table = client.create_table(bigquery.Table(table_ref, schema=schema))

    assert table.table_id == 'tetty_table'


if __name__ == '__main__':
    create_gbq_table()
