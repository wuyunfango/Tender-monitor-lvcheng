import requests
import hashlib
import os

url = "https://lczc.gtcloud.cn"

response = requests.get(url)
html = response.text

# 用 hash 判断是否变化
new_hash = hashlib.md5(html.encode()).hexdigest()

# 读取旧记录
if os.path.exists("last_hash.txt"):
    with open("last_hash.txt", "r") as f:
        old_hash = f.read()
else:
    old_hash = ""

# 判断是否更新
if new_hash != old_hash:
    print("🚨 新内容更新了！")

    # 保存新状态
    with open("last_hash.txt", "w") as f:
        f.write(new_hash)
else:
    print("没有更新")
