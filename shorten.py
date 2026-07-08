#!/usr/bin/env python3
"""
py-url-shortener — 短链接生成器
支持：TinyURL、TinyURL API、本地映射表
"""
import argparse
import json
import os
import random
import string
import urllib.request
import urllib.parse


# 本地映射表文件
DATA_FILE = os.path.expanduser("~/.py-url-shortener.json")


def load_db():
    """加载本地映射表"""
    if os.path.isfile(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_db(data):
    """保存本地映射表"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def generate_code(length: int = 6) -> str:
    """生成随机短码"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def shorten_tinyurl(url: str) -> str:
    """使用 TinyURL API 生成短链接"""
    api_url = f"https://tinyurl.com/api-create.php?url={urllib.parse.quote(url)}"
    try:
        with urllib.request.urlopen(api_url, timeout=10) as response:
            return response.read().decode()
    except Exception as e:
        return f"❌ API 错误: {e}"


def shorten_local(url: str, code: str = None) -> str:
    """使用本地映射表生成短链接"""
    data = load_db()

    # 检查是否已存在
    for c, original in data.items():
        if original == url:
            return f"http://s.local/{c}"

    # 生成新码
    if not code:
        code = generate_code()
        while code in data:
            code = generate_code()

    data[code] = url
    save_db(data)
    return f"http://s.local/{code}"


def resolve_local(code: str) -> str:
    """解析本地短链接"""
    data = load_db()
    return data.get(code, None)


def list_local():
    """列出所有本地短链接"""
    data = load_db()
    if not data:
        return "❌ 暂无本地短链接"
    lines = ["本地短链接列表:", "-" * 40]
    for code, original in data.items():
        lines.append(f"http://s.local/{code} → {original}")
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="短链接生成器")
    parser.add_argument("url", nargs="?", help="要缩短的 URL")
    parser.add_argument("-c", "--code", help="自定义短码")
    parser.add_argument("-l", "--list", action="store_true", help="列出本地短链接")
    parser.add_argument("-r", "--resolve", metavar="CODE", help="解析短链接")
    args = parser.parse_args()

    if args.list:
        print(list_local())
    elif args.resolve:
        result = resolve_local(args.resolve)
        if result:
            print(f"→ {result}")
        else:
            print("❌ 短码不存在")
    elif args.url:
        # 优先尝试 TinyURL
        result = shorten_tinyurl(args.url)
        if result.startswith("http"):
            print(result)
        else:
            # 失败则使用本地
            print(f"API 失败，使用本地: {shorten_local(args.url, args.code)}")
    else:
        parser.print_help()