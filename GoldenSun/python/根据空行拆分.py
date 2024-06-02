# 读取输入文件
with open('黄金太阳1.txt', 'r', encoding='utf-8') as 文件:
    内容 = 文件.read()

# 根据空行分割文本
段落列表 = 内容.split('\n\n')

# 创建多个txt文件，每个文件包含一个段落
for 索引, 段落 in enumerate(段落列表):
    # 构造输出文件名，例如output_1.txt, output_2.txt, ...
    输出文件名 = f'GoldenSun1_{索引 + 1}.txt'

    # 写入当前段落内容到输出文件
    with open(输出文件名, 'w', encoding='utf-8') as 输出文件:
        输出文件.write(段落.strip())

print("拆分完成！")