from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

f = open('error_caseID.text','ab+')


@app.route('/getT')
def hello_world():
    caseId = request.args.get("caseId") 
    url = 'http://mobile-api.haodf.com/patientapi/flow_getCaseStatusAndDetail'
    headers={
        'Accept-Encoding': 'gzip',
        'User-Agent': 'haodf_app/1.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'Host': 'mobile-api.haodf.com'
    }
    post_data = 'n=2&s=tb&lastPostId=&userId=0&api=1.2&caseId={caseId}&caseType=flow&m=MI%205&app=p&os=android&sv=7.0&di=862033036085049&v=5.2.3&deviceToken=862033036085049&p=1&currentUserId=0'.format(caseId=caseId)
    try:
	res = requests.post(url,data=post_data,headers=headers)
        return str(res.text)
    except:
        return str({"error_caseId":caseId})


@app.route('/doc')
def hello_doc():
    doc_id = request.args.get("doc_id")
    page = request.args.get("page")
    url = 'http://mobile-api.haodf.com/patientapi/doctor_getCaseListByDoctorIdNew'
    headers = {
    	'User-Agent':'haodf_app/1.0',
	'Content-Type':'application/x-www-form-urlencoded',
	'Host':'mobile-api.haodf.com',
	'Connection':'Keep-Alive',
	'Accept-Encoding':'gzip'
    }
    post_data = 'n=2&s=xm&userId=0&api=1.2&m=MI%205&app=p&os=android&sv=7.0&di=862033036085049&v=5.6.1&deviceToken=862033036085049&p=1&doctorId={doc_id}&nowPage={page}&_t=c42f4825f57f500d71a28a2fe2a16899&currentUserId=0'.format(doc_id=doc_id,page=page)
    try:
	res = requests.post(url,data=post_data,headers=headers)
	return str(res.text)
    except:
	return str({"error_caseId":doc_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2333)
