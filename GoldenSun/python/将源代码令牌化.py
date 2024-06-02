import tokenize
from io import BytesIO

code = '''
def add(a, b):
    return a + b

result = add(5, 10)
print(result)
'''

# 将代码转换为字节流
code_bytes = BytesIO(code.encode('utf-8'))

# 使用tokenize令牌化模块解析代码
tokens = tokenize.tokenize(code_bytes.readline)
for token in tokens:
    print(token)