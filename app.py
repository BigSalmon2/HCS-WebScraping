from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        scraped_url = 'https://www.google.com/search?q=' + firstname + '+' + lastname
        page = requests.get(scraped_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        searchTitles = soup.find_all('div', attrs={'class': lambda e: e.startswith('BNeawe') if e else False})
        internet_presence = []
        for title in searchTitles:
            if '.com' in title.text or '.io' in title.text or '.edu' in title.text:
                internet_presence.append(title.text)
        print(internet_presence)
        return render_template('index.html', internet_presence=internet_presence)

    else:
        return render_template('index.html')