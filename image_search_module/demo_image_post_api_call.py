if __name__ == '__main__':
    import requests

    url = 'http://localhost:5000/upload'
    files = {'file': open('/home/asif/Desktop/newplot.png', 'rb')}

    response = requests.post(url, files=files)

    print(response.text)