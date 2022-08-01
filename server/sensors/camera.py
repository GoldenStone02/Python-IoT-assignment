def take_pic(numbering): # numbering allows us to save more than 1 picture in the folder. In total, there will be 6 images 
    import subprocess

    subprocess.run(['fswebcam',f'../server/database/image_upload/picture_{numbering}.jpg'])