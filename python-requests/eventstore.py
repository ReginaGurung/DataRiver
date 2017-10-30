import uuid
import requests
import sys


UUID = uuid.uuid4()
headers = {
    'Content-Type': 'application/json',
    'ES-EventType': 'event',
    'ES-EventId ': str(UUID),
    'Accept-Charset': 'UTF-8'
}

# def read_event(base_url, stream, event, json_file):
#     url = "{}/streams/{}".format(base_url, stream)
#     print(url)
#     print(headers)
#     r = requests.get(url, headers = headers)
#     text = r.text
#     print(text)


def store_event(base_url, stream, event, json_file):

    with open(json_file, 'r') as fp:
        j_file = fp.read()

        url = "{}/streams/{}".format(base_url, stream)
        r = requests.post(url, data=j_file, headers=headers)

if __name__ == '__main__':

    store_event(
        base_url=sys.argv[1],
        stream= sys.argv[2],
        event=sys.argv[3],
        json_file=sys.argv[4])

    # read_event(
    #     base_url=sys.argv[1],
    #     stream= sys.argv[2],
    #     event=sys.argv[3],
    #     json_file=sys.argv[4])

