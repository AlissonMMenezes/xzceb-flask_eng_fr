"""
Coursera Challenge
"""
from ibm_watson import LanguageTranslatorV3
from flask import Flask, request, jsonify
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(
    'APITOKEN')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

INSTANCE = "1d5d894c-1984-4616-8437-79ae2386dfd0"
URL = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/" + INSTANCE
language_translator.set_service_url(URL)

app = Flask("Web Translator")


@app.route("/englishToFrench")
def english_to_french():
    """
    function that translates from english to french
    """
    text_to_translate = request.args.get('textToTranslate')
    translation = language_translator.translate(
        text=text_to_translate,
        model_id='en-fr').get_result()
    print(translation)
    text_translated = translation["translations"][0]["translation"]
    response = {"original": text_to_translate, "translated": text_translated}
    return jsonify(response)


@app.route("/frenchToEnglish")
def french_to_english():
    """
    function that translates from french to english
    """
    text_to_translate = request.args.get('textToTranslate')

    translation = language_translator.translate(
        text=text_to_translate,
        model_id='fr-en').get_result()
    print(translation)
    text_translated = translation["translations"][0]["translation"]

    response = {"original": text_to_translate, "translated": text_translated}

    return jsonify(response)


@app.route("/")
def render_index_page():
    """
    function for the index page
    """
    return "this is a coursera challenge"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
