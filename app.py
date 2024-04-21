from flask import Flask, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS


app = Flask(__name__)
load_dotenv()
CORS(app)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route('/')
def index():
    return([])

@app.route('/translate', methods=['POST'])
def translate_code():
    data = request.json
    source_code = data['source_code']
    source_lang = data['source_lang']
    target_lang = data['target_lang']
    
    try:
        prompt_message = f""" Here is a snippet of code that includes inline comments and strings in {source_lang}. Please translate only the inline comments and strings to {target_lang}, and leave the code—including reserved keywords, variable names, and any code structure (like classes, functions, and tags)—exactly as it is. 

The inline comments and strings can be identified by the quotation marks that surround them or by comment tags such as //, /* */, or # depending on the programming language.

Please maintain the integrity of the code and do not alter any part of the code itself.

Code snippet:
{source_code}   """


        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_message},
                {"role": "user", "content": source_code}
            ],
            max_tokens=1024
        )
        translated_code = response.choices[0].message.content
        return jsonify({'translated_code': translated_code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
