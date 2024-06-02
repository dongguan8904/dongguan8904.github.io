import subprocess
import os

# 获取当前目录下所有的APE文件
ape_files = [f for f in os.listdir('.') if f.endswith('.ape')]

# 循环处理每个APE文件
for file in ape_files:
    # 构建输出文件名
    output_file = file.replace('.ape', '.mp3')
    # 构建ffmpeg命令
    command = ['ffmpeg', '-i', file, '-codec:a', 'libmp3lame', '-b:a', '320k', output_file]
    # 执行命令
    subprocess.run(command)
    
"""
`subprocess` 是 Python 标准库中的一个模块，它允许你在 Python 脚本中创建新的进程，连接到其输入、输出和错误管道，并且获取返回状态码。这个模块提供了多个函数来执行外部命令，比如 `subprocess.run()`，`subprocess.Popen()` 等。

使用 `subprocess` 模块，你可以在 Python 中执行外部命令，如系统命令、Shell 命令等，并且可以通过 Python 脚本与这些外部命令进行交互。
"""