import sys
import requests
import urllib3
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GetDaclByUser:
    def __init__(self, **kwargs):
        self.ise_primary_PAN = kwargs.pop('ise_primary_PAN')
        self.username = kwargs.pop('username')
        self.password = kwargs.pop('password')
        self.user = kwargs.pop('user')
        self.base_url = f'https://{self.username}:{self.password}@{self.ise_primary_PAN}:9060/ers/config/'
        self.result = self.get_dacl_by_user()

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

    def get_dacl_by_user(self):
        user_settings = self.ise_api_call(f'internaluser/name/{self.user}',
                                          {'ERS-Media-Type': 'identity.internaluser.1.2'})
        if type(user_settings) == str:
            return user_settings
        dacl_name = user_settings.json()['InternalUser']['customAttributes']['DACL']
        page_num = 1
        dacl_id = 0
        dacls = self.ise_api_call(f'downloadableacl?size=100&page={page_num}',
                                  {'ERS-Media-Type': 'network.downloadableacl.1.0'})
        while dacls.json()['SearchResult']['total'] != 0:
            page_num += 1
            for dacl in dacls.json()['SearchResult']['resources']:
                if dacl_name == dacl['name']:
                    dacl_id = dacl['id']
            if dacl_id:
                break
            dacls = self.ise_api_call(f'downloadableacl?size=100&page={page_num}',
                                      {'ERS-Media-Type': 'network.downloadableacl.1.0'})
        if dacl_id == 0:
            return f'No dacls for user: {self.user}'
        dacl_settings = self.ise_api_call(f'downloadableacl/{dacl_id}',
                                          {'ERS-Media-Type': 'network.downloadableacl.1.0'})
        result = dacl_settings.json()['DownloadableAcl']
        return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        params = {'ise_primary_PAN': '172.22.2.1',
                  'username': 'API_user',
                  'password': ''}
        users = sys.argv
        for user in users[1:]:
            params.update({'user': user})
            result = GetDaclByUser(**params)
            if type(result.result) == dict:
                print(f"ACL name: {result.result['name']}")
                print(f"Rules:\n{result.result['dacl']}")
            else:
                print(result.result)
    else:
        print("Use Usernames as arguments")
