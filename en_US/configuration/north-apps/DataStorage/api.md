# Subscription Information Query API

The following content describes the API service for querying the subscription information of the DataStorage node.


## Get All Subscription Groups

*GET*  /api/v2/datalayers/groups

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

```json
{
    "error": 0,
    "children": [
        {
            "id": "6a0662ef-db11-cdde-6eba-21bff62cb350",
            "name": "modbus_node",
            "category": 1,
            "children": [
                {
                    "id": "ae2601b6-7a11-408d-a815-d493c9e128f0",
                    "name": "modbus_group",
                    "category": 2,
                    "children": []
                }
            ]
        }
    ]
}
```

## Get Tags under a Specified Subscription Group

*GET*  /api/v2/datalayers/tags

### Request Params

**driver**  required

**group**  required

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

```json
{
    "error": 0,
    "children": [
        {
            "id": "ae2601b6-7a11-408d-a815-d493c9e128f0",
            "name": "modbus_group",
            "category": 2,
            "children": [
                {
                    "id": "6af5975f-171b-28b5-5aaf-cf77ed801cee",
                    "name": "abc",
                    "type": 3,
                    "category": 3,
                    "leaf": true,
                    "children": []
                },
                {
                    "id": "44ef919e-2e04-7b52-9491-4056ac3da8c6",
                    "name": "def",
                    "type": 3,
                    "category": 3,
                    "leaf": true,
                    "children": []
                },
                {
                    "id": "a3da88b9-e202-509a-a2aa-b6f3d050ad19",
                    "name": "abcdef",
                    "type": 3,
                    "category": 3,
                    "leaf": true,
                    "children": []
                }
            ]
        }
    ]
}
```

## Fuzzy Search for Subscription Tags

*GET*  /api/v2/datalayers/tag

### Request Params

**tag**  required

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

```json
{
    "error": 0,
    "children": [
        {
            "id": "6a0662ef-db11-cdde-6eba-21bff62cb350",
            "name": "modbus_node",
            "category": 1,
            "children": [
                {
                    "id": "ae2601b6-7a11-408d-a815-d493c9e128f0",
                    "name": "modbus_group",
                    "category": 2,
                    "children": [
                        {
                            "id": "6af5975f-171b-28b5-5aaf-cf77ed801cee",
                            "name": "abc",
                            "type": 3,
                            "category": 3,
                            "leaf": true,
                            "children": []
                        },
                        {
                            "id": "a3da88b9-e202-509a-a2aa-b6f3d050ad19",
                            "name": "abcdef",
                            "type": 3,
                            "category": 3,
                            "leaf": true,
                            "children": []
                        }
                    ]
                }
            ]
        }
    ]
}
```