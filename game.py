
with open("hello.txt") as f:
    content = f.read()
if 'python' in content.lower():
    print("python is precent")
else:
    print("python is not precent")