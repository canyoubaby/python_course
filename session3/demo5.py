import base64

def demo_python2():
    original_str = 'Hieu dep zai'
    encode_str = base64.b64encode(original_str)
    decode_str = base64.b64decode(encode_str)
    print(original_str)
    print(encode_str)
    print(decode_str)