from google.cloud import bigquery

from gbq_setting import BIGQUERY_CLIENT, DATASET, TEST_TABLE_ID


def create_gbq_table():
    client = BIGQUERY_CLIENT
    schema = [
        bigquery.SchemaField('name', 'STRING', mode='REQUIRED'),
        bigquery.SchemaField('money', 'INTEGER', mode='REQUIRED'),
    ]
    table_ref = DATASET.table(TEST_TABLE_ID)
    table = client.create_table(bigquery.Table(table_ref, schema=schema))

    assert table.table_id == TEST_TABLE_ID


if __name__ == '__main__':
    create_gbq_table()
