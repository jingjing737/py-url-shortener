# py-url-shortener 🔗

短链接生成器，支持 TinyURL API 和本地映射表。

## 快速开始

```bash
# 生成短链接（使用 TinyURL）
python3 shorten.py https://github.com/jingjing737

# 使用自定义短码
python3 shorten.py https://google.com -c gg

# 列出本地短链接
python3 shorten.py -l

# 解析短链接
python3 shorten.py -r abc123
```

## 参数

| 参数 | 说明 |
|------|------|
| `url` | 要缩短的 URL |
| `-c, --code` | 自定义短码 |
| `-l, --list` | 列出本地短链接 |
| `-r, --resolve` | 解析短码 |

## 特性

- ✅ TinyURL API 集成
- ✅ 本地映射表（不依赖网络）
- ✅ 自定义短码
- ✅ 零依赖（标准库实现）

## License

MIT