<details markdown='1'><summary>系统信息</summary>

### 系统信息
- `date` - 显示当前日期和时间。
- `cal` - 显示本月的日历。
- `uptime` - 显示当前的运行时间。
- `w` - 显示谁当前在线。
- `whoami` - 显示当前登录用户。
- `finger <用户>` - 显示有关用户的信息。
- `uname -a` - 显示内核信息。
- `cat /proc/cpuinfo` - 显示 CPU 信息。
- `cat /proc/meminfo` - 显示内存信息。
- `man <命令>` - 显示命令的手册。
- `df` - 显示磁盘使用情况。加上 `-h` 以显示更友好的值。
- `du` - 显示目录空间使用情况。
- `du -hsx * | sort -rh | head -10` - 以人类可读的形式显示目录，按从大到小的顺序排序，总结文件夹大小并显示前 10 个位置。
- `free` - 显示内存和交换空间的使用情况。
- `whereis <应用>` - 显示应用可能的位置。使用 `-b` 查找二进制文件，`-m` 查找手册部分，`-s` 查找源代码。
- `which <应用>` - 显示默认运行的应用程序。
- `lsb_release -a` - 显示发行版信息，`-r` 显示版本号，`-c` 显示代号。
- `cat /etc/os-release` - 显示发行版信息。
- `hostnamectl` - 显示操作系统版本。
- `uname -a` - 显示内核架构。
- `cat /proc/version` - 显示发行版信息。

</details>

---

<details markdown='1'><summary>文件命令</summary>

