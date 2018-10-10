some_list = {
    'value': 1,
    'next': {
        'value': 2,
        'next': {
            'value': 3,
            'next': {
                'value': 4,
                'next': None,
            },
        },
    },
}


def reverse_print(some_list):
    arr = []
    while some_list:
        arr.append(some_list.get('value'))
        some_list = some_list.get('next')

    return print(arr[::-1])


reverse_print(some_list)
