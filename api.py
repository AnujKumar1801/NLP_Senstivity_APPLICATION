import paralleldots as pd

api_key = 'CWloAOJKW4TBMDUjY1MqZ6zwQr7akhcmxV4kPsXJyIc'
pd.set_api_key(api_key)


def ner(string):
  String_ner = pd.ner(string)
  return String_ner
