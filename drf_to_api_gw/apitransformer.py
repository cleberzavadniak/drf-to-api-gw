import requests


def transform(url, output_format='swagger20json'):
    apitransformer_url = "https://apitransformer.com/api/transform?output={}".format(output_format)

    response = requests.post(apitransformer_url, data={
        'url': url
    })

    return response.json()
