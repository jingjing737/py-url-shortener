# py-url-shortener 🔗

URL shortener using TinyURL API with local mapping storage.

## Quick Start

```bash
# Shorten a URL
python3 shorten.py https://github.com/jingjing737

# Custom short code
python3 shorten.py https://google.com -c gg

# List all mappings
python3 shorten.py --list

# Lookup a short code
python3 shorten.py --lookup gg
```

## Storage

Mappings are saved locally in `url_mappings.json`.

## License

MIT
