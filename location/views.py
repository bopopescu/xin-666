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
from weibousers.models import WeiboUser
from .forms import CategorisePostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.db import connection
from django.db.models import Count
def index(request):
	cx = {}
	statistics = []
	places = Place.objects.all()
	posts = Post.objects.count()
	uncategorised_posts = Post.objects.filter(category=None).count()
	users = WeiboUser.objects.count()
	f_users = WeiboUser.objects.filter(gender='F').count()
	m_users = WeiboUser.objects.filter(gender='M').count()
	# truncate_date = connection.ops.date_trunc_sql('month', 'created')
	# qs = Post.objects.filter(place=1).extra({'month':truncate_date})
	# report = qs.values('month').annotate(Count('pk')).order_by('month')
	cx['places'] = places.count()
	cx['posts'] = posts
	cx['uncategorised_posts'] = uncategorised_posts
	cx['users'] = users
	cx['f_users'] = f_users
	cx['m_users'] = m_users
	for place in places:
		posts = Post.objects.filter(place=place)
		not_categorised_posts = posts.filter(category=None)
		truncate_date = connection.ops.date_trunc_sql('month', 'created')
		qs = posts.extra({'month':truncate_date})
		report = qs.values('month').annotate(Count('pk')).order_by('month')
		statistics.append({
			'place': place,
			'count': posts.count(),
			'not_categorised_count': not_categorised_posts.count(),
			'report': report


		})
		cx['statistics'] = statistics
				
	return render(request, "index.html", cx)


def place_index(request, place_id):
    cx = {}
    place = Place.objects.get(id=place_id)
    cx['place'] = place
    cx['posts'] = Post.objects.filter(place=place).order_by('-created')[:10]
    return render(request, "location/place_index.html", cx)


def categorise_post(request, place_id, post_id=None):
	place = Place.objects.get(id=place_id)
	if post_id:
		obj = get_object_or_404(Post, pk=post_id)
		print 'has post id'
	else:
		obj = Post.objects.filter(place=place, category=None).order_by('created').first()
		print 'haven\' post id'
	form = CategorisePostForm(request.POST or None, instance=obj)
	print request.method
	if request.method == 'POST':
		if form.is_valid():
			print "form.is_valid"
			form.save()
		return redirect(reverse('location:categorise_post', kwargs={'place_id': place_id}))
	print "not valid"
	return render(request, 'location/categorise_post_form.html', 
			{'form': form, 'obj': obj})


@staff_member_required
class CategorisePostView(UpdateView):
    # form_class = CategorisePostForm
    model = Post
    fields = ('place', 'user', 'created', 'text', 'weibo_img', 'category',)
    template_name_suffix = '_update_form'
