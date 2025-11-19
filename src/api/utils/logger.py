import datetime
import json

def log_event(event_type: str, data: dict):
    timestamp = datetime.datetime.utcnow().isoformat()
    log = {
        "time": timestamp,
        "event": event_type,
        "data": data
    }
    print(json.dumps(log))
