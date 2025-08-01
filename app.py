# app.py - Minimal backend that just works
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import json

app = Flask(__name__)
CORS(app)

def call_anthropic_api(question):
    """Direct API call to Anthropic - bypassing the Python library entirely"""
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    
    if not api_key:
        return "API key not configured"
    
    # Basic context about Satvik
    context = """
Satvik Puti is a founder of Just Build It. He has experience at Sanofi, Danone, and L'Oréal. 
He's an ambitious entrepreneur who founded France's largest student AI association.
He's an endurance athlete, content creator, and community builder living in Paris.
Values: Ambitious, daring, curious,and humble.
"""
    
    prompt = f"""You are Satvik's AI assistant. Based on this context: {context}

Question: {question}

Give a professional response for VCs/HRs. If you don't know something specific, suggest booking a call at https://calendly.com/satvikputi/brainstorming"""
    
    try:
        # Direct HTTP request to Anthropic API
        response = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers={
                'Content-Type': 'application/json',
                'x-api-key': api_key,
                'anthropic-version': '2023-06-01'
            },
            json={
                'model': 'claude-3-sonnet-20240229',
                'max_tokens': 300,
                'messages': [
                    {'role': 'user', 'content': prompt}
                ]
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            return data['content'][0]['text']
        else:
            print(f"API Error: {response.status_code} - {response.text}")
            return "I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly: https://calendly.com/satvikputi/brainstorming"
            
    except Exception as e:
        print(f"Request error: {e}")
        return "I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly: https://calendly.com/satvikputi/brainstorming"

@app.route('/')
def home():
    return jsonify({
        "status": "Satvik AI Backend is running!",
        "message": "Simple backend with direct Anthropic API calls"
    })

@app.route('/api/ask', methods=['POST', 'OPTIONS'])
def ask():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({"answer": "Please provide a question about Satvik."})
        
        # Get AI response
        answer = call_anthropic_api(question)
        return jsonify({"answer": answer})
        
    except Exception as e:
        return jsonify({
            "answer": "I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly: https://calendly.com/satvikputi/brainstorming"
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)