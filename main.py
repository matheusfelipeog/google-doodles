# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Builtins
    import json

    # My modules
    from sample.process import start

    data = start("josephine-langs-205th-birthday")

    with open('./data/data-google-doodles.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
