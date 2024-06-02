# 读取输入文件
with open('黄金太阳1.txt', 'r', encoding='utf-8') as 文件:
    行列表 = 文件.readlines()

# 创建100个txt文件，每个文件包含一行内容
for 索引, 行内容 in enumerate(行列表):
    # 构造输出文件名，例如output_1.txt, output_2.txt, ...
    输出文件名 = f'output_{索引 + 1}.txt'

    # 写入当前行内容到输出文件
    with open(输出文件名, 'w', encoding='utf-8') as 输出文件:
        输出文件.write(行内容.strip())

print("拆分完成！")