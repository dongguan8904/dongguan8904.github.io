1. 安装adb工具
```
sudo pacman -S android-tools
```

2. 查看adb版本
```
adb version
```

3. 查看adb与安卓手机的连接状态
```
adb devices
```

4. adb获取手机root权限, 如果失败，重启手机，Magisk确认给予shell权限
```
adb shell
su
```

5. adb卸载手机系统流氓内置应用
```
adb shell pm uninstall --user 0 软件包名
```
- 示例：卸载搜狗输入法
```
adb shell pm uninstall --user 0 com.sohu.inputmethod.sogou.xiaomi
```

6. 停用指令disable-user
```
adb shell pm disable-user com.xiaomi.account
```
- 启用
```
adb shell pm enable com.xiaomi.account
```

7. usb安装(需要登录小米解锁usb安装权限)
```
adb install Magisk-v26.4.apk
```
