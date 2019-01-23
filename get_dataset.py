from google.cloud import bigquery

from gbq_setting import BIGQUERY_CLIENT, DATASET_REF


def get_table_content():
    table_ref = DATASET_REF.table('test_table')
    table = BIGQUERY_CLIENT.get_table(table_ref)

    print('table content ---------\n')
    print(table.schema)
    print(table.description)
    print(table.num_rows)
    print('-----------------------')


if __name__ == '__main__':
    get_table_content()
