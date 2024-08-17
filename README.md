## Instalar
sudo apt update
sudo apt upgrade

sudo apt install build-essential cmake git libgtk-3-dev libboost-all-dev
sudo apt install libjpeg-dev libpng-dev libtiff-dev
sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt install libxvidcore-dev libx264-dev
sudo apt install libatlas-base-dev gfortran
sudo apt install python3-dev python3-pip

pip install opencv-python
pip install flask

## Para correr
python3 pose.py

python3 api.py

curl -X POST http://localhost:5000/process-video -H "Content-Type: application/json" -d '{"video_url": "https://mcp-wildsense.s3.us-east-2.amazonaws.com/videos/7/2024-03-15/11_28_22-player9.mp4"}'

Video Francisco
{
    "video_url": "https://mcp-wildsense.s3.us-east-2.amazonaws.com/videos/7/2024-03-15/11_28_22-player9.mp4"
}

Video Fabian
{
    "video_url": "https://mcp-wildsense.s3.us-east-2.amazonaws.com/videos/7/2024-01-30/11_07_17-player1.mp4"
}
