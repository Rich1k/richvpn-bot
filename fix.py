import os

# убиваем ВСЕ прокси переменные
for k in list(os.environ.keys()):
    if "proxy" in k.lower():
        os.environ.pop(k)

# жесткий сброс для httpx/telegram
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["ALL_PROXY"] = ""
os.environ["http_proxy"] = ""
os.environ["https_proxy"] = ""
os.environ["all_proxy"] = ""

print("OK - proxies cleared")