import json


class Dajax(object):

    def __init__(self):
        self.calls = []

    def json(self):
        return json.dumps(self.calls)

    def alert(self, message):
        message = unicode(message)
        self.calls.append({'cmd': 'alert', 'val': message})

    def assign(self, id, attribute, value):
        id = unicode(id)
        attribute = unicode(attribute)
        value = unicode(value)
        self.calls.append({'cmd': 'as', 'id': id, 'prop': attribute, 'val': value})

    def add_css_class(self, id, value):
        id = unicode(id)
        value = unicode(value)
        if not hasattr(value, '__iter__'):
            value = [value]
        self.calls.append({'cmd': 'addcc', 'id': id, 'val': value})

    def remove_css_class(self, id, value):
        id = unicode(id)
        value = unicode(value)
        if not hasattr(value, '__iter__'):
            value = [value]
        self.calls.append({'cmd': 'remcc', 'id': id, 'val': value})

    def append(self, id, attribute, value):
        id = unicode(id)
        attribute = unicode(attribute)
        value = unicode(value)
        self.calls.append({'cmd': 'ap', 'id': id, 'prop': attribute, 'val': value})

    def prepend(self, id, attribute, value):
        id = unicode(id)
        attribute = unicode(attribute)
        value = unicode(value)
        self.calls.append({'cmd': 'pp', 'id': id, 'prop': attribute, 'val': value})

    def clear(self, id, attribute):
        id = unicode(id)
        attribute = unicode(attribute)
        self.calls.append({'cmd': 'clr', 'id': id, 'prop': attribute})

    def redirect(self, url, delay=0):
        url = unicode(url)
        self.calls.append({'cmd': 'red', 'url': url, 'delay': delay})

    def script(self, code):  # OK
        code = unicode(code)
        self.calls.append({'cmd': 'js', 'val': code})

    def remove(self, id):
        id = unicode(id)
        self.calls.append({'cmd': 'rm', 'id': id})

    def add_data(self, data, function):
        self.calls.append({'cmd': 'data', 'val': data, 'fun': function})
