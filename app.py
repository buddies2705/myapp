from flask import Flask,render_template, request, jsonify
from pip._vendor import requests
from sqlalchemy.dialects.postgresql import JSON
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    prepareAndMakeRequest()
    return 'Hello World!'


@app.route('/main',methods=['GET','POST'])
def main():
    if request.method=='GET':
        return render_template("main.html")
    elif request.method=='POST':
        qbAccessToken1=request.form('accessToken1')
        qbAccessToken2=request.form('accessToken2')
        if qbAccessToken1 is not None and qbAccessToken2 is not None:
            checkFordata(qbAccessToken1,qbAccessToken2)





def checkFordata(qbaccessToken1,qbAccesToken2):
    return render_template('result.html',list)

def prepareAndMakeRequest():
    s = requests.Session()
    response=s.get('https://shop7-us.myshopify.com/admin/products.json',headers={'X-Shopify-Access-Token':'b817cda8d553fc059c8877a1f0fe9fea'})
    json_data = json.loads(response.text)
    print(s)
    print(response)



if __name__ == '__main__':
    app.run()
