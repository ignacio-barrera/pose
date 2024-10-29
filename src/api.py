from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
from video_processor import process_video

app = FastAPI()

class VideoRequest(BaseModel):
    video_url: str
    test_mode: bool = False
    segmentation_mode: bool = False

@app.post("/process-video")
async def process_video_endpoint(request: VideoRequest):
    video_url = request.video_url
    test_mode = request.test_mode
    segmentation_mode = request.segmentation_mode
    
    frames_info = process_video(video_url, test_mode, segmentation_mode)
    return {"status": "success", "frames_info": frames_info}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)