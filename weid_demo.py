from pyweidentity.weidentityService import weidentityService

URL = "http://124.251.110.210:6001"
# WeIdentity RestService URL

weid = weidentityService(URL)
create_weid = weid.create_weidentity_did()
print(create_weid)


# http://124.251.110.210:6001