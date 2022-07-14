def take_pic():
    from asyncio import subprocess
    import subprocess

    subprocess.run(['fswebcam','../database/image_upload/picture.jpg'])