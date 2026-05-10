import whisper
import sys
from pathlib import Path

def transcrie_video(video_path):
    video_path = Path(video_path)
    if not video_path.exists():
        print("Fisierul nu exista")
        return
    model = whisper.load_model("small")
    result = model.transcribe(str(video_path), language="ro")
    output_path = video_path.with_suffix(".txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print("Transcriere salvata in: ", output_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Folosire: python transcrie_video.py path/video.mp4")
    else:
        transcrie_video(sys.argv[1])