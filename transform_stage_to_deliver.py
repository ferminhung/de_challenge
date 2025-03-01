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

    return results