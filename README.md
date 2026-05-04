# API algoritmo de pose (BlazePose)
---
Este repositorio contiene una API que recibe un video, el cual es procesado con BlazePose. Como resultado, se devuelve la información de cada frame con las posiciones de los tres keypoints correspondientes al pie, proporcionados por BlazePose. Para obtener más información sobre BlazePose, haga clic [aquí](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker).

![Demostración visual output](Video-demo-BlazePose.gif)

---

## Rol en la arquitectura

Este microservicio es una **dependencia obligatoria** tanto para la versión local (`neuro-error-testing`) como para la versión productiva (`mcp-vision`). Ambos componentes realizan una llamada HTTP a esta API para obtener las posiciones de los pies antes de ejecutar el análisis de errores.

```
┌────────────────────────┐         POST /process-video         ┌──────────────────┐
│  neuro-error-testing   │ ──────── localhost:5000 ───────────► │                  │
│  (versión local C++)   │                                      │   pose API       │
└────────────────────────┘                                      │   (este repo)    │
                                                                │   Puerto 5000    │
┌────────────────────────┐   blazepose-api:5000 (red Docker)    │                  │
│  mcp-vision            │ ────────────────────────────────────► │                  │
│  (versión producción)  │                                      │                  │
└────────────────────────┘                                      └──────────────────┘
```

> [!IMPORTANT]
> **Este microservicio debe estar corriendo ANTES de ejecutar cualquiera de los dos componentes de análisis.** Sin esta API levantada, el procesamiento fallará al intentar obtener los datos de pose.

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
    },

    // Máscaras de segmentación (si segmentation_mode está activo)
    'left_mask': base64_png,   // Máscara ROI del pie izquierdo
    'left_roi': [x, y, w, h],
    'right_mask': base64_png,  // Máscara ROI del pie derecho
    'right_roi': [x, y, w, h]
}
```
---

## Cómo levantar este microservicio

### Opción 1: Ejecución local (para desarrollo / uso con `neuro-error-testing`)

> [!NOTE]
> Se requiere **Python 3.11** y las dependencias listadas en `requirements.txt`.

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar la API:**
   ```bash
   cd src
   uvicorn api:app --host 0.0.0.0 --port 5000
   ```

3. La API quedará disponible en `http://localhost:5000`. Ahora puedes ejecutar `neuro-error-testing` que se conecta a `localhost:5000`.

### Opción 2: Docker (para uso con `mcp-vision` en producción)

1. **Construir la imagen:**
   ```bash
   docker build -t blazepose-api .
   ```

2. **Ejecutar en la red Docker compartida con `mcp-vision`:**
   ```bash
   docker run -d --name blazepose-api --network <nombre-red-docker> -p 5000:5000 blazepose-api
   ```

   > [!IMPORTANT]
   > El contenedor **debe llamarse `blazepose-api`** porque `mcp-vision` se conecta internamente a `http://blazepose-api:5000/process-video` usando el nombre del contenedor como hostname dentro de la red Docker.

3. **Para Docker en desarrollo local** (sin red compartida):
   ```bash
   docker run -d --name blazepose-api -p 5000:5000 blazepose-api
   ```

---

## Resumen de puertos y nombres

| Contexto | URL de conexión | Quién se conecta |
|---|---|---|
| Local (sin Docker) | `http://localhost:5000/process-video` | `neuro-error-testing` |
| Docker (red compartida) | `http://blazepose-api:5000/process-video` | `mcp-vision` |