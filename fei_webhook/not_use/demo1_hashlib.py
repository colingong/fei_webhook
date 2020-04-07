import hashlib, hmac

def func1():
    key = b'123456'
    raw = b'abcdef'
    sign = hmac.new(key, raw, hashlib.sha1)
    print(sign)

if __name__ == '__main__':
    func1()
