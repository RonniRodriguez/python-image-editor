from PIL import Image, ImageEnhance, ImageFilter 
import os 

path = './imgs' 
pathOut = '/editedImgs' 

for filename in os.listdir(path): 
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert("L").rotate(-0)
    
    factor = 1.25
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor) 
    
    factor = 1.25
    enhancer = ImageEnhance.Color(edit)
    edit = enhancer.enhance(factor) 
    
    factor = 2.0
    enhancer = ImageEnhance.Sharpness(edit) 
    edit = enhancer.enhance(factor)

    factor = 1.05
    enhancer = ImageEnhance.Brightness(edit) 
    edit = enhancer.enhance(factor) 
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
    