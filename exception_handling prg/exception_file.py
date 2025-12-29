import io
try:
    with open("file4.txt",'w') as fd:
        data=fd.write("hello")
except FileNotFoundError as file_err:
    print("not exist")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err)
else:
    print("else block")
finally:
    print("i am always print")
    fd.close()