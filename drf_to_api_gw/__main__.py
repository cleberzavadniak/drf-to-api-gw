import sys
import json
import subprocess
import tempfile

from . import converter, apitransformer


url = sys.argv[1]
title = sys.argv[2]

if url.startswith('heroku:'):
    url = url.split(':')[1]
    url = "https://{}.herokuapp.com/v1/docs/api-docs/".format(url)

# Transform into Swagger 2.0:
swagger20 = apitransformer.transform(url)

original_path = tempfile.mktemp(prefix='SWAGGER-')
with open(original_path, 'w') as f:
    f.write(json.dumps(swagger20, indent=4))
print('Original (Swagger 2.0): {}'.format(original_path))

# Convert to be acceptable to AWS API:
new = converter.convert(swagger20, title)

output_path = tempfile.mktemp(prefix='AWS-SWAGGER-')
with open(output_path, 'w') as f:
    f.write(json.dumps(new, indent=4))
print('Adapted: {}'.format(output_path))

# Send to AWS API Gateway:
cmd = 'aws apigateway import-rest-api --body "$(cat {})"'.format(output_path)
print(cmd)

status, output = subprocess.getstatusoutput(cmd)
print(output)

sys.exit(status)
