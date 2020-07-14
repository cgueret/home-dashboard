from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

app = Flask(__name__)

#BASE = "https://journeyplanner.transportforireland.ie/nta/XSLT_DM_REQUEST?language=en&std3_suggestMacro=std3_suggest&std3_commonMacro=dm&itdLPxx_contractor=&std3_contractorMacro=&includeCompleteStopSeq=1&mergeDep=1&mode=direct&name_dm=Donabate%2C+Donabate&nameInfo_dm=51026226&type_dm=any&itdDateDayMonthYear=08.11.2019&itdTime=22%3A25&&sessionID=0&requestID=0&itdLPxx_directRequest=1&coordOutputFormat=WGS84[dd.ddddd]"
BASE = "https://journeyplanner.transportforireland.ie/nta/XSLT_DM_REQUEST?language=en&std3_suggestMacro=std3_suggest&std3_commonMacro=dm&itdLPxx_contractor=&std3_contractorMacro=&includeCompleteStopSeq=1&mergeDep=1&mode=direct&name_dm=Donabate%2C+Donabate&nameInfo_dm=51026226&type_dm=any&itdDateDayMonthYear={today}&itdTime={hour}%3A{minute}&&sessionID=0&requestID=0&itdLPxx_directRequest=1&coordOutputFormat=WGS84[dd.ddddd]"
# today: 08.11.2019
# hour: 22
# minute 34

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/train")
def get_train_times():
    now = datetime.now()
    url = BASE.format(today=datetime.strftime(now, '%d.%m.%Y'), 
                    hour=datetime.strftime(now, '%H'), 
                    minute=datetime.strftime(now, '%M'))
    data = requests.get(url)
    soup = BeautifulSoup(data.content)
    times = []
    for div in soup.find_all('div'):
        if 'data-time' in div.attrs.keys():
            dst_div = list(div.find_all('div', {'class': 'std3_result-description'}))[0]
            dst = list(dst_div.strings)[1]
            time_str = '{}:{}'.format(div['data-time'][:2], div['data-time'][2:])
            times.append([time_str, dst])
    return json.dumps(times[:6])

# run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
