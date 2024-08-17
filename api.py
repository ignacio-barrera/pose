from flask import Flask, request, jsonify
import requests
import os
import shutil

from pose import process_video  # Importa la función process_video del archivo pose.py

app = Flask(__name__)

# Ruta temporal donde se almacenará el video descargado
TEMP_VIDEO_PATH = './temp_video.mp4'

@app.route('/process-video', methods=['POST'])
def process_video_api():
    data = request.json
    video_url = data.get('video_url')
    
    if not video_url:
        return jsonify({'error': 'No video URL provided'}), 400

    try:
        # Descargar el video desde la URL de Amazon S3
        download_video(video_url, TEMP_VIDEO_PATH)

        # Procesar el video descargado
        frames_info = process_video(TEMP_VIDEO_PATH)

        # Devolver la información procesada en la respuesta
        return jsonify({'frames_info': frames_info}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Eliminar el video descargado para limpiar el espacio temporal
        if os.path.exists(TEMP_VIDEO_PATH):
            os.remove(TEMP_VIDEO_PATH)

def download_video(url, save_path):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(save_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
