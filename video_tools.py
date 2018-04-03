import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip, concatenate_videoclips
from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task()
def concat_video_files(filename1, filename2, outfilename):
    
    with app.app_context():
        try:
            clip1 = VideoFileClip(filename1)
            clip2 = VideoFileClip(filename2)
            final_clip = concatenate_videoclips([clip1, clip2])
            final_clip.write_videofile(outfilename)
        except Exception as e:
            return 'Job Failed with Exception: {}'.format(e)
        finally:
            return {'current': 100, 'total': 100, 'status': 'Task completed!'}

@celery.task()
def invert_green_blue(image):
    return image[:, :, [0, 2, 1]]
