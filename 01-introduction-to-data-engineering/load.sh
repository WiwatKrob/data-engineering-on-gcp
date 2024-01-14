#!/bin/bash

API_KEY='$2a$10$WM2MYaGUlNfKZlkwJJIl3.DpwgIDsHU2pSCWmnvOAV2d6y.nIrF7O'
COLLECTION_ID='659a4f30266cfc3fde739afa'

curl -XPOST \
    -H "Content-type: application/json" \
    -H "X-Master-Key: $API_KEY" \
    -H "X-Collection-Id: $COLLECTION_ID" \
    -d @dogs.json \
    "https://api.jsonbin.io/v3/b"