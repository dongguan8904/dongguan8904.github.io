在给定的脚本中，并没有明确的地方设置系统代理。要在 Brave 浏览器中配置系统代理，你可能需要使用其他手段。以下是一种常见的方法：

1. **命令行选项：**
   使用编辑器打开brave-browser-nightly文本，找到以下指令：

   ```bash
   "$HERE/brave" "$@" || true
   ```

   你可以在这一行之前添加代码来设置系统代理的环境变量。例如：

   ```bash
   export http_proxy=http://your-proxy-address:your-proxy-port
   export https_proxy=http://your-proxy-address:your-proxy-port
   export all_proxy=socks5://your-proxy-address:your-proxy-port
   ```
   将 `your-proxy-address` 和 `your-proxy-port` 替换为你实际的代理服务器地址和端口。

   然后再执行启动./brave-browser-nightly的命令。
   ```bash
   chmod +x brave-browser-nightly
   ./brave-browser-nightly
   ```

