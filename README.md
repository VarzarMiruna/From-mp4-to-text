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
```

Pentru ca Whisper să poată procesa fișiere video, este nevoie și de FFmpeg.

Pe Windows 10/11 se poate folosi Winget. Eu am instalat FFmpeg din PowerShell cu următoarea comandă:

```powershell
winget install --id Gyan.FFmpeg -e
```

După instalare, terminalul trebuie închis și deschis din nou.

Pentru verificare:

```powershell
ffmpeg -version
```

Dacă se afișează versiunea FFmpeg, instalarea este corectă.

## Observație despre Chocolatey și Scoop

FFmpeg se poate instala și cu Chocolatey sau Scoop:

```powershell
choco install ffmpeg
```

```powershell
scoop install ffmpeg
```

În cazul meu, aceste comenzi nu au funcționat deoarece Chocolatey și Scoop nu erau instalate pe calculator.

De aceea, pe Windows 11 am folosit varianta cu Winget:

```powershell
winget install --id Gyan.FFmpeg -e
```

## Rulare proiect

Scriptul se rulează din terminal astfel:

```powershell
python videos.py "C:\Users\Miruna\Desktop\video.mp4"
```

Exemple:

```powershell
python videos.py "C:\Users\mirudiva\Videos\15min.mp4"
```

```powershell
python videos.py "C:\Users\mirudiva\Videos\7min.mp4"
```

```powershell
python videos.py "C:\Users\mirudiva\Videos\3min.mp4"
```

Dacă fișierul există, programul va crea automat un fișier `.txt` în același folder cu videoclipul.

Exemplu:

```text
15min.mp4  ->  15min.txt
```

## Cum funcționează

Programul primește ca argument calea către un videoclip.

Apoi verifică dacă fișierul există. Dacă fișierul nu există, se afișează mesajul:

```text
Fisierul nu exista
```

Dacă fișierul există, se încarcă modelul Whisper:

```python
model = whisper.load_model("small")
```

Modelul transcrie videoclipul în limba română:

```python
result = model.transcribe(str(video_path), language="ro")
```

Textul rezultat este salvat într-un fișier `.txt` cu același nume ca videoclipul.
