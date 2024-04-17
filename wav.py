import wave

# 打开 PCM 文件
pcm_file = "output.pcm"
with wave.open(pcm_file, "rb") as wf:
    # 获取 PCM 文件的参数
    channels = wf.getnchannels()  # 声道数
    sample_width = wf.getsampwidth()  # 每个样本的位深度（字节数）
    frame_rate = wf.getframerate()  # 采样率
    total_frames = wf.getnframes()  # 总帧数

print("声道数:", channels)
print("位深度 (字节):", sample_width)
print("采样率 (Hz):", frame_rate)
print("总帧数:", total_frames)

