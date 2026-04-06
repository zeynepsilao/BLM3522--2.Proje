import time
import json
import random
from google.cloud import pubsub_v1

project_id = "soc-dashboard-project" 
topic_id = "security-logs"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def generate_soc_log():
    events = ["Brute Force Attempt", "SQL Injection", "Malware Sync", "Unauthorized SSH"]
    severities = ["Low", "Medium", "High", "Critical"]
    
    log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "event": random.choice(events),
        "source_ip": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
        "severity": random.choice(severities),
        "analyst": "Zey-SOC-Bot"
    }
    return log

print(f"Log akışı başlatıldı... Topic: {topic_id}")

while True:
    data = generate_soc_log()
    message = json.dumps(data).encode("utf-8")
    
    future = publisher.publish(topic_path, message)
    
    print(f"[{data['severity']}] Gönderilen Log: {data['event']} - IP: {data['source_ip']}")
    time.sleep(3) # 3 saniyede bir log üretir
