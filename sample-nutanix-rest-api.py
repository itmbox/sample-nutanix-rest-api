import requests
# pip install requests
# Global constant. change your VIP and credential
YourCVM="x.x.x.x"
ID= "admin"
PW= "!"

def main():
    global YourCVM,ID,PW
    requestUrl = "https://" + YourCVM + ":9440/PrismGateway/services/rest/v2.0/hosts/"
    # Disable "InsecureRequestWarning: Unverified HTTPS request"
    requests.packages.urllib3.disable_warnings()

    session = requests.Session()
    session.auth = (ID, PW)
    # verify=False, https://stackoverflow.com/questions/51768496/why-do-https-requests-produce-ssl-certificate-verify-failed-error
    response = session.get(requestUrl, verify=False).json()
    # response type is dict, {'metadata':{dict}, 'entities':[....]}
    print(type(response),response)

if __name__ == "__main__":
    main()