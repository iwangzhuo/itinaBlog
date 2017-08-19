#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json  
import os  
import requests
import uuid
import json

import urllib2  
import StringIO  
import datetime


auth_token = 'instagram-api-token'




def _key_name(id):  
    return 'instagram-photos/%s.png' % id


def get_ghost_token():  
    res = requests.post('http://127.0.0.1/ghost/api/v0.1/authentication/token', data={
        'username': '78259091@163.com',
        'password': '540058595',
        'grant_type': 'password',
        'client_id': '597878c4f333f74b0a5cae04',
        'client_secret': '9631a53dd871'
    })

    # return json.loads(res.content)['access_token']
    return '2D5DCUrtqar8ET0DmCOokXNWUcJgmFRvSm8TuhbTq6jPjYJImShOgMFeO4jBk5CrvbYhlxcxVfJAaBL7vI9H2JmbzkjQQPjS7Qvt1iqQCZWiA8E1Bt0jFAT69qUc40mlM9Pg41bFcDeEY1aZz2e9LvdfS1ssEBzyWfJW1Nrm9VfVkFbNwgQeT3oKpnuzjNT'

def create_post(title, created_time, imgId, html,location, insUrl):  
    token = get_ghost_token()

    try:
        slug = slugify(title)
    except Exception:
        slug = '(untitled)'

    pd = dict(author="1",
              featured=False,
              image=None,
              feature_image=imgId,
              language="zh_CN",
              markdown=html,
              meta_description=location,
              meta_title=insUrl,
              page=False,
              published_by=None,
              slug=slug,
              status="published",
              tags=[{
                  "id": 7,
                  "uuid": "041d5867-9bc2-4f9e-a5a5-51cf7ab541d1",
                  "name": "instagram",
                  "slug": "instagram",
              }],
              title=title,
              published_at=created_time)

    h = {'Authorization': 'Bearer %s' % token, 'Content-Type': 'application/json'}
    res = requests.post('http://127.0.0.1:2368/ghost/api/v0.1/posts',
                        json=dict(posts=[pd]), headers=h)

def postItem(item):
    # title = item.caption != null?item.caption.text:'无标题'
    
    title = '无标题'
    if 'caption' in item and item['caption'] != None:
      title = item['caption'].get('text')

    created_time = datetime.datetime.fromtimestamp(float(item.get('created_time'))).strftime('%Y-%m-%d %H:%M:%S')
    for url in item.get('urls'): 
      create_post (title, created_time,url.split('/')[-1].split('.')[0],'content', item.get('location'), item.get('link'))

def readInstagramJson():
  json_file = open('tinasun0815/tinasun0815.json')
  json_str = json_file.read()
  json_data = json.loads(json_str)
  print len(json_data)
  for item in json_data:
    postItem(item)

if __name__=='__main__':
  readInstagramJson()
  # print uuid.uuid4()
  # create_post('hello api2xxxxxx','2017-08-18 17:32:37','xxxxxx');