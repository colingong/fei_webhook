import hashlib

def func1():
    abc_then_def = hashlib.md5()
    abc_then_def.update(b'abc')
    abc_then_def.update(b'def')

    abcdef = hashlib.md5()
    abcdef.update(b'abcdef')

    print(abc_then_def.hexdigest(), abc_then_def.digest())
    print(abcdef.hexdigest(), abcdef.digest())

if __name__ == '__main__':
    func1()
