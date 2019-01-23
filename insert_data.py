from google.cloud import bigquery

from gbq_setting import DATASET_REF, BIGQUERY_CLIENT, DATASET_ID, TEST_TABLE_ID


def insert_gbq_data():
    table_ref = DATASET_REF.table(TEST_TABLE_ID)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job_config.autodetect = True
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND

    with open('assets/test_table_assets.json', 'rb') as source_file:
        job = BIGQUERY_CLIENT.load_table_from_file(
            source_file,
            table_ref,
            location='asia-northeast1',
            job_config=job_config)

    job.result()

    print('Loaded {} rows into {}:{}.'.format(
        job.output_rows, DATASET_ID, TEST_TABLE_ID))


if __name__ == '__main__':
    insert_gbq_data()
