# 在 ~/.zshrc 文件中添加代理配置
```bash
# 设置 HTTP 代理
export http_proxy=http://127.0.0.1:7890
export HTTP_PROXY=http://127.0.0.1:7890

# 设置 HTTPS 代理
export https_proxy=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890

# 设置 FTP 代理
export ftp_proxy=http://127.0.0.1:7890
export FTP_PROXY=http://127.0.0.1:7890

# 设置不使用代理的地址，可选
export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"

# 如果代理需要身份验证，可以在 URL 中包含用户名和密码
# export http_proxy=http://username:password@proxy-server:port
# export https_proxy=http://username:password@proxy-server:port
# export ftp_proxy=http://username:password@proxy-server:port

# 如果代理服务器使用 SOCKS 协议，可以使用 socks 配置
# export socks_proxy=socks://username:password@proxy-server:port

# 启用全局代理
# export ALL_PROXY=$http_proxy
# 或者使用 socks 代理
# export ALL_PROXY=$socks_proxy
```
