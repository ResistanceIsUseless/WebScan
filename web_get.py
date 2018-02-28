import http.client

conn = http.client.HTTPConnection("10,11,1,50")

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "965e8a0f-c503-4424-ad9a-0e76bc9c8640"
    }

conn.request("GET", "undefined", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
