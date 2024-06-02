data = {
    "MinorOverloadCreedanth": "克里登斯号轻微超载",
    "CharringMountain": "查林山",
    "FoldSpaceDrive": "折叠空间驱动",
    "OverlordSyndat": "至高主宰辛达特",
    "AryanReinhart": "阿里安·莱因哈特",
    "Centerpoint": "中央点",
    "Taltscience": "塔尔特科学",
    "VayaconDios": "维亚康-迪奥斯",
    "LenoxPrime": "莱诺克斯主星",
    "Navigation": "导航",
    "PromarFive": "普罗马五",
    "FoldSpace": "折叠空间",
    "SpaceFold": "空间折叠",
    "Charring": "查林",
    "KiosFour": "基奥斯四",
    "Zaltules": "扎图勒斯",
    "Harmock": "哈莫克",
    "Harnett": "哈内特",
    "Kiveans": "基维安斯",
    "Lanolth": "拉诺斯",
    "Michael": "迈克尔",
    "Reliant": "依赖者",
    "Tranton": "特兰顿",
    "Zaltule": "扎图勒",
    "Argyle": "阿戈尔",
    "Autumn": "秋天",
    "Bixutl": "比克斯特尔",
    "BugOne": "错误一",
    "Crylia": "克莉亚",
    "Daeben": "戴本",
    "Darthu": "达尔苏",
    "Delton": "德尔顿",
    "Diadem": "饰冠",
    "Gureen": "古林",
    "Kaluse": "卡卢斯",
    "Keluth": "凯拉斯",
    "Kivean": "基维安",
    "Kleese": "克里斯",
    "Marken": "马肯",
    "Micene": "米塞尼",
    "Nalton": "纳尔顿",
    "Pradel": "普拉德尔",
    "Raluth": "拉鲁斯",
    "Salten": "萨尔滕",
    "Syndat": "辛达特",
    "Taalon": "塔隆",
    "Tintul": "丁图尔",
    "Betel": "贝特尔",
    "Blair": "布莱尔",
    "Brian": "布赖恩",
    "Ethan": "伊桑",
    "Human": "人类",
    "Kales": "卡勒斯",
    "Kivea": "基维亚",
    "Lenox": "莱诺克斯",
    "Mason": "梅森",
    "Prime": "主星",
    "Queex": "奎克斯",
    "Sword": "剑",
    "Vesta": "维斯塔",
    "Xatul": "萨图尔",
    "Bose": "博斯",
    "Bree": "布莉",
    "Eden": "伊甸",
    "Kios": "基奥斯",
    "ping": "响应时间",
    "Ryan": "瑞恩",
    "Talt": "塔尔特",
    "Wade": "韦德",
    "FTL": "超光速",
    "HUD": "抬头显示器",
    "KEW": "动能武器",
    "KIA": "在行动中阵亡",
    "LAV": "轻型机动车辆",
    "bug": "错误",
    "Bug": "错误"
}

# 读取文本文件
input_file_path = "银河帝国战争.txt"
output_file_path = "银河帝国战争1.txt"

with open(input_file_path, "r", encoding="utf-8") as input_file:
    english_text = input_file.read()

# 替换英文单词为中文
for english_word, chinese_translation in data.items():
    english_text = english_text.replace(english_word, chinese_translation)

# 写回文件
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(english_text)

print(f"替换完成，结果已保存到 {output_file_path} 文件中。")
