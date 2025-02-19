from PIL import Image
import io
from fastapi import UploadFile, File

async def deconstruct(pindgris: str, new_image: UploadFile = File(...)):
    #File inputstream
    content = await new_image.read()
    #convert inputstream to PIL.Image
    meta_data = Image.open(io.BytesIO(content))
    
    #extract Exif datapoints
    exifdata = meta_data.getexif()

    '''
    for tag_id, data in exifdata.items():
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes into string if needed
        if isinstance(data, bytes):
            try:
                data = data.decode()
            except UnicodeDecodeError:
                data = "Binary data not readable as String"

        print(f"{tag}: {data}")
    '''
    