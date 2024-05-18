import whisper
model = whisper.load_model("base")

result = model.transcribe("hellothere.mp3")
print(result["text"])