### 文件命令
- `ls -F` - 显示每个条目后面的指示符，斜杠表示文件夹，星号表示可执行文件，@符号表示别名。
- `ls -lah` - 将文件大小转换为更友好的表示法。
- `ls -t` - 按时间排序。
- `ls -m` - 以逗号分隔。
- `ls -R` - 递归列出。
- `pwd` - 显示当前目录。
- `mkdir` - 创建目录。
- `rm` - 删除文件。
- `rm -r` - 删除目录。
- `rm -f` - 强制删除。
- `cp` - 复制文件。
- `cp -r` - 复制目录。
- `mv` - 移动文件。
- `ln -s` - 创建符号链接。
- `ln -s python_script.py /usr/bin/command` - 创建一个用户命令，执行 Python 脚本，并在系统中被全局识别。
- `touch <文件>` - 创建文件。
- `cat > 文件` - 创建文件，你可以写一些内容保存在该文件中，然后按 Ctrl+D 保存。
- `cat <文件>` - 显示文件内容。
- `cat -n <文件>` - 显示带有行号的文件内容。
- `more` - 逐行显示文件内容。
- `less` - 显示文件内容并允许使用上下箭头在行之间移动。
- `head` - 显示文件的前 10 行。
- `tail` - 显示文件的最后 10 行。
- `tail -f` - 持续显示文件的最后 10 行，跟踪变化。
- `tail -n 15 -f access.log` - 显示并跟踪日志文件的最后 15 行的变化。
- `tail -f access.log | grep 127.0.0.1` - 在访问日志文件中显示并跟踪特定值（在此示例中为 IP 127.0.0.1）的变化。
- `watch tail -n 15 access.log` - 显示日志文件的最后 15 行，并每 2 秒更新输出。
- `watch -n 10 tail -n 15 access.log` - 每 10 秒显示并跟踪最后 15 行的变化。
- `wc` - 计算行数、单词数和字符数。
- `wc -l <文件名>` - 计算文件中的行数。
- `tr` - 在不需要手动进行多个更改的情况下操作文本，类似于 Word 文档中的查找和替换功能。`tr [原始字符串] [要替换的字符串] < 输入文件.txt > 输出文件.txt`
- `sed` - 通常用于从文本中搜索和替换特定的字符串模式。与tr不同，sed可以搜索和替换更具体的字符串，而不仅仅是转换文本中的所有字符。`sed 's/要查找的模式/要替换的模式/g' 输入文件.txt`
    sed -i 's/“/<font color="red">“/g' /storage/emulated/0/Text/*.html
    sed -i 's/”/”<\/font>/g' /storage/emulated/0/Text/*.html
    
- `cut` - 根据分隔符切割，提取指定的部分（列）。
- `cut -d ' ' -f1,3,6 access.log` - 分隔符是空格，显示从第1到第3列的内容。
- `cut -d ' ' -f3 access.log | sort | uniq -c` - 按第3列列出，去重、按字母顺序排序，并计算每个值的数量。
- `nl` - 显示行号，在使用head和tail命令之前很有用。
- `|` - 管道，连接两个或多个命令，例如：`grep 关键词 access.log | head -n 5`

</details>

---

<details markdown='1'><summary>文件权限</summary>

### 文件权限
`chmod <八进制> <文件>` - 将文件的权限更改为八进制数，可以分别为用户、组和其他用户添加：

- 4 - 读取（r）
- 2 - 写入（w）
- 1 - 执行（x）

例如，`chmod 777 文件` 表示为文件提供了对所有用户的读取、写入和执行权限。

</details>

---

<details markdown='1'><summary>压缩</summary>

### 压缩
- `tar cf <文件.tar> <文件>` - 创建一个名为file.tar的tar文件，其中包含指定的文件。
- `tar xf <文件.tar>` - 从file.tar中提取文件。
- `tar czf <文件.tar.gz>` - 创建一个带有Gzip压缩的tar文件。
- `tar xzf <文件.tar.gz>` - 使用Gzip解压缩tar文件。
- `tar cjf <文件.tar.bz2>` - 创建一个带有Bzip2压缩的tar文件。
- `tar xjf <文件.tar.bz2>` - 使用Bzip2解压缩tar文件。
- `gzip <文件>` - 压缩文件并将其重命名为file.gz。
- `gzip -d <文件.gz>` - 将file.gz解压缩为原始文件。
- `7zr a -t7z <存档.7z> /文件夹/` - 从文件夹创建7z存档。您还可以指定文件。
- `7zr a -tzip <存档.zip> /文件夹/` - 从文件夹创建zip存档。您还可以指定文件。
- `7zr e 文件.7z` - 提取7z文件。
- `unrar e 文件.rar </路径>` - 将rar文件提取到指定路径。
- `unrar x 文件.rar` - 提取带有其原始目录结构的rar文件。
- `rar a 文件.rar /文件夹/` - 从文件夹创建rar文件。

</details>

---

<details markdown='1'><summary>搜索和查找命令</summary>

### 搜索和查找命令：
- `grep <模式> <文件>` - 在文件中搜索模式。 `-A NUM` 或 `--after-context=NUM` 会打印匹配行后的NUM行文本。 `-B NUM` 或 `--before-context=NUM` 会打印匹配行前的NUM行文本。
- `grep -r <模式> <目录>` - 在目录中递归搜索模式。
- `<命令> | grep <模式>` - 在命令的输出中搜索模式。
- `locate <文件>` - 查找文件的所有实例。
- `find </路径/> -iname 模式.扩展名` - 在指定路径中搜索具有特定模式和扩展名的文件。 `-type f` 表示文件，`-type d` 表示目录。
- `find </路径/> | grep '单词'` - 在指定路径中搜索文件名中的单词。
- `grep 单词 /路径/文件` - 在文件中搜索单词。
- Midnight Commander有搜索文件和文本的选项。运行mc并按下Alt + Shift +？以打开搜索窗口。

</details>

---

<details markdown='1'><summary>进程管理</summary>

### 进程管理：
- `ps` - 显示你的活动进程。
- `top` - 显示所有运行中的进程。
- `htop` - 控制台进程管理器，你需要安装它。你会喜欢它的。
- `kill <进程ID>` - 终止进程ID为pid的进程。
- `killall <进程名>` - 终止所有名称为name的进程。
- `bg` - 列出/恢复已停止或在后台运行的作业。
- `fg` - 将最近的作业移到前台。

</details>

---

<details markdown='1'><summary>网络</summary>

### 网络：
- `ping <主机>` - 对主机进行ping测试并输出结果。
- `whois <域名>` - 获取域名的whois信息。
- `dig <域名>` - 获取域名的DNS信息。
- `dig -x <主机>` - 反向查找主机。
- `wget <文件>` - 下载文件。
- `wget -c <文件>` - 继续一个已经停止的下载。
- `sudo lsof -i -P -n | grep LISTEN` - 检查开放的端口。
- `sudo netstat -tulpn | grep LISTEN` - 检查开放的端口。
- `sudo ss -tulpn | grep LISTEN` - 检查开放的端口。
- `sudo lsof -i:22` - 检查特定端口，例如22端口。
- `sudo nmap -sTU -O IP-地址` - 检查开放的端口。

</details>

---

<details markdown='1'><summary>SSH远程</summary>

### SSH远程：
- `ssh user@host -p 8022` - 连接到主机，使用用户名user，在8022端口上。
- `ssh-copy-id user@host` - 将你的密钥添加到主机的用户，以启用基于密钥的或无密码登录。

</details>

---

<details markdown='1'><summary>安装</summary>

### 安装

从源代码安装：

```bash
./configure
make
make install
```

从文件安装：

Debian系统（使用`.deb`包）：
```bash
dpkg -i <pkg.deb>  # 安装软件包
```

使用`apt`工具安装依赖（如果有的话）：
```bash
apt install -f
```

RPM系统（使用`.rpm`包）：
```bash
rpm -Uvh <pkg.rpm>  # 安装软件包
```

</details>

---

<details markdown='1'><summary>快捷键</summary>

### 快捷键：
- `Ctrl+C` - 终止当前命令。
- `Ctrl+Z` - 暂停当前命令，使用`fg`在前台恢复或使用`bg`在后台恢复。
- `Ctrl+D` - 注销当前会话，类似于`exit`。
- `Ctrl+W` - 删除当前行的一个单词。
- `Ctrl+U` - 删除整行。
- `Ctrl+R` - 输入以调出最近的命令。
- `!!` - 重复上一条命令。
- `&&` 或 `;` - 用于链接多个命令。
- `/` - 在行末尾单独使用时，用于连接多行。
- `|` - 将一个命令/程序/进程的输出发送到另一个命令/程序/进程进行进一步处理。
- `exit` - 注销当前会话。

</details>

---

<details markdown='1'><summary>GitHub使用</summary>

### GitHub 使用
我主要用它来下载一些脚本并保持其最新状态。

- `git pull <http://some_repo/code.git /opt/code` - 下载/更新本地仓库到最新的提交。

如果你有很多本地仓库，比如在你的 Kali 机器上，并且想要保持它们全部最新，你可以使用 gitup。这个工具是用于一次性更新多个 git 仓库的。你可以在 Debian 上通过 `apt install gitup` 安装它。然后只需运行：

- `gitup /opt/` - 更新位于 /opt 文件夹下的所有 GitHub 仓库。你可以按文件夹或递归方式执行。你还可以为仓库创建书签，比如 `gitup --add ~/repos` 如果你添加了很多仓库，比如 `--add ~/repos/foo ~/repos/bar ~/repos/baz`，你只需使用 `gitup` 命令来更新所有书签而无需指定每个文件夹。

</details>

---

<details markdown='1'><summary>Python脚本的运行</summary>

### Python 脚本的运行很简单。

- `python script.py` - 使用默认的 Python 版本运行 Python 脚本。
- `python2.7 script.py` - 使用指定版本运行 Python 脚本。

要检查你的 Python 版本，只需键入 `python -V`。

在 Kali Linux 中，默认的 Python 版本设置为 3，但一些仍然有效的脚本是用 Python 2 编写的。有时，当我从 GitHub 拉取脚本并为该脚本创建系统别名，以便被系统识别为系统命令时，由于默认的 Python 版本，它会执行错误，例如 golismero。

创建基于脚本的系统命令：`ln -s ${PWD}/golismero.py /usr/bin/golismero`。

现在系统识别 `golismero` 命令，我可以在任何位置运行它。

Python 文件的头部定义了 shebang：`#!/usr/bin/env python`，因此它将作为 Python 3 执行。你可以将其更改为 `#!/usr/bin/env python2.7` 并保存，但你需要记住每次拉取和更新时都要更改。为了避免这个问题，创建一个 shell 脚本，例如：`golismero.sh`，并添加以下内容：

```bash
#!/bin/sh
python2.7 /opt/golismero/golismero.py
```

将其设为可执行：`chmod u+x golismero.sh`，并创建链接：`ln -s /opt/golismero.sh /usr/bin/golismero`。

你还可以全局更改 Python 版本：

```bash
sudo update-alternatives --config python
```

但我不建议这样做。

</details>

---

<details markdown='1'><summary>图像转换和优化</summary>

### 图像转换和优化
批量图像文件转换：

- `mogrify -quality 80% *.jpg` - 将所有 jpg 文件的质量更改为 80%。
- `mogrify -format jpg *.png` - 将所有 png 文件转换为 jpg 文件。
- `mogrify -format jpg -path ./new_folder *.png` - 将所有 png 文件转换为 jpg 文件并保存在 new_folder 中。
- `mogrify -format jpg -resize 50% -path ./new_folder *.png` - 将所有 png 文件转换为 jpg 文件，将它们缩小50%并保存在 new_folder 中。
- `mogrify -quality 85 -format jpg *.png && rm *.png` - 将位于同一文件夹中的所有 png 文件转换为 jpg 文件，将 jpg 文件质量更改为 85%，并在转换后删除源 png 文件。

</details>

---

<details markdown='1'><summary>清理网站数据库日志</summary>

### 清理网站数据库日志

1. 列出所有 MySQL 或 MariaDB 的二进制日志：
    ```bash
    sudo ls -al /var/log/mysql/
    ```
    输出将显示日志列表。例如，最后一个可能是 `mariadb-bin.002345`。

2. 登录到数据库：
    ```bash
    sudo mysql -u root -p
    ```

3. 删除到最后一个日志：
    ```sql
    PURGE BINARY LOGS TO 'mariadb-bin.002345';
    ```
    或者，你也可以使用时间：
    ```sql
    PURGE BINARY LOGS BEFORE '2021-10-01 22:00:00';
    ```

4. 值得设置日志过期时间。在数据库配置文件 `my.cnf` 中，更改以下行的值：
    ```
    expire_logs_days = 5
    ```

这将设置日志的过期时间为 5 天。

</details>

---

<details markdown='1'><summary>清理日志和备份</summary>

### 清理日志和备份

删除所有已压缩的日志文件：
```bash
sudo find /var/log/* -name "*.gz" -exec rm -f {} \;
```
该命令查找所有已压缩的日志文件并删除它们。在“搜索”部分中，我描述了 `find` 命令，现在你可以在实际案例中看到它的使用。

- `-name "FILE-TO-FIND"` - 文件模式。
- `-exec rm -rf {} \;` - 删除所有与文件模式匹配的文件。

另一个示例是查找 `.bak` 文件并在用户确认后删除它们：
```bash
find . -type f -name "*.bak" -exec rm -i {} \;
```

删除备份文件夹中 15 天前的文件：
```bash
find /home/user/backup/* -mtime +15 -exec rm {} \;
```

</details>

---
