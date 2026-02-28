import psutil
import time
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def get_system_metrics():
    """دالة لجمع بيانات النظام."""
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=0.5),
        "memory_usage": psutil.virtual_memory()._asdict(),
        "disk_usage": psutil.disk_usage('/')._asdict(),
        "timestamp": time.time()
    }

@app.route('/')
def index():
    """عرض صفحة الواجهة الرسومية (Dashboard)."""
    return render_template('index.html')

@app.route('/api/metrics')
def api_metrics():
    """نقطة نهاية (API) لتقديم البيانات بصيغة JSON."""
    return jsonify(get_system_metrics())

if __name__ == "__main__":
    PORT = 5000
    print(f"Web Dashboard running at http://0.0.0.0:{PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=False)
