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

<details markdown='1'><summary>（4）在 debian系统中文化</summary>

如果 `locales-all` 包太大，你可以只生成所需的中文语言环境而不安装整个包。下面是具体步骤：

1. **安装必需的包**：

    ```sh
    sudo apt update
    sudo apt install locales
    ```

2. **配置语言环境**：

    编辑 `/etc/locale.gen` 文件：

    ```sh
    sudo nano /etc/locale.gen
    ```

    找到并取消注释以下行：

    ```
    zh_CN.UTF-8 UTF-8
    ```

    保存并退出。

3. **生成语言环境**：

    运行以下命令生成语言环境：

    ```sh
    sudo locale-gen
    ```

4. **设置系统默认语言**：影响所有用户

    编辑 `/etc/default/locale` 文件，添加或修改以下行：

    ```sh
    sudo nano /etc/default/locale
    ```

    添加以下内容：

    ```sh
    LANG="zh_CN.UTF-8"
    LANGUAGE="zh_CN:zh"
    LC_ALL="zh_CN.UTF-8"
    ```

5. **配置用户环境**：影响当前用户

    在用户的 home 目录下编辑或创建 `.bashrc` 文件，添加以下行：

    ```sh
    nano ~/.bashrc
    ```

    添加以下内容：

    ```sh
    export LANG=zh_CN.UTF-8
    export LANGUAGE=zh_CN:zh
    export LC_ALL=zh_CN.UTF-8
    ```

    保存并退出后，运行以下命令立即应用更改：

    ```sh
    source ~/.bashrc
    ```

6. **重启系统或重新启动终端会话**：

    完成以上步骤后，重启系统或重新启动终端会话，你的Debian终端应该能够正确显示中文了。

通过这种方式，你只会生成和使用所需的语言环境，而不会安装整个 `locales-all` 包，从而节省存储空间。

</details>

----

<details markdown='1'><summary>（5）Termux如何安装Debian系统</summary>

# Termux如何安装Debian系统(图形界面＋中文化＋音讯＋一键启动指令稿)

这篇文章介绍如何用Termux的proot-distro工具，手动建立中文化、支援PulseAudio音讯、桌面环境为XFCE4的Debian系统，不需要root权限。文末再附上一键启动的指令稿。

选用Debian的好处是比Ubuntu稳定，套件格式跟Ubuntu相近，并且没有Snap干扰(需要systemd，Termux不支援)。

如果您不想手动安装，请改用 社群制作的指令稿自动安装。

## 前置条件

要跑Debian手机需要至少4GB RAM，图形界面至少6GB。

储存空间需准备10GB。

我的装置：小米Poco F1, Lineage OS 20 (Android 13)

安装 Termux

安装 Termux X11

启用GPU硬体加速Termux以virglrenderer达成GPU 3D硬体加速

## 安装Debian最小档案系统

这里的最小档案系统指的是proot-distro开发者提供的rootfs，没有要用debootstrap制作啦。

安装Proot-distro和PulseAudio
```bash
pkg update
termux-setup-storage
pkg install proot-distro pulseaudio vim
```
安装Proot Debian
```bash
proot-distro install debian
```
登入Debian。--user参数表示登入指定帐户，目前是root。--shared-tmp则是将Termux的tmp目录挂载至proot内部以共享X伺服器资源。
```bash
proot-distro login debian --user root --shared-tmp
```
登入后先安装sudo、vim、Firefox浏览器
```bash
apt update
apt install sudo vim firefox-esr
```
要退出Proot系统，请输入exit登出。

## 更换Debian映射站台

此为选择性步骤。更改映射站，加快套件下载速度。

详细用法参考 SourcesList - Debian Wiki

可用的映射站台： Debian 映射站台

编辑映射站列表
vim /etc/apt/sources.list
将网址全部替换成台湾国网中心的网址（需注意版本代号，目前是bookworm）：
```bash
deb http://opensource.nchc.org.tw/debian/ bookworm main contrib non-free
deb-src http://opensource.nchc.org.tw/debian/ bookworm main contrib non-free
deb http://opensource.nchc.org.tw/debian/ bookworm-updates main
deb-src http://opensource.nchc.org.tw/debian/ bookworm-updates main
deb http://security.debian.org/debian-security bookworm/updates main contrib non-free
deb http://opensource.nchc.org.tw/debian bookworm-backports main
```
更新套件列表
```bash
apt update
```

## 建立一般使用者
#
通常情况下我们不会使用root帐户操作系统，为此需要新增一般使用者帐户，并在需要变更系统时(例如执行apt指令)加上sudo指令暂时提升权限。

修改root密码
```bash
passwd
```
新增wheel和video群组
```bash
groupadd storage
groupadd wheel
groupadd video
```
新增一般帐户"user"，并修改密码。
```bash
useradd -m -g users -G wheel,audio,video,storage -s /bin/bash user
passwd user
```
将user加入sudo群组。执行visudo指令，找到root ALL=(ALL:ALL) ALL那一行，在下一行加入以下内容：
```bash
user ALL=(ALL:ALL) ALL
```
切换一般帐户
```bash
su user
cd
```

</details>

----
