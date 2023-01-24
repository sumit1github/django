from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str

def encode_text(text_data):
    result= urlsafe_base64_encode(str(text_data).encode('utf-8'))
    return result

def decode_text(text_data):
    result= force_str(urlsafe_base64_decode(text_data))
    return result
