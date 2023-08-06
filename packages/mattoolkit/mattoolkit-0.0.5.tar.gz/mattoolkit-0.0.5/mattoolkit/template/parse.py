from pathlib import Path
import itertools

import yaml

from .representation import (
    StructureRepresentation, CalculationRepresentation,
    ClusterRepresentation, UserRepresentation
)
from ..api.resource import ResourceItem


def read_yaml_files(path):
    filepath = Path(path)
    for yaml_file in itertools.chain(filepath.glob('**/*.yaml'),
                                     filepath.glob('**/*.yml')):
        for yaml_document in yaml.load_all(yaml_file.open()):
            yield (str(yaml_file), yaml_document)


def linearize_dependencies(representations):
    # Hack to linearize resolve order
    resolve_order = []
    # All Users First
    for representation in representations:
        if isinstance(representation, UserRepresentation):
            resolve_order.append(representation)

    # All Cluster, Structure Second
    for representation in representations:
        if isinstance(representation, (StructureRepresentation, ClusterRepresentation)):
            resolve_order.append(representation)

    # Finally Add Calculation in correct order
    while len(resolve_order) < len(representations):
        resolve_order_added = []
        for representation in representations:
            if representation in resolve_order:
                continue
            dependencies_satisfied = True
            print(representation)
            for dependency in representation.dependencies:
                if isinstance(dependency, ResourceItem):
                    continue
                elif dependency not in resolve_order:
                    dependencies_satisfied = False
            if dependencies_satisfied:
                resolve_order_added.append(representation)
        if len(resolve_order_added) == 0:
            raise ValueError('Unable to linearize dependencies curently resolved list', resolve_order)
        resolve_order.extend(resolve_order_added)
    return resolve_order


def parse_yaml_files(paths, recursive, test, search_api=True):
    # TODO: listen to recursive argument
    # TODO: test make do something
    representations = []
    for path in paths:
        for filename, document in read_yaml_files(path):
            if 'kind' not in document:
                raise ValueError({
                    'filename': filename,
                    'errors': {'kind', 'must be specified'}
                })

            kinds_map = {
                'Structure': StructureRepresentation,
                'Calculation': CalculationRepresentation,
                'Cluster': ClusterRepresentation,
                'User': UserRepresentation
            }

            try:
                representation = kinds_map[document['kind']](document, filename, search_api=search_api)
                representations.append(representation)
            except ValueError as e:
                raise ValueError({'filename': filename, 'errors': e.args[0]})

    for representation in representations:
        representation.determine_dependencies(representations)
    resolved_order = linearize_dependencies(representations)
    return representations, resolved_order
