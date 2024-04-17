import whisper

model = whisper.load_model("base")
result = model.transcribe("chinese.wav")
print(result["text"])
