"""
curl -X POST https://raw-to-stage-535074537328.us-central1.run.app \
 -H "Authorization: bearer $(gcloud auth print-identity-token)" \
 -H "Content-Type: application/json" \
 -d '{"action": "all" }'
"""
import functions_framework
from load_raw_to_stage import load_departments, load_jobs, load_hired_employees
from transform_stage_to_deliver import departments_to_deliver, jobs_to_deliver, hired_employees_to_deliver

@functions_framework.http
def begin_challenge(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args
    
    if request_json and 'action' in request_json:
        action = request_json['action']
    elif request_args and 'action' in request_args:
        action = request_args['action']
    else:
        action = 'all'
    
    if action == "departments":
        dep_logs = load_departments()

        return [action,
        dep_logs,
        departments_to_deliver()] 

    elif action == "jobs":
        job_logs = load_jobs()

        return [action,
        job_logs,
        jobs_to_deliver()]

    elif action == "hired":
        hir_logs = load_hired_employees()

        return [action,
        hir_logs,
        hired_employees_to_deliver()]

    else:
        dep_logs = load_departments()
        job_logs = load_jobs()
        hir_logs = load_hired_employees()

        return [action,
        dep_logs, job_logs, hir_logs,
        departments_to_deliver(), 
        jobs_to_deliver(), 
        hired_employees_to_deliver()]
