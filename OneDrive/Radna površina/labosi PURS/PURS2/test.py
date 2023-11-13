import requests

payload = {
"temperatura": "120"
}
response = requests.post('http://127.0.0.1:80/temperatura',json=payload)

for k,v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print(response.status_code)
