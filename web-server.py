from flask import Flask, render_template,jsonify,request

from pars_hh import request_hh

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(r'index.html')

@app.route("/contact")
def contact():
    return render_template(r'contact.html')


@app.route("/form", methods=['GET', 'POST'])
def form():
    developer_name="**view Леонид**"
    main_data={
        'a':"A",
        'b': "B",
        'c': "C",
    }
    context={
        'a':"A",
        'b': "B",
    }
    #контекст те даные которые мы передает из view в шаблон
    if request.method == "POST":
        text=request.form['param_two']
        print(text)
        j_hh=request_hh("Python developer")
        return jsonify({"data":j_hh['requirements']})
    else:
        param = request.args.get('param')
        print(param)
        if param:
            j_hh = request_hh("Python developer")

            return render_template(r'form_boost.html', name=developer_name,main_data=main_data, hh_data=j_hh, **context)
        return render_template(r'form_boost.html',name=developer_name,main_data=main_data,**context)

@app.route("/form_get/", methods = ['GET'])
def form_post():
    param=request.args.get('param')
    print(param)
    return render_template(r'form_boost.html')

if __name__ == "__main__":
    print('start')
    app.run(debug=True)