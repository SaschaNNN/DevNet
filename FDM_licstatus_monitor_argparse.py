import requests
import urllib3
import argparse
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# fdm_list = ['172.24.2.66', '172.27.128.5']


class SmartAccountStatus:
    def __init__(self):
        self.result = self.licstatus()

    def licstatus(self):
        username = 'zabbix'
        password = ''
        data = {"grant_type": "password", "username": f"{username}", "password": f"{password}"}
        token_url = f'https://{args.fdm_ip}/api/fdm/v5/fdm/token'
        lic_status_url = f'https://{args.fdm_ip}/api/fdm/v5/license/smartagentstatuses'
        headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        try:
            page = requests.post(token_url, data=json.dumps(data), headers=headers, verify=False, timeout=5)
        except requests.exceptions.ConnectTimeout:
            print(f'{args.fdm_ip} - Timeout')
        except requests.exceptions.ConnectionError:
            print(f'{args.fdm_ip} - No connection')
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
                    result = {str(args.fdm_ip): [str(reg_status), str(authz_status)]}
                    return result
                return 'Error: cannot get lic status'
            return 'Error: cannot access FDM ip'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='FDM smart account status check')
    parser.add_argument('-fdm_ip', required=True, )
    args = parser.parse_args()
    print(SmartAccountStatus().result)
