# from app.process import get_search_tags,get_data,prepere_data,get_data_query
from process import get_search_tags,get_data,prepere_data,get_data_query
from flask import Flask, render_template,request
app = Flask(__name__)
data=get_data()
@app.route('/')
def main_page():
    return render_template("index.html",context=get_search_tags(data))

@app.route('/results',methods=['POST','GET'])
def results_page():
    if request.method=='POST':
        tags=request.form.getlist("tags[]")
        if tags!=[]:
            return render_template("results.html",context=get_data_query(prepere_data(data),tags), selectOptions = get_search_tags(data))
        else:
            return render_template("error.html")
    else:
            return render_template("error.html")

@app.errorhandler(404)
def page_not_found(error):
    print("ERORR-404",error)
    return render_template("error.html")
