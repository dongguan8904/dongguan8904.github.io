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

<details markdown='1'><summary>（3）删除空行</summary>
  
# （3）删除空行

```bash
sed -i '/^[[:space:]]*$/d' GSen_3.md
```

- 更通用指令是使用`^[[:space:]]*$`来匹配仅包含空白字符的行（包括空行），并使用`d`来删除它们。

</details>

---

<details markdown='1'><summary>（4）用正则将匹配的行复制到txt文件</summary>

# （4）用正则将匹配的行复制到txt文件

要在终端使用正则表达式将匹配的行复制到 txt 文件，可以使用以下步骤：

1. **使用 `sed` 命令**

`sed` 是一种强大的文本处理工具，可用于搜索、编辑和转换文本。它可以使用正则表达式来匹配文本行。

以下是如何使用 `sed` 将匹配特定正则表达式的行复制到名为 `output.txt` 的文件的示例：

```bash
sed -n '/pattern/p' input.txt > output.txt
```

在此示例中：

* `-n` 选项告诉 `sed` 仅打印匹配模式的行。
* `/pattern/` 表示要匹配的正则表达式。
* `p` 命令打印匹配的行。
* `input.txt` 是要处理的输入文件。
* `> output.txt` 将输出重定向到名为 `output.txt` 的文件。

2. **使用 `awk` 命令**

`awk` 是一种用于处理文本和数据的文件处理语言。它可以使用正则表达式来匹配文本行。

以下是如何使用 `awk` 将匹配特定正则表达式的行复制到名为 `output.txt` 的文件的示例：

```bash
awk '/pattern/{print > "output.txt"}' input.txt
```

在此示例中：

* `/pattern/{print > "output.txt"}` 表示要执行的操作。
* `pattern` 是要匹配的正则表达式。
* `print` 命令将匹配的行打印到标准输出。
* `> "output.txt"` 将输出重定向到名为 `output.txt` 的文件。
* `input.txt` 是要处理的输入文件。

3. **使用 `grep` 命令**

`grep` 是一种用于搜索文本的命令行实用程序。它可以使用正则表达式来匹配文本行。

但是，`grep` 本身不会将输出复制到文件。您可以将 `grep` 的输出重定向到文件，然后再使用 `sed` 或 `awk` 来提取匹配的行。

以下是如何使用 `grep`、`sed` 和 `awk` 将匹配特定正则表达式的行复制到名为 `output.txt` 的文件的示例：

```bash
grep -l 'pattern' input.txt | xargs -I{} sed -n '/{pattern}/p' {} > output.txt
```

或者：

```bash
grep -l 'pattern' input.txt | xargs -I{} awk '/{pattern}/{print > "output.txt"}' {}
```

在此示例中：

* `grep -l 'pattern' input.txt` 使用 `grep` 搜索包含模式 `pattern` 的行，并仅打印包含匹配行的文件的文件名。
* `xargs -I{} sed -n '/{pattern}/p' {}` 将 `grep` 的输出传递给 `sed`，并替换 `{}` 为每个文件名。
* `sed -n '/{pattern}/p' {}` 使用 `sed` 提取每个文件中匹配模式 `pattern` 的行。
* `> output.txt` 将输出重定向到名为 `output.txt` 的文件。

请注意，这些只是一些示例，您可能需要根据自己的特定需求修改命令。

以下是一些其他注意事项：

* 确保您使用的正则表达式语法正确。您可以使用 [https://regex101.com/](https://regex101.com/) 等在线工具来测试您的正则表达式。
* 如果要匹配多行，可以使用多行正则表达式。
* 如果要从多个文件中提取匹配的行，可以使用通配符或 `find` 命令来标识要处理的文件。

</details>

---
