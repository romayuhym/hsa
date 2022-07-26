from elasticsearch import Elasticsearch, NotFoundError

# Create the client instance
client = Elasticsearch("http://localhost:9200")

SOURCE_INDEX_NAME = "words"
DESTINATION_INDEX_NAME = "autocomplete"


def create_index():
    try:
        client.indices.delete(index=SOURCE_INDEX_NAME)
        client.indices.delete(index=DESTINATION_INDEX_NAME)
    except NotFoundError:
        pass

    client.indices.create(
        index=SOURCE_INDEX_NAME,
        ignore=400,
        settings={
            "analysis": {
                "filter": {
                    "autocomplete_filter": {
                        "type": "edge_ngram",
                        "min_gram": 1,
                        "max_gram": 10
                    }
                },
                "analyzer": {
                    "autocomplete": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "lowercase",
                            "autocomplete_filter"
                        ]
                    }
                }
            }
        },
        mappings={
            "properties": {
                "txt": {
                    "type": "text",
                    "analyzer": "autocomplete",
                    "search_analyzer": "standard"
                }
            }
        }
    )
    client.indices.create(
        index=DESTINATION_INDEX_NAME,
        ignore=400,
        mappings={
            "properties": {
                "txt": {
                    "type": "search_as_you_type",
                }
            }
        },
    )

    with open("google-10000-english.txt", "r") as file:
        for word in file:
            word = word.strip(" ").strip("\n")
            if len(word) > 3:
                client.index(index=SOURCE_INDEX_NAME, id=word, document={"txt": word})

    client.index(index=SOURCE_INDEX_NAME, id='1', document={"txt": 'booba'})
    client.index(index=SOURCE_INDEX_NAME, id='2', document={"txt": 'vooba'})
    client.index(index=SOURCE_INDEX_NAME, id='3', document={"txt": 'boooba'})
    client.index(index=SOURCE_INDEX_NAME, id='4', document={"txt": 'oboba'})
    client.index(index=SOURCE_INDEX_NAME, id='5', document={"txt": 'buba'})
    client.index(index=SOURCE_INDEX_NAME, id='6', document={"txt": 'booba suffix'})
    client.index(index=SOURCE_INDEX_NAME, id='7', document={"txt": 'booba another'})
    client.index(index=SOURCE_INDEX_NAME, id='8', document={"txt": 'booba third'})


if __name__ == "__main__":
    create_index()
