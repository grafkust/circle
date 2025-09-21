from moviepy.video.io.VideoFileClip import VideoFileClip

"""
  Создаёт квадратное видео по центру исходника.
"""
def make_circle_video(input_path, output_path, max_duration=60):
    clip = VideoFileClip(input_path)

    if clip.duration > max_duration:
        clip = clip.subclipped(0, max_duration)

    clip = get_center(clip)

    clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        fps=60,
        threads=4,
        ffmpeg_params=[
            "-pix_fmt", "yuv420p",
            "-crf", "18",        # 18-23 = отличное качество
            "-preset", "medium", # Баланс скорости и качества
            "-movflags", "faststart"
        ]
    )
    clip.close()
    print(f"Видео-кружок готов! Сохранено в: {output_path}")

"""
  Получаем центральный кадр 240*240px
"""
def get_center(clip):
    size = min(clip.w, clip.h)
    x_center = clip.w / 2
    y_center = clip.h / 2

    clip = clip.cropped(x1=x_center - size / 2,
                        y1=y_center - size / 2,
                        x2=x_center + size / 2,
                        y2=y_center + size / 2
                        )
    clip.resized((240, 240))
    return clip