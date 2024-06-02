# 批量压缩并设置密码
```bash
#!/bin/bash

# 循环处理每个文件
for file in *; do
    # 检查是文件而不是目录
    if [ -f "$file" ]; then
        # 获取文件名（不包含路径）
        filename=$(basename -- "$file")

        # 设置密码
        password="密码"

        # 创建ZIP文件，并设置密码
        zip -P "$password" "${filename%.${filename##*.}}.zip" "$file"
    fi
done
```
# 批量解压
```bash
#!/bin/bash

# 循环处理每个ZIP文件
for zip_file in *.zip; do
    # 检查是文件而不是目录
    if [ -f "$zip_file" ]; then
        # 获取文件名（不包含路径和扩展名）
        filename=$(basename -- "$zip_file" .zip)

        # 设置密码
        password="密码"

        # 解压ZIP文件，并设置密码
        unzip -P "$password" "$zip_file" -d "$filename"
    fi
done
```
# 压缩文件夹并设置密码
1. zip -er meimei_image.zip images
