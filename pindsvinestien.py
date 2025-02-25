#from google.cloud import storage
from fastapi import FastAPI, File, UploadFile
import pillow_heif
from image_manipulator import deconstruct

# Enable HEIC support
pillow_heif.register_heif_opener()

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.post("/upload/{pindgris}")
async def upload_image(pindgris: str, new_image: UploadFile = File(...)) :
    print(pindgris)
    print(new_image.filename)
    
    result = await deconstruct(pindgris, new_image)
    print(result)
        
    return {"filename": new_image.filename, "imageDate": result.get(306)}