def take_pic():
    import subprocess

    subprocess.run(['fswebcam','server/database/image_upload/picture.jpg'])