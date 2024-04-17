from pydub import AudioSegment

# 读取 MP3 文件
mp3_file = "input.mp3"
audio = AudioSegment.from_mp3(mp3_file)

# 将 MP3 文件转换为 PCM 格式
pcm_data = audio.raw_data

# 保存为 PCM 文件
pcm_file = "output.pcm"
with open(pcm_file, "wb") as f:
    f.write(pcm_data)

