# API algoritmo de pose
---
Este repositorio contiene una API que recibe un video, el cual es procesado con BlazePose. Como resultado, se devuelve la información de cada frame con las posiciones de los tres keypoints correspondientes al pie, proporcionados por BlazePose. Para obtener más información sobre BlazePose, haga clic [aquí](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker).

## Comandos útiles
### Para correr Docker

docker build -t blazepose-api .
docker run --name blazepose-api -p 5000:5000 blazepose-api

### Para Docker local
docker run -d --name vision-api --network test -p 3001:3001 vision-api
docker run -d --name blazepose-api --network local -p 5000:5000 blazepose-api