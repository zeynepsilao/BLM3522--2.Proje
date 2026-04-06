import base64
import json
from google.cloud import firestore
import functions_framework

db = firestore.Client(project="soc-dashboard-project", database="soc-logs")

@functions_framework.cloud_event
def process_log(cloud_event):
    """Pub/Sub'dan gelen veriyi yakalar ve Firestore'a yazar."""
    
    pubsub_message = base64.b64decode(cloud_event.data["message"]["data"]).decode('utf-8')
    log_data = json.loads(pubsub_message)
    
    print(f"SOC Logu Isleniyor: {log_data.get('event', 'Bilinmeyen Olay')}")
    
    try:
        db.collection('logs').add(log_data)
        print("Veritabanina basariyla kaydedildi.")
    except Exception as e:
        print(f"Hata olustu: {e}")
