# 需要安装python3,pip3
1. sudo apt install python3 pip3
# 使用pip3安装deepl-cli,国内需要在后面加上清华源链接,增加下载速度
2. pip3 install deepl-cli -i https://pypi.tuna.tsinghua.edu.cn/simple\n
# 为deepl设置环境变量,在zshrc最后添加环境变量
3. export PATH="$HOME/.local/bin:$PATH"\n
# 创建一个文件夹,将几百行文本拆分为按照顺序的每行一个文本
```bash
# 读取输入文件
with open('input.txt', 'r') as file:
    lines = file.readlines()

# 创建100个txt文件，每个文件包含一行内容
for i, line in enumerate(lines):
    # 构造输出文件名，例如output_1.txt, output_2.txt, ...
    output_filename = f'output_{i + 1}.txt'

    # 写入当前行内容到输出文件
    with open(output_filename, 'w') as output_file:
        output_file.write(line.strip())

print("拆分完成！")
```
4. python3 拆分.py
# 使用shell脚本遍历文本并进行翻译,授予执行权限
```bash
#!/bin/bash

target_language="zh"  # 目标语言代码，例如 'zh' 表示中文
output_folder="output_files"  # 输出文件夹，用于保存翻译后的文本文件

# 确保输出文件夹存在，如果不存在则创建
mkdir -p "$output_folder"

# 创建一个单独的输出文件
output_file="$output_folder/translated_output.txt"

# 遍历所有以 "output_" 开头的文本文件，按照自然顺序排序
for input_file in $(ls -1v output_*.txt); do
    if [ -e "$input_file" ]; then
        # 使用 Deepl 命令行工具进行翻译，并追加到输出文件
        deepl -f "$input_file" --to "$target_language" >> "$output_file"

        echo "翻译完成：$input_file -> $output_file"
    fi
done

echo "所有文件翻译完成！"
```
5. chmod +x 翻译.sh
