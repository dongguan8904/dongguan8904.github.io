# 确保文件编码为 UTF-8
输入路径 = '/storage/emulated/0/Documents/黄金太阳中英/黄金太阳.md'

# 使用 UTF-8 编码读取文件
with open(输入路径, 'r', encoding='utf-8') as 文件:
    内容 = 文件.read()

# 打印内容以检查是否正确读取
print(内容)

# 对文本内容进行其他处理
# 根据自定义分隔符分割文本
段落列表 = 内容.split('￥')

# 创建多个txt文件，每个文件包含一个段落
for 索引, 段落 in enumerate(段落列表):
    # 构造输出文件名，例如 GS_1.txt, GS_2.txt, ...
    输出文件名 = f'/storage/emulated/0/Documents/黄金太阳中英/GS_{索引 + 1}.md'

    # 写入当前段落内容到输出文件
    with open(输出文件名, 'w', encoding='utf-8') as 输出文件:
        输出文件.write(段落.strip())

print("拆分完成！")
