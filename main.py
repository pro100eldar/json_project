from plotly.graph_objs import Layout
from plotly import offline

from utils import get_questions_data_by_requests


all_eq_data = get_questions_data_by_requests()
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    title = eq_dicts['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)


data = [{'type': 'scattergeo', 'lon': lons, 'lat': lats, 'text': hover_texts,
         'marker': {'size': [5 * mag for mag in mags],
                    'color': mags,
                    'colorscale': 'Viridis',
                    'reversescale': True,
                    'colorbar': {'title': 'Magnitude'}}}]
my_layout = Layout(title='Global Eathquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_eathquakes.html')
