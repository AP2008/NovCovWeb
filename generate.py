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
    <meta name="description" content="This website gives the latest data and visualizations of the Novel Covid 19 Virus.">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script async src="https://arc.io/widget.min.js#LHbAsxJ6"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
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