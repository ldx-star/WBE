from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        print(request.form)
        return "注册成功"


@app.route('/post/reg',methods=['POST'])
def post_reg():
    print(request.form)
    return "注册成功"


if __name__ == '__main__':
    app.run()