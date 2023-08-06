from .base import BaseRepresentation
from ..schema import ClusterSchema
from ...api import ClusterResourceList

class ClusterRepresentation(BaseRepresentation):
    SCHEMA = ClusterSchema

    def _search_api_for_duplicates(self):
        duplicates = []
        clusters = ClusterResourceList()
        clusters.get()
        for cluster in clusters.items:
            if cluster.uri == self.uri:
                duplicates.append(cluster)
        return duplicates

    def determine_dependencies(self, candidates):
        self._dependencies = []

    @property
    def uri(self):
        ssh = self.document['spec']['ssh']
        return f'{ssh["username"]}@{ssh["hostname"]}:{ssh["port"]}'
