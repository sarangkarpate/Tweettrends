import json

m = 3

print 'Encoding m = ', m, ' Value is : ', lambda m: json.dumps(m).encode('ascii')


print 'Decoding m = ', m, ' Value is : ', lambda m: json.loads(m.decode('ascii'))

m = '{"timestamp": "Thu Apr 13 20:18:21 +0000 2017", "message": "RT @Alythuh: Glad I started taking my art seriously and turned it into a career, in exchange it's taken me around the world. \ud83c\udfa8\ud83d\udcda\u2026 ", "location": [24.499305555745337, 51.746526363741566], "id": "852616970998390784", "author": "Aquafina\ud83c\udf0a"}'