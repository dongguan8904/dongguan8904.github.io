words = [
    "a",
    "adrienne",
    "alexdreland",
    "allison",
    "aquaria",
    "arcles",
    "armageddon",
    "b",
    "bailey",
    "beth",
    "bree",
    "breefullerton",
    "bresth",
    "brian",
    "brianjones",
    "bug",
    "bugone",
    "cag",
    "cap",
    "cherylrobinson",
    "com",
    "corporalburns",
    "dailypamela",
    "darren",
    "darrenkirby",
    "dawson",
    "drake",
    "ensignfullerton",
    "ethan",
    "ethanhall",
    "f",
    "fantasy",
    "foldspace",
    "ftl",
    "h",
    "harnett",
    "hedon",
    "hocklyns",
    "holbrook",
    "http",
    "hud",
    "humvees",
    "jaime",
    "jalt",
    "jalton",
    "jaltons",
    "janicewilliams",
    "jessica",
    "jessicalang",
    "jornada",
    "juanramos",
    "kalarn",
    "keith",
    "keithdavis",
    "kivean",
    "kiveanmarken",
    "kiveans",
    "kleese",
    "kristencarlyle",
    "larnell",
    "lav",
    "lawrence",
    "lawrencehenderson",
    "lightcruiserbunkerhill",
    "lori",
    "loriwright",
    "lunacity",
    "m",
    "major",
    "marken",
    "marshatrask",
    "mason",
    "michael",
    "michaelkirby",
    "michelkirby",
    "mitchell",
    "mk",
    "morgan",
    "mre",
    "mres",
    "nelson",
    "nelsons",
    "nicolefoster",
    "pamela",
    "pamelacairns",
    "phildawson",
    "phoenix",
    "pittman",
    "raven",
    "raymondl",
    "raymondlweil",
    "rg",
    "russell",
    "sacramentovalleys",
    "sanders",
    "sanjoaquin",
    "sean",
    "seanmiller",
    "sheen",
    "shirleymelvin",
    "skagern",
    "smithfield",
    "spacefold",
    "stalorsystem",
    "starstrike",
    "stehr",
    "stern",
    "streth",
    "taalon",
    "takencareof",
    "tellus",
    "tricia",
    "typeone",
    "typethrees",
    "vesta",
    "w",
    "wade",
    "wadenelson",
    "wainright",
    "weil",
    "wern",
    "whitesands",
    "williams",
    "x"
]
# 使用 lambda 函数作为 key，按照单词长度从大到小进行排序
sorted_words = sorted(words, key=lambda x: len(x), reverse=True)

# 打印结果
for word in sorted_words:
    print(word)
