## 数字签名和验签
from ecdsa import PrivateKey, hash256


e = int.from_bytes(hash256(b'my secret'), 'big') # 私钥
z = int.from_bytes(hash256(b'my message'), 'big')  # 加密的数据
print(e)
print(z)
pk = PrivateKey(e)
sig = pk.sign(z)
print(sig)
res = pk.point.verify(z, sig)
print(res)