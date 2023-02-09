from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator

from flask import Flask
app = Flask("Flask")
text1 = 'Hello, good day to you'

@app.route('/')
def english_to_french():
  url='https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/343971cd-82b8-45ed-a65e-544b18b97226'
  apikey='Us2a4GDOlyzuuLWnfnnGsyZq2z2Ev-tks3wbQlrfvreF'
  text1 = 'Hello, good day to you'
  authenticator = IAMAuthenticator(apikey)
  language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
  language_translator.set_service_url(url)
  frenchtranslation = language_translator.translate(text=text1,model_id='en-fr').get_result()
  return frenchtranslation.get("translations")[0].get("translation")

if __name__ == "__main__":
	app.run(debug=True)
