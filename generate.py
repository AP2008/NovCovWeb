template = """
<html>
  <head>
    <meta name="yandex-verification" content="079aab4b66735690" />
    <script>
      (function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
      new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
      j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
      'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
      }})(window,document,'script','dataLayer','GTM-5J8VR7G');
    </script>
    <style>
      html, body {{
        border: 0px;
        margin: 0px;
        padding: 0px;
      }}
    </style>
    <link rel="icon" type="image/x-icon" href="https://thunder2020.pythonanywhere.com/home/assets/favicon.ico?m=1616760516.946934">
    <title>Corona Tracker - {}</title>
    <meta name="google-site-verification" content="z25fvQ62ziQp5ROIjNJnQizrG8TrsramdlmwDvnVrsc" />
    <meta name="description" content="This website gives the latest data and visualizations of the Novel Covid 19 Virus.">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script async src="https://arc.io/widget.min.js#LHbAsxJ6"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
  </head>
  <body>
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5J8VR7G"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <iframe width="100%" height="100%" frameBorder="0" src="https://thunder2020.pythonanywhere.com/{}"></iframe>
  </body>
</html>
"""

pages = ['index', 'timeline', 'datatable', 'map', 'counter', 'growth', 'vaccine', 'infocenter', 'about']


for page in pages:
  print(f"Writing {page}")
  with open(page+'.html', "w+") as f:
    f.write(template.format((page if page != 'index' else 'home').capitalize(), page))