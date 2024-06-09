<details markdown='1'><summary>（1）编辑欢迎页面及一些常用指令</summary>

# （1）编辑欢迎页面及一些常用指令

```bash
vim /data/data/com.termux/files/usr/etc/motd
```
Welcome to Termux!

Docs:       https://termux.dev/docs
Donate:     https://termux.dev/donate
Community:  https://termux.dev/community

常用指令：
 - Search:  pkg search <query>
 - Install: pkg install <package>
 - Upgrade: pkg upgrade
- 列出已安装：pkg list-installed
- 卸载：apt remove 包名
- 卸载依赖：apt autoremove

订阅其他存储库：
 - Root:    pkg install root-repo
 - X11:     pkg install x11-repo

解决存储库问题请尝试：termux-change-repo

报告问题于：https://termux.dev/issues

- 显示包大小：
```bash
dpkg-query -Wf='${Installed-Size}\t${Package}\n' | sort -n | awk '{ printf "%.2f MB\t%s\n", $1/1024, $2 }'
```

- 显示总大小：
```bash
du -sh $PREFIX
```

- 显示安装日志：
```bash
cat /data/data/com.termux/files/usr/var/log/apt/history.log
```
</details>

----

<details markdown='1'><summary>（2）termux备份与还原</summary>

# （2）termux备份与还原

- 恢复包其实就是将整个Termux的资料备份起来的压缩文件。针对喜欢反复卸载Termux折腾的用户，也有必要学习如何给自己制作能快速恢复之前使用Termux环境的恢复包。
- 建立Termux备份压缩包
- 取得存储权限
```bash
termux-setup-storage
```
- 建立备份压缩包，此命令会备份Termux外部目录的资料，不包含proot-distro，并将其储存为手机内部空间的"termux-backup.tar.gz"文件。备份时间视Termux占用的空间而定，例如10GB约需要10分钟，生成的压缩包约为5GB。

```bash
tar -zcf /sdcard/termux-backup.tar.gz -C /data/data/com.termux/files ./home ./usr
```

- 没有Root权限下，只能用proot-distro backup命令另外备份proot-distro的资料成一个压缩包，需指定proot-distro的代号：

```bash
proot-distro backup --output /sdcard/debianbackup.tar.gz debian
```

- 如果有Root权限，以下版本的命令则能连proot-distro内部目录的资料一起备份成单一压缩包，无须再使用proot-distro backup命令。

```bash
pkg install tsu
sudo tar -zcf /sdcard/termux-backup.tar.gz -C /data/data/com.termux/files ./home ./usr
```

- 还原Termux备份
- 重装Termux后，还原Termux备份不需要Root权限。
- 同样先申请存储空间权限

```bash
termux-setup-storage
```

- 假设备份位于内部空间/termux-backup.tar.gz，将其复原并还原权限。此步骤执行后Termux资料会被覆盖。

```bash
tar -zxf /sdcard/termux-backup.tar.gz -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
```

- 输入exit退出Termux，重新开启APP后文件就回来了。
- 要还原另外备份的proot-distro则输入：
```bash
proot-distro restore /sdcard/debianbackup.tar.gz
```

- 延伸阅读
- Backing up - Termux Wiki: https://wiki.termux.com/wiki/Backing_up_Termux
</details>

----

<details markdown='1'><summary>（3）在 Termux中安装proot-distro再安装debian系统</summary>
 
要在 Termux 中安装 `proot-distro`，你可以按照以下步骤进行：

1. 更新 Termux 包管理器：
    ```sh
    pkg update
    ```

2. 安装 `proot-distro`：
    ```sh
    pkg install proot-distro
    ```

安装完成后，你可以使用 `proot-distro` 安装和管理不同的 Linux 发行版。例如，安装 Debian 发行版：

3. 安装 Debian 发行版：
    ```sh
    proot-distro install debian
    ```

4. 进入 Debian 发行版环境：
    ```sh
    proot-distro login debian
    ```

在进入环境后，你可以像在常规的 Debian 系统上一样操作，包括使用 `apt` 列出和管理包。

</details>

----
