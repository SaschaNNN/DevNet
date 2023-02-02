import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import sys


# fdm_list = ['172.24.2.66', '172.27.128.5']

class SmartAccountStatus:
    def __init__(self, fdm_ip, username, password):
        self.fdm_ip = fdm_ip
        self.username = username
        self.password = password
        self.result = self.licstatus()
        self.get_result()

    def licstatus(self):
        data = {"grant_type": "password", "username": f"{username}", "password": f"{password}"}
        token_url = f'https://{self.fdm_ip}/api/fdm/v5/fdm/token'
        lic_status_url = f'https://{self.fdm_ip}/api/fdm/v5/license/smartagentstatuses'
        headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        try:
            page = requests.post(token_url, data=json.dumps(data), headers=headers, verify=False, timeout=5)
        except requests.exceptions.ConnectTimeout:
            print(f'{self.fdm_ip} - Timeout')
        except requests.exceptions.ConnectionError:
            print(f'{self.fdm_ip} - No connection')
        else:
            if page.status_code == 200:
                access_token = page.json()['access_token']
                headers_authz = {'content-type': 'application/json',
                                 'Accept': 'application/json',
                                 'Authorization': f'Bearer {access_token}'}

                status_raw = requests.get(lic_status_url, headers=headers_authz, verify=False)
                if status_raw.status_code == 200:
                    reg_status = status_raw.json()['items'][0]['registrationStatus']
                    authz_status = status_raw.json()['items'][0]['authorizationStatus']
                    result = {str(self.fdm_ip): [str(reg_status), str(authz_status)]}
                    return result
                return 'Error: cannot get lic status'
            return 'Error: cannot access FDM ip'

    def get_result(self):
        if self.result:
            print(self.result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = 'zabbix'
        password = ''
        ips = sys.argv
        for fdm_ip in ips[1:]:
            SmartAccountStatus(fdm_ip, username, password)
    else:
        print("Use FDM ips as arguments")

