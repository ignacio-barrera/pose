# API algoritmo de pose
---
Este repositorio contiene una API que recibe un video, el cual es procesado con BlazePose. Como resultado, se devuelve la información de cada frame con las posiciones de los tres keypoints correspondientes al pie, proporcionados por BlazePose. Para obtener más información sobre BlazePose, haga clic [aquí](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker).

La API bajo la ruta /process-video recibe tres parametros:
- string video_url: Indica la URL hacia la dirección web donde esta almacenado el video.
- bool test_mode: Activa una salida visual de los datos, un video juntos a los frames con los keypoints dibujados.
- bool segmentation_mode: Activa la generación visual de la mascara de segmentación del jugador.

## Comandos útiles
### Para correr Docker

docker build -t blazepose-api .
docker run --name blazepose-api -p 5000:5000 blazepose-api

### Para Docker local
docker run -d --name blazepose-api --network local -p 5000:5000 blazepose-api