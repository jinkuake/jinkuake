import io
a = "hello"
sio = io.StringIO(a)
print(sio.getvalue())
sio.seek(1)
sio.write("s")
print(sio.getvalue())