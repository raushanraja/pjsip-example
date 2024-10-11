import pjsua2 as pj
import time

class Account(pj.Account):
    def onRegState(self, prm):
        print("***OnRegState: " + prm)
        return super().onRegState(prm)


class Calls(pj.Call):
    pass


# create and initialize the endpoint library

endpoint = pj.Endpoint() # Create an endpoing
endpoint_config = pj.EpConfig() # Define a endpoing configuration
endpoint.libCreate() 
endpoint.libInit(endpoint_config) # Initializing Endpoint


# Create a SIP Transport
sip_transport_config = pj.TransportConfig()
sip_transport_config.port = 5060
endpoint.transportCreate(pj.PJSIP_TRANSPORT_UDP, sip_transport_config) # Add transport to endpoint

# start endpoing Library
endpoint.libStart()

# Create an Account
account = pj.Account()
account_config = pj.AccountConfig()
account_config.idUri = "sip:192.168.1.175"


account.create(account_config)


dest_uri = 'sip:name@dest.org'
parameters = pj.CallOpParam(True)
call = Calls(acc=account)
call.makeCall(dest_uri, parameters)


time.sleep(10)

#Destroy the library
endpoint.libDestroy()

