linux系统安装Android工具包
sudo pacman -S android-tools
验证安装
fastboot --version


下载Magisk.apk软件，放在手机目录
下载手机对应的TWRP文件，有zip和img两个文件，img文件放在电脑，zip文件放在手机目录。


检查设备连接
手机进入开发者模式，打开USB调试模式
1. adb指令需要手机正常开机并进入桌面才能使用，检测是否连接成功，返回一窜数字就是成功连接了。
    adb devices
2. fastboot指令需谷歌手机重启并长按音量下键打开fastboot模式，此时输入下面指令，返回一窜数字成功连接。
    fastboot devices
3. 刷入 TWRP 镜像，谷歌手机，我没有成功刷入
    fastboot flash recovery <twrp_image.img>
    重新启动设备到 TWRP 恢复模式
    fastboot reboot recovery

    只能用临时打开一次，下次需要再重新连接电脑使用。
    fastboot boot <twrp_image.img>
    进入twrp页面后就可以安装magisk.apk，手机就可以root了。
    重启手机


刷写步骤：
1. 进入 Fastboot 模式：
    将设备进入 Fastboot 模式。通常，你可以通过按住设备上的特定硬件按键（如音量键和电源键）或使用 Fastboot 命令来完成。
2. 连接设备到计算机：
    使用 USB 数据线将设备连接到计算机。在 Fastboot 模式下，运行以下命令验证设备是否正确连接：
    fastboot devices
    应该看到设备的序列号，表示设备已正确连接。
3. 刷写引导加载程序（如果需要）：
    如果你需要刷写引导加载程序，请使用以下命令之一：
    fastboot flash bootloader bootloader.img
    替换 bootloader.img 为你的引导加载程序文件的实际名称。
4. 刷写系统分区：
    使用以下命令刷写系统分区：
    fastboot flash system system.img
    替换 system.img 为你的系统分区文件的实际名称。
5. 刷写其他分区（可选）：
    根据需要，刷写其他分区，例如 boot.img、dtbo.img、vbmeta.img、vendor.img。
    fastboot flash boot boot.img
    fastboot flash dtbo dtbo.img
    fastboot flash vbmeta vbmeta.img
    fastboot flash vendor vendor.img
6. 重启设备：
    使用以下命令重启设备：
    fastboot reboot
7. 等待设备启动：
    等待设备启动，刷写的系统生效。


电脑终端输入指令，手机进入fastboot模式
adb reboot bootloader
