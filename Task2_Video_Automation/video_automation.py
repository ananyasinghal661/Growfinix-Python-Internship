from pathlib import Path
from moviepy import VideoFileClip, TextClip, CompositeVideoClip, vfx


# Folders
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


# Text for the event promo
WATERMARK = "308 GROUP"
EVENT_TEXT = "LUXURY BIRTHDAY CELEBRATION"


def process_video(input_file, output_file):

    print(f"Processing: {input_file.name}")

    video = VideoFileClip(str(input_file))

    # Fade-in effect
    video = video.with_effects([
        vfx.FadeIn(1.5)
    ])

    width, height = video.size

    # Watermark
    watermark = TextClip(
        text=WATERMARK,
        font_size=35,
        color="white",
        stroke_color="black",
        stroke_width=2,
        duration=video.duration
    )

    watermark = watermark.with_position(
        (width - watermark.w - 30, height - watermark.h - 30)
    )

    # 3D text shadow
    shadow = TextClip(
        text=EVENT_TEXT,
        font_size=65,
        color="#4A3000",
        stroke_color="#4A3000",
        stroke_width=2,
        duration=5
    )

    shadow = shadow.with_position(
        ("center", height * 0.72 + 5)
    )

    # Golden text
    golden_text = TextClip(
        text=EVENT_TEXT,
        font_size=65,
        color="#D4AF37",
        stroke_color="#FFF2A6",
        stroke_width=2,
        duration=5
    )

    golden_text = golden_text.with_position(
        ("center", height * 0.72)
    )

    # Combine video and text
    final_video = CompositeVideoClip([
        video,
        watermark,
        shadow,
        golden_text
    ])

    # Export edited video
    final_video.write_videofile(
        str(output_file),
        codec="libx264",
        audio_codec="aac"
    )

    video.close()
    final_video.close()


# Process every MP4 file in the input folder
for video_file in INPUT_DIR.glob("*.mp4"):

    output_file = OUTPUT_DIR / f"{video_file.stem}_edited.mp4"

    process_video(video_file, output_file)


print("All videos processed successfully!")