# recon-logger

A lightweight Python script for passive HTTP header reconnaissance. Point it at a target URL and it checks for missing security headers, outdated server signatures, and CORS misconfigurations.

## What it checks

- **Missing headers** — `X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`
- **Outdated server banners** — PHP 5.x, Apache 2.2/2.4.1, nginx 1.0, IIS 6/7
- **CORS misconfigurations** — wildcard origin combined with `Access-Control-Allow-Credentials: true`
- **Raw header dump** — full response header output for manual review

## Usage

```bash
pip install requests
python recon_logger.py
```

Enter the target URL when prompted.

## Requirements

- Python 3.x
- `requests`

---

[johnnymeintel.com](https://www.johnnymeintel.com)
