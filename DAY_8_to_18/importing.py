class MyClass:
    def show(self):
        print("This is example of importing....")

num = 10

def fun():
    print("This is function")

#  current_file_name == importing.py
if __name__ == "__main__":
    obj = MyClass()
    obj.show()
    print(num)
    fun()