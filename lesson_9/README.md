# Result

## typos and errors

Request
```json
{
  "query": {
    "fuzzy": {
      "txt": {
        "value": "spplr",
        "fuzziness": 2,
        "max_expansions": 50,
        "prefix_length": 0,
        "transpositions": true,
        "rewrite": "constant_score"
      }
    }
  }
}
```
### words index returned
```json
{
  "took": 16,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 81,
      "relation": "eq"
    },
    "max_score": 1.0,
    "hits": [
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "apparel",
        "_score": 1.0,
        "_source": {
          "txt": "apparel"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "supported",
        "_score": 1.0,
        "_source": {
          "txt": "supported"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "upper",
        "_score": 1.0,
        "_source": {
          "txt": "upper"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "spirit",
        "_score": 1.0,
        "_source": {
          "txt": "spirit"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "separate",
        "_score": 1.0,
        "_source": {
          "txt": "separate"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "supplies",
        "_score": 1.0,
        "_source": {
          "txt": "supplies"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "apply",
        "_score": 1.0,
        "_source": {
          "txt": "apply"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "supply",
        "_score": 1.0,
        "_source": {
          "txt": "supply"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "opportunities",
        "_score": 1.0,
        "_source": {
          "txt": "opportunities"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "appropriate",
        "_score": 1.0,
        "_source": {
          "txt": "appropriate"
        }
      }
    ]
  }
}
```

### autocomplete index returned
```json
{
  "took": 11,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 6,
      "relation": "eq"
    },
    "max_score": 1.0,
    "hits": [
      {
        "_index": "autocomplete",
        "_type": "_doc",
        "_id": "apple",
        "_score": 1.0,
        "_source": {
          "txt": "apple"
        }
      },
      {
        "_index": "autocomplete",
        "_type": "_doc",
        "_id": "apply",
        "_score": 1.0,
        "_source": {
          "txt": "apply"
        }
      },
      {
        "_index": "autocomplete",
        "_type": "_doc",
        "_id": "supply",
        "_score": 1.0,
        "_source": {
          "txt": "supply"
        }
      },
      {
        "_index": "autocomplete",
        "_type": "_doc",
        "_id": "upper",
        "_score": 1.0,
        "_source": {
          "txt": "upper"
        }
      },
      {
        "_index": "autocomplete",
        "_type": "_doc",
        "_id": "spell",
        "_score": 1.0,
        "_source": {
          "txt": "spell"
        }
      },
      {
        "_index": "autocomplete",
        "_type": "_doc",
        "_id": "super",
        "_score": 1.0,
        "_source": {
          "txt": "super"
        }
      }
    ]
  }
}
```

## strict match

Words and autocomplete index returned the same results

```json
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 4,
      "relation": "eq"
    },
    "max_score": 1.0,
    "hits": [
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "1",
        "_score": 1.0,
        "_source": {
          "txt": "booba"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "6",
        "_score": 1.0,
        "_source": {
          "txt": "booba suffix"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "7",
        "_score": 1.0,
        "_source": {
          "txt": "booba another"
        }
      },
      {
        "_index": "words",
        "_type": "_doc",
        "_id": "8",
        "_score": 1.0,
        "_source": {
          "txt": "booba third"
        }
      }
    ]
  }
}
```
