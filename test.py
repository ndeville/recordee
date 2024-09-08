import moviepy.editor

from moviepy.editor import VideoFileClip
    
try:
    with VideoFileClip("import moviepy.editor") as video:
        duration = video.duration
    print(f"\nVideo duration: {duration:.2f} seconds")
except Exception as e:
    print(f"\nError getting video duration: {str(e)}")