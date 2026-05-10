# Video Transcriber

Acest proiect primește calea către un fișier video și generează automat un fișier text cu transcrierea conținutului vorbit din videoclip.

Proiectul folosește modelul Whisper pentru speech-to-text și FFmpeg pentru procesarea fișierelor video.

## Tehnologii folosite

- Python
- OpenAI Whisper
- FFmpeg

## Instalare

Mai întâi trebuie instalate dependențele Python:

```bash
pip install -U openai-whisper

Pe Windows 10/11 se poate folosi Winget:

winget install --id Gyan.FFmpeg -e

După instalare, terminalul trebuie închis și deschis din nou.

Pentru verificare:

ffmpeg -version

Rulare proiect

Scriptul se rulează din terminal astfel:

python videos.py "C:\Users\Miruna\Desktop\video.mp4"

Dacă fișierul există, programul va crea automat un fișier .txt în același folder cu videoclipul.

Exemplu:

15min.mp4  ->  15min.txt


Cum funcționează

Programul primește ca argument calea către un videoclip.

Apoi verifică dacă fișierul există. Dacă fișierul nu există, se afișează mesajul:

Fisierul nu exista

Dacă fișierul există, se încarcă modelul Whisper:

model = whisper.load_model("small")

Modelul transcrie videoclipul în limba română:

result = model.transcribe(str(video_path), language="ro")

Textul rezultat este salvat într-un fișier .txt cu același nume ca videoclipul.