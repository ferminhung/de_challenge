# de_challenge

# Process
This API takes csv files ( hired_employees.csv, jobs.csv and departments.csv ) in GCP Bucket ( globant-coding-challenge/raw_files/ ), then sink in bigquery dataset globant-452412.coding_challenge_silver_stage, every table has all columns in string format, the last step is load the tables in dataset globant-452412.coding_challenge_gold_deliver, those tables are transformed to defined column type.

# Use
In browser: this url ( https://de-challenge-535074537328.us-central1.run.app/ ) trigger a cloud run app and it begins all pipelines.

In console:
for all pipelines
curl -X POST https://de-challenge-535074537328.us-central1.run.app \
 -H "Authorization: bearer $(gcloud auth print-identity-token)" \
 -H "Content-Type: application/json" \
 -d '{"action": "all" }'
for jobs pipelines
 curl -X POST https://de-challenge-535074537328.us-central1.run.app \
 -H "Authorization: bearer $(gcloud auth print-identity-token)" \
 -H "Content-Type: application/json" \
 -d '{"action": "jobs" }'
for departments pipeline
 curl -X POST https://de-challenge-535074537328.us-central1.run.app \
 -H "Authorization: bearer $(gcloud auth print-identity-token)" \
 -H "Content-Type: application/json" \
 -d '{"action": "departments" }'
for hired employees
 curl -X POST https://de-challenge-535074537328.us-central1.run.app \
 -H "Authorization: bearer $(gcloud auth print-identity-token)" \
 -H "Content-Type: application/json" \
 -d '{"action": "hired" }'
 
by default every trigering are all pipelines 

 # Visuality
 You can watch the results on https://lookerstudio.google.com/reporting/5f4fa799-6bf2-47b9-a721-119a2f9776de/page/p_rm33a2u8pd

 # for any question you can write to ferminhung@gmail.com
 
