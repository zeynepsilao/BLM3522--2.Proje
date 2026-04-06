import base64
import json
from google.cloud import firestore
import functions_framework

# Firestore istemcisini globalde tanımlıyoruz (Performans için)
db = firestore.Client(project="soc-dashboard-project", database="soc-logs")

@functions_framework.cloud_event
def process_log(cloud_event):
    """Pub/Sub'dan gelen veriyi yakalar ve Firestore'a yazar."""
    
    # Pub/Sub mesajını yakala ve çöz
    pubsub_message = base64.b64decode(cloud_event.data["message"]["data"]).decode('utf-8')
    log_data = json.loads(pubsub_message)
    
    # Terminale log bas (Monitoring için)
    print(f"SOC Logu Isleniyor: {log_data.get('event', 'Bilinmeyen Olay')}")
    
    # Firestore'daki 'logs' koleksiyonuna ekle
    try:
        db.collection('logs').add(log_data)
        print("Veritabanina basariyla kaydedildi.")
    except Exception as e:
        print(f"Hata olustu: {e}")
