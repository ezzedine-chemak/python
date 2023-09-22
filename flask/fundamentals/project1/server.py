from flask import Flask
app = Flask(__name__)
print(__name__)

print ("i am wissal from server.py")
if __name__ == "__main__" :
    print ("executiong server.py")
else :
    print ("execution test.py")