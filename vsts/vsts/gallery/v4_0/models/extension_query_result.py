# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ExtensionQueryResult(Model):
    """ExtensionQueryResult.

    :param results: For each filter supplied in the query, a filter result will be returned in the query result.
    :type results: list of :class:`ExtensionFilterResult <gallery.v4_0.models.ExtensionFilterResult>`
    """

    _attribute_map = {
        'results': {'key': 'results', 'type': '[ExtensionFilterResult]'}
    }

    def __init__(self, results=None):
        super(ExtensionQueryResult, self).__init__()
        self.results = results
