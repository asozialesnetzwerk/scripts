#!/usr/bin/env python

import requests
import sys

if len(sys.argv) > 1:
    url = "https://zitate.prapsschnalinen.de/api/wrongquotes?sort=score&search=" + sys.argv[1]
else:
    url = "https://zitate.prapsschnalinen.de/api/wrongquotes/random?min_rating=2"

response = requests.get(url)
data = response.json()[0]

print(data["quote"]["quote"] + "\n ~ " + data["author"]["author"])