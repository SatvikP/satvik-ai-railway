# app.py - Simple Flask app for Railway
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "Satvik AI Backend is running on Railway!"})

@app.route('/api/ask', methods=['POST', 'OPTIONS'])
def ask():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({"answer": "Please provide a question about Satvik."})
        
        # Simple responses for testing
        question_lower = question.lower()
        
        if 'values' in question_lower:
            answer = "Satvik's core values are being ambitious and daring, yet humble. He founded France's largest student AI association and believes in innovation with execution excellence."
        elif 'company' in question_lower and 'value' in question_lower:
            answer = "Satvik can create value through his experience at Sanofi, Danone, and L'Oréal where he drove 85% growth. As founder of Just Build It, he brings entrepreneurial mindset and AI expertise."
        elif 'not working' in question_lower or 'personal' in question_lower:
            answer = "Satvik is an endurance athlete (1000km+ annually), content creator (400K+ impressions), and community builder. He's training for Ladakh Half Marathon and runs a Substack called '1% Better'."
        else:
            answer = f"I'd recommend booking a call with Satvik to discuss '{question}' in detail. Here's his Calendly: https://calendly.com/satvikputi/brainstorming"
        
        return jsonify({"answer": answer})
        
    except Exception as e:
        return jsonify({
            "answer": "I'd recommend booking a call with Satvik. Here's his Calendly: https://calendly.com/satvikputi/brainstorming"
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)