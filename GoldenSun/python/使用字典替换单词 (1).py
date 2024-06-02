字典 = {'Bookcase 1:': '书柜 1:', 'Bookcase 2:': '书柜 2:', 'Bookcase 3:': '书柜 3:', 'Bookcase 4:': '书柜 4:', 'Bookcase 5:': '书柜 5:', 'Bookcase 6:': '书柜 6:', 'Bookcase 7:': '书柜 7:', 'Brigand 1 :': '土匪 1:', 'Brigand 2 :': '土匪 2:', 'Brigand 3 :': '土匪 3:', 'Chef 2 :': '厨师 2:', 'Dog 1 :': '狗 1:', 'Dog 2 :': '狗 2:', 'Employee 1:': '员工 1:', 'Employee 2:': '员工 2:', 'Employee 3:': '员工 3:', 'Gladiator1:': '角斗士 1:', 'Gladiator2:': '角斗士 2:', 'Guard 1 :': '守卫 1:', 'Guard 2 :': '守卫 2:', 'Guard 3 :': '守卫 3:', 'Guard 4 :': '守卫 4:', 'Guide 1 :': '向导 1:', 'Guide 2 :': '向导 2:', 'Guqard 2 :': '守卫 2:', 'Head Chef:': '主厨:', 'Healer 1 :': '治疗师 1:', 'Healer 1:': '治疗师 1:', 'Healer 2 :': '治疗师 2:', 'Healer 3 :': '治疗师 3:', 'Innkeeper1:': '旅店老板 1:', 'Innkeeper2:': '旅店老板 2:', 'Man 1 :': '男子 1:', 'Man 2 :': '男子 2:', 'Man 3 :': '男子 3:', 'Message 1 :': '信息 1:', 'Message 2 :': '信息 2:', 'Message 3 :': ' 信息 3:', 'Message 4 :': '信息 4:', 'Message 5 :': '信息 5:', 'Message 6 :': '信息 6:', 'Oarsman 1 :': '桨手 1:', 'Oarsman 2 :': '桨手 2:', 'Oarsman 3 :': '桨手 3:', 'Oarsman 4 :': '桨手 4:', 'Oarsman 5 :': '桨手 5:', 'Oarsman 6 :': '桨手 6:', 'Oarsman 7 :': '桨手 7:', 'Oarsman 8 :': '桨手 8:', 'Owner 1 :': '老板 1:', 'Owner 2 :': '老板 2:', 'Passenger1:': '乘客 1:', 'Scholar 1 :': '学者 1:', 'Scholar 2 :': '学者 2:', 'Scholar 3 :': '学者 3:', 'Shelf 1 :': '书架 1:', 'Shelf 2 :': '书架 2:', 'Shelf 3 :': '书架 3:', 'Signpost 1:': '路标 1:', 'Signpost 2:': '路标 2:', 'Soldier 1 :': '士兵 1:', 'Soldier 2 :': '士兵 2:', 'Soldier 3 :': '士兵 3:', 'Soldier 4 :': '士兵 4:', 'Stage 1 :': '舞台 1:', 'Stage 2 :': '舞台 2:', 'Stage 3 :': '舞台 3:', 'Stage 4 :': '舞台 4:', 'Stage 5 :': '舞台 5:', 'Stage 6 :': '舞台 6:', 'Thief 1 :': '小偷 1:', 'Thief 2 :': '小偷 2:', 'Tree 1 :': '树 1:', 'Tree 2 :': '树 2:', 'Tree 3 :': '树 3:', 'Wardrobe 1:': '衣柜 1:', 'Worker 1 :': '工人 1:', 'Worker 2 :': '工人 2:', 'colors:': '颜色:'}

# 读取文本文件
输入文件路径 = "GoldenSun-1-GameScript2.txt"
输出文件路径 = "GoldenSun-1-GameScript2.txt"

with open(输入文件路径, "r", encoding="utf-8") as 输入文件:
    英语文本 = 输入文件.read()

# 替换英文单词为中文
for 英语单词, 中文词语 in 字典.items():
    英语文本 = 英语文本.replace(英语单词, 中文词语)

# 写回文件
with open(输出文件路径, "w", encoding="utf-8") as 输出文本:
    输出文本.write(英语文本)

print(f"替换完成，结果已保存到 {输出文件路径} 文件中。")
