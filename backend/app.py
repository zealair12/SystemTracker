from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Store events in memory
events = []

@app.route('/api/hello')
def hello():
    """Simple test endpoint to verify API is working"""
    return jsonify({"message": "Hello from Flask backend!"})

@app.route('/api/events')
def get_events():
    """Endpoint to get all events and trigger generation of a new event"""
    # Run Perl script to generate a new event with full path to perl.exe
    script_path = os.path.join(os.path.dirname(__file__), 'simulate.pl')
    perl_path = "C:\\Strawberry\\perl\\bin\\perl.exe"
    result = subprocess.run([perl_path, script_path], capture_output=True, text=True)
    
    if result.returncode == 0:
        line = result.stdout.strip()
        # Parse line into components
        parts = line.split(" - ", 1)
        if len(parts) == 2:
            timestamp, msg = parts[0], parts[1]
            events.append({"time": timestamp, "message": msg})
    
    # Limit to most recent 100 events to prevent unbounded growth
    if len(events) > 100:
        events.pop(0)
    
    return jsonify({"events": events})

if __name__ == '__main__':
    app.run(port=5000, debug=True) 