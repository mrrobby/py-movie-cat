import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip, concatenate_videoclips


class VideoTools(object):
    """ Basic VideoTools Class """
    def __init__():
        pass

    @staticmethod
    def concat_video_files(filename1, filename2, outfilename):
        clip1 = VideoFileClip(filename1)
        clip2 = VideoFileClip(filename2)
        final_clip = concatenate_videoclips([clip1, clip2])
        final_clip.write_videofile(outfilename)
        return

    @staticmethod
    def invert_green_blue(image):
        return image[:, :, [0, 2, 1]]
