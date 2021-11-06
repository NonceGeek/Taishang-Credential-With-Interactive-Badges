from pyweidentity.weidentityService import weidentityService

URL = "http://124.251.110.210:6001"
# WeIdentity RestService URL
weid = weidentityService(URL)

# _weid = weid.create_weidentity_did()

# # print(_weid)
# # _weid = "did:weid:3:0xa8b750253750e275fa970d8660036e18e07c7311"
_weid = "did:weid:3:0xbce3653371dd7d77aebd17a6832dca8eb8c8a212"


# claim = {
#     "addr": "zhang san",
#     "token_id": "123",
#     "response": "{wlkejgiwoe}"
# }
# credential = weid.create_credentialpojo(333333, _weid, "2022-04-18T21:12:33Z", claim, _weid)






cptId = 333333
issuanceDate = 1636175773

context = "https://github.com/WeBankFinTech/WeIdentity/blob/master/context/v1"

claim = {'addr': 'zhang san', 'response': '{wlkejgiwoe}', 'token_id': '123'}

id = '861c88fb-9444-467a-8086-4096a22c9b6b'

proof = {
    "created": 1636175773,
    "creator": "did:weid:3:0xbce3653371dd7d77aebd17a6832dca8eb8c8a212#keys-0", 
    "salt": {"addr": "mYZVD", "response": "AHqyC", "token_id": "T0Geo"}, 
    "signatureValue": "bQci49FW83ouS0+Ts6pWWtg4s/BlfSul90JocqcwW50PJ+9bcapIXbHEB9S13fiUZH8xqpQJscnAB2p1iktRcAE=", 
    "type": "Secp256k1"
}

_type = ["VerifiableCredential", "original"]


issuer = "did:weid:3:0xbce3653371dd7d77aebd17a6832dca8eb8c8a212"

expirationDate = 1650287553

# self, cptId, issuanceDate, context, claim, credential_pojo_id, proof, issuerWeId, expirationDate

verify_credential_data = weid.verify_credentialpojo(cptId,issuanceDate,context,claim,id,proof,_type,issuer,expirationDate)
print(verify_credential_data)

# {'functionArg': 
#     {'claim': {'con_addr': 'test', 'token_id': 'test'},
#                  'context': 'https://github.com/WeBankFinTech/WeIdentity/blob/master/context/v1',
#                  'cptId': 2000003,
#                  'expirationDate': 1650287553,
#                  'id': 'c5cb3828-5d94-4e5b-afdd-f965125fd3e8',
#                  'issuanceDate': 1636165120,
#                  'issuer': 'did:weid:3:0xbce3653371dd7d77aebd17a6832dca8eb8c8a212',
#                  'proof': {'created': 1636165120,
#                            'creator': 'did:weid:3:0xbce3653371dd7d77aebd17a6832dca8eb8c8a212#keys-0',
#                            'salt': {'con_addr': 'kWtjQ', 'token_id': 'grtBq'},
#                            'signatureValue': '8+zTMGEYOjqgiwBjF/lULyuhYDpJSwHZKdOdc6xtN+lJWoboKRow8/DK9AQAMCsI0mqxZno1j4w09DM2mNuWUgA=',
#                            'type': 'Secp256k1'},
#                  'type': ['VerifiableCredential', 'hashTree']},
#  'functionName': 'verifyCredentialPojo',
#  'transactionArg': {},
#  'v': '1.0.0'}