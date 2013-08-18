chunk = bytearray("x" * 1024 * 1024)

i = 128
while chunk:
    piece = chunk[:i]
    del(chunk[:i])
