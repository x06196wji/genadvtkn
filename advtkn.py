import argparse
from datetime import datetime, timedelta

def genAdvTkn(mac):
    try:
        _t = datetime.utcnow()
        _mac = int (mac, 16)
        _t = _t + timedelta(days=int(str(_mac)[-2:]))
        _tt = int(_t.year) + int(_t.month) + int(_t.day)
        _c = _mac - _tt - (int(_t.day) * int(_t.year) * (int(_t.month) * int(_t.day)) * 3 * int(_t.month))
        _key = str(_c)[-6:]
        return _key
    except Exception as e:
        return ''

