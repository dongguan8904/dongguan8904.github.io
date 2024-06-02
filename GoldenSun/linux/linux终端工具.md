<details markdown='1'><summary>（1）pandoc文本转换</summary>

# （1）pandoc文本转换

```bash
pandoc -s 基地.epub -o 基地.txt --wrap=none
```

</details>

----

<details markdown='1'><summary>（2）ffmpeg影音处理</summary>

# （2）ffmpeg影音处理

- 无损ape转为mp3

- 这个命令将音频编码为320 kbps的MP3文件。根据需要调整比特率（例如128k, 256k, 320k）。

```bash
ffmpeg -i 2寂静山林.ape -codec:a libmp3lame -b:a 320k 2寂静山林.mp3
```

- 使用python批量执行转换

```py
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
```

- `subprocess` 是 Python 标准库中的一个模块，它允许你在 Python 脚本中创建新的进程，连接到其输入、输出和错误管道，并且获取返回状态码。这个模块提供了多个函数来执行外部命令，比如 `subprocess.run()`，`subprocess.Popen()` 等。

- 使用 `subprocess` 模块，你可以在 Python 中执行外部命令，如系统命令、Shell 命令等，并且可以通过 Python 脚本与这些外部命令进行交互。

</details>

----

<details markdown='1'><summary>（3）使用pdftk合并pdf文件</summary>

# （3）使用pdftk合并pdf文件

- 安装pdftk工具包
```bash
sudo apt install pdftk
```
- 合并名为file1.pdf和file2.pdf的两个PDF文件，并将输出保存为combined.pdf。
```bash
pdftk file1.pdf file2.pdf cat output combined.pdf
```

</details>

----

<details markdown='1'><summary>（4）使用poppler的pdftotext提取pdf文本</summary>

# （4）使用poppler的pdftotext提取pdf文本

如果PDF文件有几百页，可以使用`pdftotext`工具一次性提取整个PDF文件的文本内容。以下是在Termux中提取长PDF文件文本的详细步骤：

1. **更新和安装必要的软件包**：
   ```sh
   pkg update
   pkg upgrade
   pkg install poppler
   ```

2. **使用 `pdftotext` 提取文本**：
   ```sh
   pdftotext input.pdf output.txt
   ```
   - `input.pdf` 是你要转换的PDF文件路径。
   - `output.txt` 是输出的文本文件路径。

3. **验证输出文件**：
   ```sh
   cat output.txt
   ```
- 即使PDF文件有几百页，它也能够一次性完成文本提取。

### 主要选项：
- **默认行为**：不指定任何选项时，`pdftotext` 会智能地提取文本，保持基本的段落结构。
- **-layout**：保持原始 PDF 的布局，这会使输出的文本文件尽量模拟 PDF 的视觉布局。
- **-raw**：逐行提取文本，不进行段落和布局分析。
- **-fixed <number>**：使用固定宽度的字符网格来提取文本。

### 示例：
1. **默认提取**：
   ```sh
   pdftotext input.pdf output.txt
   ```

2. **保持布局**（非默认）：
   ```sh
   pdftotext -layout input.pdf output.txt
   ```

3. **逐行提取**：
   ```sh
   pdftotext -raw input.pdf output.txt
   ```

4. **固定宽度提取**：
   ```sh
   pdftotext -fixed 10 input.pdf output.txt
   ```

### 查看帮助：
你可以通过以下命令查看 `pdftotext` 的所有可用选项：
```sh
pdftotext -h
```

</details>

----
