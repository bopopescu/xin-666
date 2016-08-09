from celeryconfig import app
from django.conf import settings
import requests
import json
from email.utils import parsedate
import time
import datetime
import calendar
import os
from .models import Place, Post
from weibousers.models import WeiboUser

@app.task
def place_pois(place_list=None): # [a, b] are the month of 2016 to request a data from weibo api
    if place_list is None:
        place_list = Place.objects.all()
    else:
        for place_item in place_list:
            stop_loop = False
            stop_page_loop = False
            for page in range(1, 200):
                url = "https://api.weibo.com/2/place/pois/photos.json?poiid={0}&count=50&page={1}&access_token={2}".format(place_item.poiid, page, settings.WEIBO_ACCESS_TOKEN) 
                start_date = datetime.date(2016, 1, 1)
                # _end_date = datetime.date(2016, b, 31)
                # end_date = _end_date.replace(day = calendar.monthrange(_end_date.year, _end_date.month)[1])
                end_date = datetime.date(2016, 12, 31)
                print url, start_date, end_date
                try:
                    response = requests.get(url)
                    data = response.json()
                except requests.exceptions.Timeout:
                    raise
                except requests.exceptions.HTTPError:
                    print "oops something unexpected happened!"
                except requests.exceptions.TooManyRedirects:
                # Tell the user their URL was bad and try a different one
                    print "Error - TooManyRedirects!"
                except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                    print e
                if not data:
                    stop_page_loop = True
                    stop_loop = True
                    break
                json_data = json.dumps(data['statuses'])
                item_dict = json.loads(json_data.replace('\r\n', '\\r\\n'))
                for index, item in enumerate(item_dict):
                    create_date = parsedate(item["created_at"])
                    create_date = time.mktime(create_date)
                    create_date = datetime.date.fromtimestamp(create_date)
                    if start_date > create_date or create_date > end_date:
                        stop_page_loop = True
                        break
                    print index, item['id']
                    print start_date, create_date, end_date
                    try:
                        user=item['user']
                        try:
                            u = WeiboUser.objects.get(weibo_id=user['id'])
                            print 'get -u'
                        except WeiboUser.DoesNotExist:
                            u = WeiboUser(
                                weibo_name=user['name'], weibo_id=user['id'], 
                                gender=user['gender'], province=user['province'],
                                city=user['city'], location=user['location'] )
                            u.save()
                            print 'saved -u'
                        try:
                            p = Post.objects.get(weibo_id=item['id'])
                            print 'get -p'
                            # Uncomment below line after got sorted all error
                            stop_loop = True
                            stop_page_loop = True
                            break
                        except Post.DoesNotExist:
                            p = Post(
                                place=place_item, user=u, 
                                weibo_id=item['id'], created=create_date, 
                                text=item['text'], weibo_img=item['bmiddle_pic'] )
                            p.save()
                            print 'saved -p'
                    except KeyError:
                        pass    
                if stop_page_loop:           
                    break
