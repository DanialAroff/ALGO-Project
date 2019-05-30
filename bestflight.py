from gmplot import *
from number2 import ADistance
from Graph import Graph
from geopy.geocoders import Nominatim
import plotly.plotly as py
import plotly.graph_objs as go
import RabinKarp
import webbrowser
import time
import os

start = time.time()

d = ADistance()
locations = ['Jakarta', 'Dhaka', 'Manila', 'Bandar Seri Begawan', 'Shanghai', 'Kuala Lumpur', 'Tokyo']

for i in range(len(locations)):
    city = locations[i]
    lat, lon = d.get_coord(city)

    # place Map
    # First 2 arguments are the geographical coordinates and the zoom resolution
    gmap3 = gmplot.GoogleMapPlotter(lat, lon, 15)

    gmap3.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"
    # Location of where you want to save the map
    gmap3.draw("maps/" + city + ".html")

# get latitude and longitude points of different cities
coord = []
for j in range(len(locations)):
    coord.append(d.get_coord(locations[j]))
lats, lons = zip(*coord)

# declare center of the map
gmap2 = gmplot.GoogleMapPlotter(3.1516636, 101.6943028, 6)

# Scatter map
gmap2.scatter(lats, lons, '#FF0000', size=50000, marker=False)

# Plot method Draw a line in between given coordinates
# Jakarta(-6.1753942, 106.827183)
# Dhaka(23.7593572, 90.3788136)
# Manila(14.5906216, 120.9799696)
# Bandar Seri Begawan(4.8895453, 114.9417574)
# Shanghai(31.2252985, 121.4890497)
# Kuala Lumpur(3.1516636, 101.6943028)
# Tokyo(35.6828387, 139.7594549)
gmap2.plot([3.1516636, 23.7593572, 35.6828387, 14.5906216, 4.8895453, -6.1753942, 3.1516636, 4.8895453],
           [101.6943028, 90.3788136, 139.7594549, 120.9799696, 114.9417574, 106.827183, 101.6943028, 114.9417574],
           'cornflowerblue', edge_width=2.0)
gmap2.plot([23.7593572, 31.2252985, 35.6828387], [90.3788136, 121.4890497, 139.7594549],
           'cornflowerblue', edge_width=2.0)
gmap2.plot([31.2252985, 14.5906216], [121.4890497, 120.9799696], 'cornflowerblue', edge_width=2.0)
gmap2.plot([23.7593572, 4.8895453], [90.3788136, 114.9417574], 'cornflowerblue', edge_width=2.0)

gmap2.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"

# draw map into html
gmap2.draw("maps/graph_before.html")
url = r"maps\graph_before.html"
webbrowser.open(url, new=2)

geolocator = Nominatim(user_agent='WIA2005_Assignment')
d = ADistance()
locations = ['Jakarta', 'Dhaka', 'Manila', 'Bandar Seri Begawan', 'Shanghai', 'Kuala Lumpur', 'Tokyo']
edges = []

for current in range(len(locations)):
    for other in range(len(locations)):
        if current is not other:
            print(locations[current], '<->', locations[other])
            distance = d.distance(locations[current], locations[other])
            print('Distance: ' + str(distance) + 'km')
            # edges.append(edge(locations[current], locations[other], distance))
    print('\n')

graph = Graph([
    ("Kuala Lumpur", "Dhaka", 2584.787), ("Kuala Lumpur", "Jakarta", 1178.665),
    ("Kuala Lumpur", "Bandar Seri Begawan", 1483.521), ("Jakarta", "Bandar Seri Begawan", 1519.996),
    ("Dhaka", "Bandar Seri Begawan", 3361.34), ("Dhaka", "Shanghai", 3171.866), ("Dhaka", "Tokyo", 4903.439),
    ("Bandar Seri Begawan", "Manila", 1260.663), ("Manila", "Shanghai", 1842.992), ("Manila", "Tokyo", 2995.407),
    ("Shanghai", "Tokyo", 1766.048)])


shortest_route = list(graph.dijkstra("Kuala Lumpur", "Tokyo"))

print("Shortest route from Kuala Lumpur to Tokyo")
for i in shortest_route:
    if i is shortest_route[-1]:
        print(i, '\n')
    else:
        print(i, "--> ", end="")

# declare center of the map
gmap3 = gmplot.GoogleMapPlotter(3.1516636, 101.6943028, 6)

for i in range(len(shortest_route) - 1):
    gmap3.plot([d.get_lat(shortest_route[i]), d.get_lat(shortest_route[i + 1])], [d.get_lon(shortest_route[i]), d.get_lon(shortest_route[i + 1])],
              'cornflowerblue', edge_width=2.0)

gmap3.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"
gmap3.draw("maps/graph_after.html")

url = r"maps\graph_after.html"
webbrowser.open(url, new=2)

stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
             'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being',
             'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did',
             "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few',
             'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having',
             'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him',
             'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into',
             'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't",
             'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other',
             'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd",
             "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's",
             'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they',
             "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under',
             'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't",
             'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why',
             "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've",
             'your', 'yours', 'yourself', 'yourselves']

klIO = open('news/text/Kuala Lumpur.txt', 'r', encoding='utf-8-sig')
kl_text = klIO.read().lower()
kl_text = kl_text.replace("\n", " ")
klIO.close()

jakartaIO = open('news/text/Jakarta.txt', 'r', encoding='utf-8-sig')
jakarta_text = jakartaIO.read().lower()
kl_text = kl_text.replace("\n", " ")
jakartaIO.close()

manilaIO = open('news/text/Manila.txt', 'r', encoding='utf-8-sig')
manila_text = manilaIO.read().lower()
kl_text = kl_text.replace("\n", " ")
manilaIO.close()

dhakaIO = open('news/text/Dhaka.txt', 'r', encoding='utf-8-sig')
dhaka_text = dhakaIO.read().lower()
dhaka_text = dhaka_text.replace("\n", " ")
dhakaIO.close()

bandar_seri_begawanIO = open('news/text/Bandar Seri Begawan.txt', 'r', encoding='utf-8-sig')
bandar_seri_begawan_text = bandar_seri_begawanIO.read().lower()
bandar_seri_begawan_text = bandar_seri_begawan_text.replace("\n", " ")
bandar_seri_begawanIO.close()

shanghaiIO = open('news/text/Shanghai.txt', 'r', encoding='utf-8-sig')
shanghai_text = shanghaiIO.read().lower()
shanghai_text = shanghai_text.replace("\n", " ")
shanghaiIO.close()

tokyoIO = open('news/text/Tokyo.txt', 'r', encoding='utf-8-sig')
tokyo_text = tokyoIO.read().lower()
tokyo_text = tokyo_text.replace("\n", " ")
tokyoIO.close()

# Read file for positive and negative words
pfile = open('wordlist/positivewords.txt', 'r', encoding='utf-8-sig')
positive_text = pfile.read().lower().split('\n')
nfile = open('wordlist/negativewords.txt', 'r', encoding='utf-8-sig')
negative_text = nfile.read().lower().split('\n')


# get frequency of words in a text
def frequency(text, city):
    list_of_words = text.split()
    freq = {}
    for x in list_of_words:
        freq[x] = freq.get(x, 0) + 1
    keys = freq.keys()

    print("Frequencies of word for " + city + "'s article:\n\n" + str(freq) + "\n")


# print frequency of each word in text for every cities' article
frequency(kl_text, 'Kuala Lumpur')
frequency(dhaka_text, 'Dhaka')
frequency(jakarta_text, 'Jakarta')
frequency(bandar_seri_begawan_text, 'Bandar Seri Begawan')
frequency(manila_text, 'Manila')
frequency(shanghai_text, 'Shanghai')
frequency(tokyo_text, 'Tokyo')


def word_count(text):
    stop_count = 0
    list_of_words = text.split()
    for word in stopwords:
        if RabinKarp.rabin_karp_matcher(word, text):
            stop_count = stop_count + 1
    return stop_count, len(list_of_words)


kl_stop_count, kl_total_words = word_count(kl_text)
dhaka_stop_count, dhaka_total_words = word_count(dhaka_text)
jakarta_stop_count, jakarta_total_words = word_count(jakarta_text)
bsb_stop_count, bsb_total_words = word_count(bandar_seri_begawan_text)
manila_stop_count, manila_total_words = word_count(manila_text)
shanghai_stop_count, shanghai_total_words = word_count(shanghai_text)
tokyo_stop_count, tokyo_total_words = word_count(tokyo_text)

# Histogram
py.sign_in(username='DanialHarith', api_key='NyqKPpTtwYfr4nyZwcYP')

x = ["Kuala Lumpur", "Dhaka", "Jakarta", "Bandar Seri Begawan", "Manila", "Shanghai", "Tokyo"]
stop_counts = [kl_stop_count, dhaka_stop_count, jakarta_stop_count, bsb_stop_count,
               manila_stop_count, shanghai_stop_count, tokyo_stop_count]
stop_counts = [str(i) for i in stop_counts]
total_words = [kl_total_words, dhaka_total_words, jakarta_total_words, bsb_total_words,
               manila_total_words, shanghai_total_words, tokyo_total_words]
total_words = [str(i) for i in total_words]

data = [
    go.Histogram(
        histfunc="sum",
        y=stop_counts,
        x=x,
        name="Stop words"
    ),
    go.Histogram(
        histfunc="sum",
        y=total_words,
        x=x,
        name="Total words"
    )
]
layout = go.Layout(
    title=go.layout.Title(
        text="Stop Words & Total Words",
        xref='paper',
        x=0
    )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Stop Words Count')

end = time.time() - start
print("Total running time:", end, "s")
