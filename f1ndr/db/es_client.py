from elasticsearch import Elasticsearch
from f1ndr.config.config import F1ndrConfig


def get_es():
    """
    Create and return an Elasticsearch client for f1ndr.
    """
    return Elasticsearch(
        hosts=[{
            "host": F1ndrConfig.ES["host"],
            "port": F1ndrConfig.ES["port"]
        }]
    )
