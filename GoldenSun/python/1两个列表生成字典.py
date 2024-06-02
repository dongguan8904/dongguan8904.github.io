# 输入列表
键=["Djinn","Venus","Flint","Granite","Quartz","Vine","Sap","Ground","Bane","Mars","Forge","Fever","Corona","Scorch","Ember","Flash","Torch","Jupiter","Gust","Breeze","Zephyr","Smog","Kite","Squall","Luff","Mercury","Fizz","Sleet","Mist","Spritz","Hail","Tonic","Dew","Summons","Venus","Ramses","Cybele","Judgment","Mars","Kirin","Tiamat","Meteor","Jupiter","Atalanta","Procne","Thor","Mercury","Nereid","Neptune","Boreas"]
值=["精灵","金星","燧石","花岗岩","石英","藤蔓","树液","地面","祸害","火星","锻造","狂热","电晕","烧灼","余烬","闪光","火炬","木星","阵风","微风","和风","烟雾","风筝","狂风","迎风","水星","嘶嘶声","雨夹雪","薄雾","喷雾","冰雹","奎宁水","露水","召唤","金星","拉美西斯","西布莉","审判","火星","麒麟","提亚马特","流星","木星","阿塔兰忒","普罗克涅","托尔","水星水星","海仙座","海王星","北风之神"]

# 检查并标记重复键
已见 = set()
唯一键值对 = {}
重复键 = []

for 键值, 对应值 in zip(键, 值):
    if 键值 in 已见:
        重复键.append(键值)
    else:
        已见.add(键值)
        唯一键值对[键值] = 对应值

if 重复键:
    print(f"发现重复键: {重复键}")

# 按长度排序键值对（从长到短）
排序后的键值对 = dict(sorted(唯一键值对.items(), key=lambda item: len(item[0]), reverse=True))

# 输出生成的字典
print(排序后的键值对)
