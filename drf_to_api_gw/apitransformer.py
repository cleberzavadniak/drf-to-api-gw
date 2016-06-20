import requests


def transform(url, output_format='swagger20json'):
    response = requests.get(url)
    original_data = response.text

    apitransformer_url = "https://apitransformer.com/api/transform?output={}".format(output_format)

    response = requests.post(apitransformer_url, data=original_data)

    return response.json()
