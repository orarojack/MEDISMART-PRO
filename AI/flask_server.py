from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_assistant', methods=['POST'])
def start_assistant():
    subprocess.Popen(['python', 'main.py'])
    return 'AI Assistant started.'

@app.route('/stop_assistant', methods=['POST'])
def stop_assistant():
    # Logic to stop the AI assistant (placeholder)
    return 'AI Assistant stopped.'

if __name__ == '__main__':
    app.run(debug=True)
