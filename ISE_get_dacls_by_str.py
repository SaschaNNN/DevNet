import sys
import requests
import urllib3
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GetDaclByStr:
    def __init__(self, **kwargs):
        self.ise_primary_PAN = kwargs.pop('ise_primary_PAN')
        self.username = kwargs.pop('username')
        self.password = kwargs.pop('password')
        self.dacl_str = kwargs.pop('dacl_str')
        self.base_url = f'https://{self.username}:{self.password}@{self.ise_primary_PAN}:9060/ers/config/'
        self.result = self.get_dacls_by_str()

    def ise_api_call(self, specific_url_part, media_type_header):
        header = {'Accept': 'application/json',
                  'Content-Type': 'application/json'}
        header.update(media_type_header)
        try:
            page = requests.get(f'{self.base_url}{specific_url_part}',
                                headers=header,
                                verify=False,
                                timeout=5)
        except requests.exceptions.ConnectTimeout as ct:
            return f'ISE is not reachable\n{ct}'

        else:
            if page.status_code == 200:
                return page
            else:
                return f'{page.status_code}, {page.reason}'

    def get_dacls_by_str(self):
        page_num = 1
        dacl_ids = []
        dacls_name_id = {}
        dacls = self.ise_api_call(f'downloadableacl?size=100&page={page_num}',
                                  {'ERS-Media-Type': 'network.downloadableacl.1.0'})
        if type(dacls) == str:
            return dacls
        while dacls.json()['SearchResult']['total'] != 0:
            page_num += 1
            for dacl in dacls.json()['SearchResult']['resources']:
                dacl_ids.append(dacl['id'])
            dacls = self.ise_api_call(f'downloadableacl?size=100&page={page_num}',
                                      {'ERS-Media-Type': 'network.downloadableacl.1.0'})
        if not dacl_ids:
            return 'No dacls'
        header = {'Accept': 'application/json',
                  'Content-Type': 'application/json',
                  'ERS-Media-Type': 'network.downloadableacl.1.0'}
        session = FuturesSession(max_workers=5)
        futures = [session.get(f'https://{self.username}:{self.password}@{self.ise_primary_PAN}:9060'
                               f'/ers/config/downloadableacl/{dacl_id}',
                               headers=header,
                               verify=False,
                               timeout=5) for dacl_id in dacl_ids]
        for f in as_completed(futures):
            dacl_name = f.result().json()['DownloadableAcl']['name']
            rules = f.result().json()['DownloadableAcl']['dacl']
            if self.dacl_str in rules:
                dacls_name_id.update({dacl_name: 'dacl_id'})
        if dacls_name_id:
            return dacls_name_id
        else:
            return f'No dacls with string: {self.dacl_str}'


if __name__ == "__main__":
    import time
    start = time.time()
    if len(sys.argv) > 1:
        params = {'ise_primary_PAN': '172.22.2.1',
                  'username': 'API_user',
                  'password': ''}
        dacl_strings = sys.argv
        for dacl_str in dacl_strings[1:]:
            params.update({'dacl_str': dacl_str})
            result = GetDaclByStr(**params)
            print(f'Dacls for string {dacl_str}:\n{result.result}')
            print(time.time() - start)
    else:
        print("Use any string as arguments")
