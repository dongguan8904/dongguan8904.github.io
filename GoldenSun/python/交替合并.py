# 定义文件路径
a_md_path = '/storage/emulated/0/Documents/GSz_1.md'
b_md_path = '/storage/emulated/0/Documents/GSe_1.md'
merged_md_path = '/storage/emulated/0/Documents/合并后.md'

# 读取 a.md 和 b.md 的内容
with open(a_md_path, 'r', encoding='utf-8') as 文件_a:
    a_行 = 文件_a.readlines()

with open(b_md_path, 'r', encoding='utf-8') as 文件_b:
    b_行 = 文件_b.readlines()

# 检查两个文件的行数是否相同
if len(a_行) != len(b_行):
    raise ValueError("两个文件的行数不同")

# 按行合并文件
合并行 = []
for a_line, b_line in zip(a_行, b_行):
    合并行.append(b_line.strip() + '\n')  # 添加 b.md 的一行
    合并行.append(a_line.strip() + '\n')  # 添加对应的 a.md 的一行

# 将合并后的行写入一个新文件
with open(merged_md_path, 'w', encoding='utf-8') as 合并文件:
    合并文件.writelines(合并行)

print("文件合并成功！")
