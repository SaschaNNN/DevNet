"""
Developed by NAE

Будьте осторожны, скрипт удаляющий строчки еще не добавлен!

Usage: python SCRIPT_NAME USER PASSWORD STRING_TO_FIND_NEEDED_ACLs "STRING NEED TO ADD TO THE END OF FOUND ACLs"
STRING_TO_FIND_NEEDED_ACLs - ищем нужные ACL, в которых есть вхождение этой строчки
"STRING NEED TO ADD TO THE END OF FOUND ACLs" - строчку, которую надо добавить в конец

Example:
>python ISE_get_dacls_w_str_in_name.py API_user API_password acl_LO_ "remark * ... *"
"""
import sys
import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GetDacls:
    def __init__(self, **kwargs):
        self.ise_primary_PAN = kwargs.pop('ise_primary_PAN')
        self.username = kwargs.pop('username')
        self.password = kwargs.pop('password')
        self.str_in_name = kwargs.pop('str_in_name')
        self.str_to_add = kwargs.pop('str_to_add')
        self.base_url = f'https://{self.username}:{self.password}@{self.ise_primary_PAN}:9060/ers/config/'
        self.find_change_dacl()

    def ise_api_get_call(self, specific_url_part, media_type_header):
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
                print(f'Get Failed \n{page.status_code}, {page.reason}')
                sys.exit()

    def ise_api_put_call(self, specific_url_part, media_type_header, changes):
        header = {'Accept': 'application/json',
                  'Content-Type': 'application/json'}
        header.update(media_type_header)
        try:
            page = requests.put(f'{self.base_url}{specific_url_part}',
                                headers=header,
                                verify=False,
                                timeout=5,
                                data=changes)
        except requests.exceptions.ConnectTimeout as ct:
            return f'ISE is not reachable\n{ct}'

        else:
            if page.status_code == 200:
                return page
            else:
                print(f'Change Failed \n{page.status_code}, {page.reason}')
                sys.exit()

    def find_change_dacl(self):
        page_num = 1
        dacl_id = 0
        dacls = self.ise_api_get_call(f'downloadableacl?size=100&page={page_num}',
                                      {'ERS-Media-Type': 'network.downloadableacl.1.0'})
        file_dacls = open("dacls_list_str_in_name.txt", "w")
        file_dacl_rules_before_change = open("dacl_rules_before_change.txt", "w")
        file_dacl_rules_after_change = open("dacl_rules_after_change.txt", "w")
        while dacls.json()['SearchResult']['total'] != 0:
            page_num += 1
            for dacl in dacls.json()['SearchResult']['resources']:
                if self.str_in_name in dacl['name']:
                    dacl_id = dacl["id"]
                    dacl_settings = self.ise_api_get_call(f'downloadableacl/{dacl["id"]}',
                                                          {'ERS-Media-Type': 'network.downloadableacl.1.0'})
                    jsoned_dacl_settings = dacl_settings.json()
                    jsoned_dacl_settings['DownloadableAcl'].update({
                        'dacl': dacl_settings.json()['DownloadableAcl']['dacl'] + '\n' + self.str_to_add})
                    file_dacls.writelines(f"{dacl['name']}, {dacl['description']}, {dacl['id']}\n")
                    file_dacl_rules_before_change.writelines(f"{dacl['name']}\n"
                                                             f"{dacl_settings.json()['DownloadableAcl']['dacl']}\n\n"
                                                             f"------------------------\n\n")

                    self.ise_api_put_call(f'downloadableacl/{dacl["id"]}',
                                          {'ERS-Media-Type': 'network.downloadableacl.1.0'},
                                          json.dumps(jsoned_dacl_settings))
                    dacl_settings = self.ise_api_get_call(f'downloadableacl/{dacl["id"]}',
                                                          {'ERS-Media-Type': 'network.downloadableacl.1.0'})
                    file_dacl_rules_after_change.writelines(f"{dacl['name']}\n"
                                                            f"{dacl_settings.json()['DownloadableAcl']['dacl']}\n\n"
                                                            f"------------------------\n\n")
            dacls = self.ise_api_get_call(f'downloadableacl?size=100&page={page_num}',
                                          {'ERS-Media-Type': 'network.downloadableacl.1.0'})
        file_dacls.close()
        file_dacl_rules_before_change.close()
        file_dacl_rules_after_change.close()
        if not dacl_id:
            print(f'No dacls with string {self.str_in_name} in name')
        else:
            print(f'dacls with string "{self.str_in_name}" in name FOUND.\n'
                  f'All found dacls here in the current directory: dacls_list_str_in_name.txt')
            print('Change successfull. See in the current directory: '
                  'dacl_rules_before_change.txt'
                  'dacl_rules_after_change.txt')
            return 0


if __name__ == "__main__":
    if len(sys.argv) > 2:
        params = {'ise_primary_PAN': '172.22.2.1',
                  'username': sys.argv[1],
                  'password': sys.argv[2],
                  'str_in_name': sys.argv[3],
                  'str_to_add': sys.argv[4]}
        GetDacls(**params)
    else:
        print("Enter Username and password as arguments (space separated)")
