# drf-to-api-gw

Updates AWS API Gateway using a API created with django-rest-framework as base.

Because DRF doesn't generate a Swagger 2.0 JSON file and AWS doesn't work with Swagger 1.2.


## Usage

    python3 -m drf_to_api_gw https://example.com/v1/docs/api-docs API_NAME

If your app is running on heroku, you can use:

    python3 -m drf_to_api_gw heroku:HEROKU-APP-NAME API_NAME


"API_NAME" is the name of the API as you would like it to be on AWS API Gateway.


## Tanks

 * apimatic.io and this nice tool: https://apitransformer.com/
