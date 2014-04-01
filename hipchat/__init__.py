from urllib import urlencode
import urllib2


API_URL_DEFAULT = 'https://api.hipchat.com/v1/'
FORMAT_DEFAULT = 'json'


class HipChat(object):
    def __init__(self, token=None, url=API_URL_DEFAULT, format=FORMAT_DEFAULT):
        self.url = url
        self.token = token
        self.format = format

    def message_room(self, room_id='', message_from='',
                     message='', message_format='html', color='',
                     notify=False):
        url = self.url + 'rooms/message?format=%s&auth_token=%s' \
            % (self.format, self.token)
        values = {
            'room_id': room_id,
            'from': message_from[:15],
            'message': message,
            'color': color,
            'message_format': message_format,
            'notify': notify and '1' or '0',
        }
        data = urlencode(values)
        print url, data
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        _response = response.read()
        return _response
