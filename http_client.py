import urllib, json, urllib2


def get(url, params):
    url_params = urllib.urlencode(params)
    full_url = url + '?' + url_params
    print full_url
    try:
        response = urllib2.urlopen(full_url).read()
        return json.loads(response)
    except urllib2.HTTPError as e:
        print e
        return {'user': { 'monthly_summary': []}}
