# drf-to-api-gw

Updates AWS API Gateway using an API created with django-rest-framework as base.

Because DRF doesn't generate a **Swagger 2.0** JSON file and AWS doesn't work with **Swagger 1.2**.

## Install

Install it using pip or simply clone this repository.

## Requirements

 * AWS CLI (the "aws" command) (aws-cli >= 1.10.38).

## Usage

    python3 -m drf_to_api_gw https://example.com/v1/docs/api-docs API_NAME

If your app is running on **Heroku**, you can use:

    python3 -m drf_to_api_gw heroku:HEROKU-APP-NAME API_NAME


"API_NAME" is the name of the API as you would like it to be on **AWS API Gateway**.


## Thanks

 * apimatic.io and this nice tool: https://apitransformer.com/
