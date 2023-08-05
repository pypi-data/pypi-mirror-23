import requests

from . import API_ROOT, MTKAPIError
from .api import api


class Resource:
    api = api

    @property
    def url(self):
        return API_ROOT + '/' + self.resource


class ResourceList(Resource):
    ITEM = None

    def __init__(self, resource):
        self.resource = resource
        self.items = []

    def convert_item(self, item):
        if self.ITEM is None:
            raise NotImplementedError('Must declare item version of list')

        resource_item = self.ITEM(0)
        resource_item.id = item['id']
        resource_item.data = item
        return resource_item

    def get(self, params=None):
        response = self.api.session.get(self.url, params=params)
        if response.status_code != 200:
            raise MTKAPIError(response.status_code, response.text)

        for item in response.json():
            self.items.append(self.convert_item(item))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '\n'.join(map(str, self.items))


class ResourceItem(Resource):
    def __init__(self, resource, id):
        self.resource = resource
        self.id = None if id is None else int(id)
        self.data = None

    def get(self):
        response = self.api.session.get(self.url + '/' + str(self.id))
        if response.status_code != 200:
            raise MTKAPIError(response.status_code, response.text)
        self.data = response.json()

    def save(self):
        if self.id:
            response = self.api.session.put(self.url + '/' + str(self.id), json=self.data)
        else:
            response = self.api.session.post(self.url, json=self.data)
        if response.status_code != 200:
            raise MTKAPIError(response.status_code, response.text)
        self.data = response.json()
        self.id = self.data['id']

    def delete(self):
        response = self.api.session.delete(self.url + '/' + str(self.id))
        if response.status_code != 200:
            raise MTKAPIError(response.status_code, response.text)
