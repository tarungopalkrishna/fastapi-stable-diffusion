from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import io
import cv2
import numpy
from hugging_sd import get_image

app = FastAPI()


@app.get("/")
async def root_path():
    return {"message": "This is program to get an AI generate image. It uses huggingface stable-diffusion-2 model."}

@app.get("/images")
def generate_image(prompt: str):
    # Get the image
    image = get_image(prompt)
    open_cv_image = numpy.array(image)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    #Return the image
    res, png = cv2.imencode(".png", open_cv_image)
    return StreamingResponse(io.BytesIO(png.tobytes()), media_type="image/png")
