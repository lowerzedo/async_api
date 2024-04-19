from datetime import datetime

def parse_datetime(date_string):
    return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
