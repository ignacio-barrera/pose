# API algoritmo de pose
---
Este repositorio contiene una API que recibe un video, el cual es procesado con BlazePose. Como resultado, se devuelve la información de cada frame con las posiciones de los tres keypoints correspondientes al pie, proporcionados por BlazePose. Para obtener más información sobre BlazePose, haga clic [aquí](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker).

![Demostración visual output](Video-demo-BlazePose.gif)

---
## Entrada y salida
### Entrada
Debemos realizar una solicitud POST a la API bajo la ruta /process-video, la cual recibe tres parametros:
- string video_url: Indica la URL hacia la dirección web donde esta almacenado el video.
- bool test_mode: Activa una salida visual de los datos, un video juntos a los frames con los keypoints dibujados.
- bool segmentation_mode: Activa la generación visual de la mascara de segmentación del jugador.

### Salida
Es un `.json` con la siguiente información para **cada frame**:
```
frame_info = {
    'frame_index': frame_count, // Indica el frame
    'stepDetection': stepDetection, // Indica si detecto pisadas o no
    'stepSide': stepSide, // Indica con que pie detecto pisada

    // Diccionario con las posiciones de los keypoints del pie izquierdo
    'left_position': {
        'heel': left_heel_point,
        'foot_index': left_foot_index_point,
        'ankle': left_ankle_point,
        'center': left_center_point
    },
    // Diccionario con las posiciones de los keypoints del pie derecho
    'right_position': {
        'heel': right_heel_point,
        'foot_index': right_foot_index_point,
        'ankle': right_ankle_point,
        'center': right_center_point
    }
}
```
---
## Comandos útiles
### Para correr en Docker

docker build -t blazepose-api .
docker run --name blazepose-api -p 5000:5000 blazepose-api

### Para Docker en local
docker run -d --name blazepose-api --network local -p 5000:5000 blazepose-api