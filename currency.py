import requests

def main():
    res = requests.get('http://data.fixer.io/api/latest?access_key=227e7118613b8c5bd9fd9f31353600fd')

    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessfull!")
    data = res.json()
    print(data)

if __name__ == '__main__':
    main()