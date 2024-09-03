import os
import sys
import json
import re

import requests

docs_path = sys.argv[1]
if docs_path.endswith('/'):
    docs_path = docs_path[:-1]

DIR_DICT = {
    'cn': f'{docs_path}/zh_CN',
    'en': f'{docs_path}/en_US'
}

def get_files(language, dir_config):
    url_list = []
    for i in dir_config:
        md_name = i.get('path')
        if md_name == './':
            md_name = 'index'

        if i.get('url'):
            md_path = f'{DIR_DICT[language]}/{md_name}.md'
            md_dir = os.path.dirname(md_path)
            if not os.path.exists(md_dir):
                os.makedirs(md_dir)

            response = requests.get(i['url'])
            if response.status_code == 200:
                with open(md_path, 'w') as f:
                    f.write(response.text)
            else:
                print(f'Error: {i["url"]} not found')
                exit(1)

            md_content = response.text
            markdown_image_list = re.findall('(.*?)!\[(.*?)\]\((.*?)\)', md_content)
            html_image_list = re.findall('(.*?)<img src="(.*?)"(.*?)>', md_content)

            image_list = [i[2] for i in markdown_image_list if not i[0].startswith('<!--')]
            image_list.extend([i[1] for i in html_image_list if not i[0].startswith('<!--')])

            for image_src in image_list:
                if image_src.startswith(('http://', 'https://', '<')):
                    continue

                image_path = os.path.join(md_dir, image_src)
                image_path = os.path.abspath(image_path)
                image_dir = os.path.dirname(image_path)
                image_url = f'{"/".join(i["url"].split("/")[:-1])}/{image_src}'
                image_url = image_url.replace('/./', '/')

                if not os.path.exists(image_dir):
                    os.makedirs(image_dir)

                if not os.path.exists(image_path):
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        with open(image_path, 'wb') as f:
                            f.write(response.content)
                    else:
                        print(f'Error: {image_url} not found')
                        exit(1)

        if i.get('children'):
            get_files(language, i['children'])

    return url_list


if __name__ == '__main__':
    r = open(f'{docs_path}/directory.json', 'r')
    directory_config = json.load(r)
    for lang, directory_list in directory_config.items():
        print(f'lang: {lang}')
        get_files(lang, directory_list)
