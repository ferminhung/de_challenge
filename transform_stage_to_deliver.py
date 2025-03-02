def departments_to_deliver() -> None:
    from google.cloud import bigquery

    client = bigquery.Client()
    results = client.query_and_wait(
        """
        CREATE TABLE IF NOT EXISTS globant-452412.coding_challenge_gold_deliver.departments (
          ID INT OPTIONS (description = 'Id of the department'),
          DEPARTMENT STRING OPTIONS (description = 'Name of the department'),
          BATCH_DATE TIMESTAMP OPTIONS (description = 'Batch load date')
        );

        BEGIN TRANSACTION;

        INSERT INTO globant-452412.coding_challenge_gold_deliver.departments 
        SELECT
          CAST(SILVER.id AS INT) AS ID,
          SILVER.department AS DEPARTMENT,
          TIMESTAMP(CURRENT_TIMESTAMP()) AS BATCH_DATE
        FROM globant-452412.coding_challenge_silver_stage.departments AS SILVER;

        COMMIT TRANSACTION;
        """)  

    return "departments table finish in gold"

def jobs_to_deliver() -> None:
    from google.cloud import bigquery

    client = bigquery.Client()
    results = client.query_and_wait(
        """
        CREATE TABLE IF NOT EXISTS globant-452412.coding_challenge_gold_deliver.jobs (
          ID INT OPTIONS (description = 'Id of the job'),
          JOB STRING OPTIONS (description = 'Name of the job'),
          BATCH_DATE TIMESTAMP OPTIONS (description = 'Batch load date')
        );

        BEGIN TRANSACTION;

        INSERT INTO globant-452412.coding_challenge_gold_deliver.jobs 
        SELECT
          CAST(SILVER.id AS INT) AS ID,
          SILVER.job AS JOB,
          TIMESTAMP(CURRENT_TIMESTAMP()) AS BATCH_DATE
        FROM globant-452412.coding_challenge_silver_stage.jobs AS SILVER;

        COMMIT TRANSACTION;
        """)  

    return "jobs table finish in gold"

def hired_employees_to_deliver() -> None:
    from google.cloud import bigquery

    client = bigquery.Client()
    results = client.query_and_wait(
        """
        CREATE TABLE IF NOT EXISTS globant-452412.coding_challenge_gold_deliver.hired_employees (
          ID INT OPTIONS (description = 'Id of the employee'),
          NAME STRING OPTIONS (description = 'Name of the employee'),
          DATETIME_HIRE TIMESTAMP OPTIONS (description = 'Hire datetime in ISO format'),
          DEPARTMENT_ID INT OPTIONS (description = 'ID of the department'),
          JOB_ID INT OPTIONS (description = 'ID of the Job '),
          BATCH_DATE TIMESTAMP OPTIONS (description = 'Batch load date')
        );

        BEGIN TRANSACTION;

        INSERT INTO globant-452412.coding_challenge_gold_deliver.hired_employees 
        SELECT
          CAST(SILVER.id AS INT) AS ID,
          SILVER.name AS NAME,
          CAST(SILVER.datetime AS TIMESTAMP) AS DATETIME_HIRE,
          CAST(SILVER.department_id AS INT) AS DEPARTMENT_ID,
          CAST(SILVER.job_id AS INT) AS JOB_ID,
          TIMESTAMP(CURRENT_TIMESTAMP()) AS BATCH_DATE
        FROM globant-452412.coding_challenge_silver_stage.hired_employees AS SILVER;

        COMMIT TRANSACTION;
        """)  

    return "hired_employees table finish in gold"
