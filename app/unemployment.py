

print("UNEMPLOYMENT REPORT...")


import os
import json
from dotenv import load_dotenv
import requests

from app.utils import file_csv
from app.alphavantage_service import fetch_unemployment_data

load_dotenv()

#ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

# docs: https://www.alphavantage.co/documentation/#unemployment
#url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
#response = requests.get(url)
#parsed_response = json.loads(response.text)
#print(parsed_response)
#parsed_response = fetch_unemployment_data()

#data = parsed_response["data"]
data = fetch_unemployment_data()["data"]
latest = data[0]
print(latest) #> {'date': '2022-02-01', 'value': '3.8'}


#exit()

#
# DATA AND CHARTING
#

from pandas import DataFrame
from plotly.express import bar


df = DataFrame(data)
print(df.head())

fig = bar(df, x="date", y="value", title="Unemployment Rates")
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html

# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_yaxes
# https://plotly.com/python/reference/layout/yaxis/
# https://plotly.com/python/reference/layout/yaxis/#layout-yaxis-ticksuffix
fig.update_yaxes(
    #tickprefix="$",
    ticksuffix="%",
    showgrid=True
)

fig.show()

#breakpoint()


print("DATAVIZ EXPORT...")
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_image
# fig.to_image(format="png")

# https://plotly.com/python/static-image-export/
# Image export using the "kaleido" engine requires the kaleido package,
#which can be installed using pip:
#    $ pip install -U kaleido
#img_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.png")
img_filepath = file_csv("reports", "unemployment.png")
fig.write_image(img_filepath)


print("CSV EXPORT...")
#csv_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.csv")
csv_filepath = file_csv("reports", "unemployment.csv")
df.to_csv(csv_filepath, index=False)
