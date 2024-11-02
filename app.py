# app.py
from flask import Flask, Response, render_template
import json
import time
import threading
from gen import message_queue, runcov

app = Flask(__name__)

def run_background_task():
    """Run the coverage task in background"""
    try:
        runcov()
    except Exception as e:
        # Add error to queue so frontend can be notified
        message_queue.put({"type": "error", "message": str(e)})

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/stream')
def stream():
    def generate():
        # Start runcov in a separate thread
        thread = threading.Thread(target=run_background_task)
        thread.daemon = True  # Thread will be terminated when main thread ends
        thread.start()
        
        while True:
            if not message_queue.empty():
                msg = message_queue.get()
                yield f"data: {json.dumps(msg)}\n\n"
            time.sleep(0.1)

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)