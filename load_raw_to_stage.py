def load_departments():
    from google.cloud import bigquery

    client = bigquery.Client()

    table_id = "globant-452412.coding_challenge_silver_stage.departments"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("id", "STRING"),
            bigquery.SchemaField("department", "STRING"),
        ],
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
    )
    uri = 'gs://globant-coding-challenge/raw_files/departments.csv'

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    ) 

    load_job.result()  

    destination_table = client.get_table(table_id)  
    return "Loaded {} rows.".format(destination_table.num_rows)