#from google.cloud import storage
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from PIL.ExifTags import TAGS
import pillow_heif
import io
from image_manipulator import deconstruct

# Enable HEIC support
pillow_heif.register_heif_opener()

image_manipulator = deconstruct()

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.post("/upload")
async def upload_image(pindgris: str, new_image: UploadFile = File(...)) :
    
    image_manipulator(pindgris, new_image)
        
    return {"filename": new_image.filename, "imageDate": exifdata.get(306)}