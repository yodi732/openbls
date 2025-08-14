# route/tool/func.py — minimal helpers to avoid import errors
import hashlib

def md5_replace(data: str) -> str:
    return hashlib.md5(data.encode("utf-8")).hexdigest()

def load_lang(key: str) -> str:
    # minimal stub
    return key

def cut_100(s: str) -> str:
    return s[:100]
