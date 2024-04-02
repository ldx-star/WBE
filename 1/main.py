from flask import Flask,render_template

app = Flask(__name__)

# 创建网址 /show/info 和 函数 index 的对应关系
@app.route("/show/info")
def hello_world():
    # 默认去当前目录的templates文件中查找
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()