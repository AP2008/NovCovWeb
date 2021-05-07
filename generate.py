template = """
<html>
  <head>
    <style>
      html, body {{
        border: 0px;
        margin: 0px;
        padding: 0px;
      }}
    </style>
  </head>
  <body>
    <iframe width="100%" height="100%" frameBorder="0" src="https://thunder2020.pythonanywhere.com/{}"></iframe>
  </body>
</html>
"""

pages = ['index', 'timeline', 'datatable', 'map', 'counter', 'growth', 'infocenter', 'about']


for page in pages:
  print(f"Writing {page}")
  with open(page+'.html', "w+") as f:
    f.write(template.format(page))