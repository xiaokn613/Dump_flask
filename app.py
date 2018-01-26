from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

f = open('error_caseID.text','ab+')


@app.route('/getT')
def hello_world():
    caseId = request.args.get("caseId") 
    url = 'http://mobile-api.haodf.com/patientapi/flow_getCaseStatusAndDetail'
    mheaders={
        'Accept-Encoding': 'gzip',
        'User-Agent': 'haodf_app/1.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'Host': 'mobile-api.haodf.com'
    }
    post_data = 'n=2&s=tb&lastPostId=&userId=0&api=1.2&caseId={caseId}&caseType=flow&m=MI%205&app=p&os=android&sv=7.0&di=862033036085049&v=5.2.3&deviceToken=862033036085049&p=1&currentUserId=0'.format(caseId=caseId)
    try:
	res = requests.post(url,data=post_data,headers=headers)
        return str(res.txt)
    except:
        return str({error_caseId:caseId})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2333)
