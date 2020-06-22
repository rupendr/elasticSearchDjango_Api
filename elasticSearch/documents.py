from elasticsearch_dsl import DocType, Index
from elasticSearch.models import Car_datasets

# Name of the Elasticsearch index
search_index = Index('library')
# See Elasticsearch Indices API reference for available settings
search_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@search_index.doc_type
class CarDocument(DocType):
    class Meta:
        model = Car_datasets  # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'brand',
        ]
