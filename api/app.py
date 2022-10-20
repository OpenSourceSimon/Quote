import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    rs = requests.get("https://api.quotable.io/random")
    data = rs.json()

    # Get a random background image from source.unsplash.com
    resolution = '1920x1080'
    category = 'nature'
    background = requests.get(f'https://source.unsplash.com/random/{resolution}?{category}', stream=True).url

    # Save the following to an HTML file
    html = f'''
    <html>
       <head>
          <title>Quote of the day</title>
          <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@300&display=swap" rel="stylesheet">
       </head>
       <style>
          body {{
          background-image: url("{background}");
          background-size: cover;
          background-position: center;
          font-family: 'Roboto Slab';
          color: white;
          text-align: center;
          overflow: hidden;
          display: flex;
          align-items: center;
          justify-content: center;
          flex-direction: column;
          padding-left: 50px;
          padding-right: 50px;
          }}
          h1 {{
          text-shadow: 2px 2px 4px #000000;
          font-size: 50px;
          }}
          h2 {{
            text-shadow: 2px 1px 4px #000000;
            }}
       </style>
       <div style="position: absolute; top: 40%">
          <h1>{data["content"]}</h1>
          <h2>– {data["author"]}</h2>
       </div>
    </html>
        '''
    return html
