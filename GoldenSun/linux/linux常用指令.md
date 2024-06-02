<details markdown='1'><summary>（1）linux用for遍历文件批量重命名</summary>

# （1）linux用for遍历文件批量重命名
在Termux中，`rename`命令可能不是默认安装的。你可以尝试使用`mv`命令来实现批量重命名后缀，具体命令如下：

```bash
for file in *.txt; do mv "$file" "${file%.txt}.md"; done
```

这个命令会将当前目录下所有以`.txt`结尾的文件的后缀改为`.md`。

</details>

---

<details markdown='1'><summary>（2）使用sed指令批量替换</summary>

# （2）使用sed指令批量替换
- 单个替换
```bash
sed -i 's/\*\*哈莫\*\*/哈莫/g' /storage/emulated/0/Documents/markor/翻译/*.md
```
- 多个替换
```bash
sed -i 's/\*\*罗宾\*\*/罗宾/g; s/\*\*杰拉德\*\*/杰拉德/g; s/\*\*伊万\*\*/伊万/g; s/\*\*米亚莉\*\*/米亚莉/g; s/\*\*萨丢罗斯\*\*/萨丢罗斯/g; s/\*\*梅娜蒂\*\*/梅娜蒂/g; s/\*\*杰斯敏\*\*/杰斯敏/g; s/\*\*加西亚\*\*/加西亚/g; s/\*\*斯库莱塔\*\*/斯库莱塔/g; s/\*\*哈梅特\*\*/哈梅特/g; s/\*\*哈莫\*\*/哈莫/g; s/\*\*柯兰\*\*/柯兰/g; s/\*\*巴比\*\*/巴比/g; s/\*\*西芭\*\*/西芭/g; s/\*\*阿莱克斯\*\*/阿莱克斯/g; s/\*\*贤者之石\*\*/贤者之石/g' /storage/emulated/0/Documents/markor/翻译/*.md
```

</details>

---
