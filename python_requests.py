import requests

url = "https://my-json-server.typicode.com/quyentx/my-typicode-json-server/employee"


def get_request():
    # get request without parameter
    x = requests.get(url + "/1")
    print(f"Content type is {x.headers['content-type']}")
    print(f"Body text is: {x.text}")
    print(f"Body json is: {x.json()}")
    print(f"Encoding method is: {x.encoding}")
    print(f"Status code is: {x.status_code}")


def get_request_with_params():
    # get request with parameters in URL
    pl = {"id": 2, "name": ["John Delaware", "Jack Sparrow"]}
    y = requests.get(url, params=pl)
    print(y.url)
    print(y.json())


def get_with_custom_headers():
    # get request with custom header
    headers = {"content-type": "plain/text"}
    z = requests.get(url, headers=headers)
    print(z.request.headers["content-type"])


def post_request():
    post_json = {
        "id": 3,
        "name": "John Human",
        "role": "CEO",
        "age": 34,
        "species": "human"
    }
    r = requests.post(url, data=post_json)
    print("==========================================")
    print(f"Content type is {r.headers['content-type']}")
    print(f"Body text is: {r.text}")
    print(f"Body json is: {r.json()}")
    print(f"Encoding method is: {r.encoding}")
    print(f"Status code is: {r.status_code} {r.reason}")
    print(f"Request is: {r.request}")
    print(f"Response URL is: {r.url}")
    print(f"Time elapsed is: {r.elapsed}")
    assert r.json()["id"] == "3"
    assert r.json()["name"] == "John Human"
    assert r.json()["role"] == "CEO"
    assert r.json()["age"] == "34"
    assert r.json()["species"] == "human"
    assert r.status_code == 201
    r.close()


def post_with_encoded_form():
    pl = {"name": "Mike Powder", "age": 30}
    r = requests.post("https://httpbin.org/post", data=pl)
    print(r.json())
    print(r.status_code)


def post_with_file_content():
    files = {'file': open('rps.py', 'rb')}
    # files = {'file': open('report.xls', 'rb')}
    r = requests.post("https://httpbin.org/post", files=files)
    print(r.json())


def put_request():
    put_json = {
        "id": 2,
        "name": "John Button",
        "role": "Director",
        "age": 33,
        "species": "human"
    }
    r = requests.put("https://httpbin.org/put", json=put_json)
    print(f"Content type is {r.headers['content-type']}")
    print(f"Body text is: {r.text}")
    print(f"Body json is: {r.json()}")
    print(f"Encoding method is: {r.encoding}")
    print(f"Status code is: {r.status_code} {r.reason}")
    print(f"Response URL is: {r.url}")
    print(f"Time elapsed is: {r.elapsed}")
    assert r.status_code == 200
    r.close()


def delete_request():
    # get request without parameter
    r = requests.delete(url + "/1")
    print(f"Content type is {r.headers['content-type']}")
    print(f"Body text is: {r.text}")
    print(f"Body json is: {r.json()}")
    print(f"Encoding method is: {r.encoding}")
    print(f"Status code is: {r.status_code}")
    assert r.status_code == 200
    assert r.json() == {}


get_request()
get_request_with_params()
get_with_custom_headers()

post_request()
post_with_encoded_form()
post_with_file_content()

put_request()

delete_request()
