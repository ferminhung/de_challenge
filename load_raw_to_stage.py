def load_departments():
    from google.cloud import bigquery

    client = bigquery.Client()

    table_id = "globant-452412.coding_challenge_silver_stage.departments"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("id", "STRING"),
            bigquery.SchemaField("department", "STRING"),
        ],
        source_format=bigquery.SourceFormat.CSV,
        write_disposition='WRITE_TRUNCATE'
    )
    uri = 'gs://globant-coding-challenge/raw_files/departments.csv'

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    ) 

    load_job.result()  

    destination_table = client.get_table(table_id)  
    return "Departments Loaded {} rows.".format(destination_table.num_rows)

def load_jobs():
    from google.cloud import bigquery

    client = bigquery.Client()

    table_id = "globant-452412.coding_challenge_silver_stage.jobs"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("id", "STRING"),
            bigquery.SchemaField("job", "STRING")
        ],
        source_format=bigquery.SourceFormat.CSV,
        write_disposition='WRITE_TRUNCATE'
    )
    uri = 'gs://globant-coding-challenge/raw_files/jobs.csv'

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    ) 

    load_job.result()  

    destination_table = client.get_table(table_id)  
    return "Jobs Loaded {} rows.".format(destination_table.num_rows)

def load_hired_employees():
    from google.cloud import bigquery

    client = bigquery.Client()

    table_id = "globant-452412.coding_challenge_silver_stage.hired_employees"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("id", "STRING"),
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("datetime", "STRING"),
            bigquery.SchemaField("department_id", "STRING"),
            bigquery.SchemaField("job_id", "STRING")
        ],
        source_format=bigquery.SourceFormat.CSV,
        write_disposition='WRITE_TRUNCATE'
    )
    uri = 'gs://globant-coding-challenge/raw_files/hired_employees.csv'

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    ) 

    load_job.result()  

    destination_table = client.get_table(table_id)  
    return "EmployyesLoaded {} rows.".format(destination_table.num_rows)
