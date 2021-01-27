from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        dog = firstname.replace(" ", "+")
        scraped_url = f"https://www.google.com/search?q=%22{dog}%22&start=1&num=100"
        #scraped_url = 'https://www.google.com/search?q=%22' + dog + '%22&start=1&number=100'
        print(scraped_url)
        h = {
        "accept-language":"en-US;q=0.8,en;q=0.7",
         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
         }
        response = requests.get(scraped_url, headers=h)
        #print(response)
        #response = requests.get(scraped_url)
        html = BeautifulSoup(response.text)
        div = html.find_all("span", class_="aCOpRe")
        #print(div)
        r = []
        for i in div:
            i = str(i)
            i = i.replace("""<span class="aCOpRe"><span>""", "").replace("""<span class="aCOpRe"><span class="f">""", "").replace("</em>", "").replace("<em>", "").replace("—", "").replace("</span><span>", "").replace("</span></span>", "")
            #r.append(i)
            #print(firstname)
            firstname = str(firstname)
            if firstname in i:
                print(i)
                r.append(i)
        internet_presence = r
        return render_template('index.html', internet_presence=internet_presence)
    else:
        return render_template('index.html')
        
if __name__ == "__main__":
	app.run()
