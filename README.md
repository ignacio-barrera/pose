## API algoritmo de pose
---
### Para correr usar Docker

docker build -t blazepose-api .
docker run -p 5000:5000 blazepose-api

#### Para el Docker local

docker run -d --name vision-api --network test -p 3001:3001 vision-api
docker run -d --name blazepose-api-local --network test -p 5000:5000 blazepose-api-local

### Para hacer pruebas usar Postman

POST http://localhost:5000/process-video

Video Francisco {
    "video_url": "https://mcp-wildsense.s3.us-east-2.amazonaws.com/videos/7/2024-03-15/11_28_22-player9.mp4"
    https://mcp-wildsense.s3.us-east-2.amazonaws.com/videos/7/2024-03-15/11_28_22-player9.mp4
}
Video Fabian {
    "video_url": "https://mcp-wildsense.s3.us-east-2.amazonaws.com/videos/7/2024-01-30/11_07_17-player1.mp4"
    https://mcp-wildsense.s3.us-east-2.amazonaws.com/videos/7/2024-01-30/11_07_17-player1.mp4
}