from google.cloud import bigquery

from gbq_setting import BIGQUERY_CLIENT, DATASET_REF, TEST_TABLE_ID


def get_gbq_table():
    table_ref = DATASET_REF.table(TEST_TABLE_ID)
    table = BIGQUERY_CLIENT.get_table(table_ref)

    print('table content ---------\n')
    print(table.schema)
    print(table.description)
    print(table.num_rows)
    print('-----------------------')


if __name__ == '__main__':
    get_gbq_table()
