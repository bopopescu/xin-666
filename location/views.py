# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.http import HttpResponse
from .models import Place, Post
from django.shortcuts import render

def index(request):
	cx = {}
	statistics = []
	places = Place.objects.all()
	for place in places:
		posts = Post.objects.filter(place=place)
		not_categorised_posts = posts.filter(category=None)
		statistics.append({
			'place': place,
			'count': posts.count(),
			'not_categorised_count': not_categorised_posts.count()
		})
		cx['statistics'] = statistics
				
	return render(request, "index.html", cx)

def place_index(request, place_id):
    cx = {}
    place = Place.objects.get(id=place_id)
    cx['place'] = place
    cx['posts'] = Post.objects.filter(place=place).order_by('created')[:10]
    return render(request, "location/place_index.html", cx)
