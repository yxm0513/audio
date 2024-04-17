import numpy as np

# PCM 文件路径
pcm_file = "output.pcm"

# PCM 文件参数
sample_rate = 44100  # 假设采样率为 44100 Hz
channels = 2  # 假设声道数为 2
sample_width = 2  # 假设每个样本的位深度为 16 位

# 读取 PCM 文件
with open(pcm_file, "rb") as f:
    # 读取所有的原始 PCM 数据
    pcm_data = np.frombuffer(f.read(), dtype=np.int16)

# 计算音频时长
duration = len(pcm_data) / (sample_rate * channels)

print("采样率 (Hz):", sample_rate)
print("声道数:", channels)
print("位深度 (字节):", sample_width)
print("音频时长 (秒):", duration)

