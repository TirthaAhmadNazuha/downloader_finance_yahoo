import greenstalk
import requests
import json

def main():
    client = greenstalk.Client(('192.168.20.106',11300))
    # client.use('testing-tube')
    client.watch('testing-tube')
    # client.put('hello world')
    # client.put('hello tirtha')
    # client.put('hello tirtha 1')
    # client.put('hello tirtha 2')
    # client.put('hello tirtha 3')

    print('enter while')
    while True:
        job = client.reserve()
        data = json.loads(job.body)
        print(data['url'])
        client.delete(job)
    # client.close()

main()