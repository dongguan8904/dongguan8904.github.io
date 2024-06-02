# 原始字典
字典1={'ElementalStarChamber':'元素星室','MercuryLighthouse':'水星灯塔','FuchinFallsCave':'富钦瀑布洞穴','Tolbi-boundShip':'前往托尔比的飞船','VenusLighthouse':'维纳斯灯塔','ElementalStars':'元素星','ColosseumFinal':'斗兽场决赛','BabiLighthouse':'巴比灯塔','LamakanDesert':'拉马坎沙漠','AltmillerCave':'阿尔特米勒洞穴','ColossoFinals':'巨人总决赛','LunpaFortress':'伦帕要塞','SuhallaDesert':'苏哈拉沙漠','CrossboneIsle':'十字骨岛','KolimaForest':'科利马森林','MogallForest':'莫加尔森林','GondowanCave':'贡多湾洞穴','BilibinCave':'比利宾洞穴','SuhallaGate':'苏哈拉门','TunnelRuins':'隧道遗迹','SolSanctum':'太阳圣殿','AltinPeak':'阿尔廷峰','VaultCave':'沃特洞穴','GomaCave':'戈玛洞穴','TretTree':'特雷特树','ValeCave':'瓦莱洞穴'}
字典2={'Lighthouse':'灯塔','Elemental':'元素','Altmiller':'阿尔特米勒','Colosseum':'斗兽场','Crossbone':'十字骨','Gondowan':'贡多湾','Fortress':'要塞','Sanctum':'圣殿','Chamber':'室','Bilibin':'比利宾','Mercury':'水星','Lamakan':'拉马坎','Colosso':'巨人','Suhalla':'苏哈拉','Kolima':'科利马','Forest':'森林','Fuchin':'富钦','Mogall':'莫加尔','Desert':'沙漠','Finals':'总决赛','Tunnel':'隧道','Stars':'星','Falls':'瀑布','Altin':'阿尔廷','Vault':'沃特','Tolbi':'托尔比','bound':'捆绑','Final':'决赛','Lunpa':'伦帕','Venus':'维纳斯','Ruins':'遗迹','Star':'星','Goma':'戈玛','Cave':'洞穴','Tret':'特雷特','Tree':'树','Peak':'峰','Vale':'瓦莱','Ship':'飞船','Gate':'门','Babi':'巴比','Isle':'岛','Sol':'太阳'}

# 合并字典并检查重复键
合并字典 = {}
重复键 = []

for 字典 in [字典1, 字典2]:
    for 键, 值 in 字典.items():
        if 键 in 合并字典:
            重复键.append(键)
        合并字典[键] = 值

# 输出发现的重复键
if 重复键:
    print(f"发现重复键: {重复键}")

# 按键的长度从长到短排序合并后的字典
排序后的合并字典 = dict(sorted(合并字典.items(), key=lambda item: len(item[0]), reverse=True))

# 输出排序后的字典
print(排序后的合并字典)
