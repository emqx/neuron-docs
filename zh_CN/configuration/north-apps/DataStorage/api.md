# 订阅信息查询 API

以下内容描述查询 DataStorage 节点订阅信息的 API 服务。


## 获取所有订阅组

*GET*  /api/v2/datalayers/groups

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

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

## 获取指定订阅组下的点位

*GET*  /api/v2/datalayers/tags

### 请求参数

**driver**  必需

**group**  必需

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

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

## 模糊搜索订阅点位

*GET*  /api/v2/datalayers/tag

### 请求参数

**tag**  必需

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

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