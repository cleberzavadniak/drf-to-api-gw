def convert(data, title):
    new = dict()

    for key in data.keys():
        new[key] = data[key]

    new['info'] = {
        'version': '1',
        'title': title,
    }

    new['schemes'] = ['https']
    new['paths'] = {}

    for path_uri, path_info in data['paths'].items():
        new_path_info = dict(path_info)
        for method_name, method_info in path_info.items():
            new_method_info = dict(method_info)
            new_method_info['parameters'] = []
            new_path_info[method_name] = new_method_info

            has_json_body = False
            for parameter in method_info['parameters']:
                if parameter['in'] == 'formData':
                    has_json_body = True
                    continue
                else:
                    new_parameter = dict(parameter)
                    if new_parameter.get('x-is-map', None) is not None:
                        del new_parameter['x-is-map']
                    new_method_info['parameters'].append(new_parameter)

            if has_json_body:
                new_method_info['parameters'].append({
                    'name': 'data',
                    'in': 'body',
                    'required': True,
                    'schema': {
                        'type': 'string'
                    }
                })

        new['paths'][path_uri] = new_path_info

    return new
