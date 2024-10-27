#!/usr/bin/python3
from flask import Flask, send_from_directory, jsonify, url_for, request
import qrcode
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'files'  # Directory where files are stored
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    # List all files in the upload folder
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        files_urls = [url_for('download_file', filename=f) for f in files]
        return jsonify(files_urls=files_urls)  # Display file URLs as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    # Download a file from the upload folder
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/generate_qr')
def generate_qr():
    # Generate the QR code for accessing the server
    try:
        url = request.url_root  # Base URL for server
        qr = qrcode.make(url)
        qr_path = os.path.join(app.config['UPLOAD_FOLDER'], 'server_qr.png')
        qr.save(qr_path)
        return send_from_directory(app.config['UPLOAD_FOLDER'], 'server_qr.png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
