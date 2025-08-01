# app.py - Complete backend with comprehensive Satvik context
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import json

app = Flask(__name__)
CORS(app)

def get_comprehensive_context():
    """Comprehensive context about Satvik for AI responses"""
    return (
        "SATVIK PUTI - Comprehensive Professional Profile\n\n"
        
        "CONTACT & BASIC INFO:\n"
        "• Contact: +33 07 45 64 31 33 | satvik.puti@essec.edu\n"
        "• LinkedIn: satvikputi\n"
        "• Location: Paris, France (3+ years)\n"
        "• Background: Indian entrepreneur and business professional\n"
        "• Languages: English (Bilingual), French (B2-C1), Hindi (Bilingual), Telugu (Native), Japanese (Beginner)\n\n"
        
        "EDUCATION:\n"
        "• ESSEC Business School Paris, France - Grande École Master's in Management (#3 Top Master of Science Management) Since 2022\n"
        "  - Specialized in Consumer Behaviour, Strategy and Management, Entrepreneurship Track\n"
        "  - Key projects: Market Entry for Le Slip Français, Consumer Research for menstrual products, Growth Strategy for Coachhub\n"
        "  - Founding member of Utopia (AI Association), responsible for events and hackathons\n\n"
        "• M.S. Ramaiah Institute of Technology Bangalore, India - Bachelor of Technology, Information Science and Engineering (2016-2020)\n"
        "  - Specialized in Machine Learning, Data Science with R and Python, Database Management with SQL\n"
        "  - Tournament Director for Annual Debate Tournament (500 participants, 1M+ INR budget)\n\n"
        
        "CURRENT STARTUP VENTURE:\n"
        "Just Build It - Founder (3 months, 2024-2025)\n"
        "• Founded a community for curious people in Paris to build ambitious projects together\n"
        "• Organized 3 building sessions with 50+ participants focusing on MVPs, AI Agents, and full stack applications\n"
        "• Organized 8-hour hackathon at École 42 Paris with 100+ participants\n"
        "• Secured 10K€+ sponsorship from major tech companies: Anthropic, Lovable, Cerebras Systems, and Windsurf\n"
        "• Vision: Build a 10-person company worth $100B\n"
        "• Community-first approach: Started as a community, evolving into a startup\n\n"
        
        "PROFESSIONAL EXPERIENCE:\n\n"
        "OPELLA (SANOFI CHC) - Global Insights Manager, Duclolax & Essentiale (12 months, 2024-2025)\n"
        "• Promoted consumer-focused approach within teams, liaising with internal departments to understand and respond to consumer needs\n"
        "• Coordinated research activities across marketing and digital departments for strategic alignment and efficient resource use\n"
        "• Managed insights for digital-first strategies and supported integration across the consumer experience spectrum\n"
        "• Synthesized data from diverse sources to develop insights fostering competitive growth and strategic decisions\n"
        "• Implemented agile methodologies and contributed to global consumer insight efforts, supporting cross-functional teams\n\n"
        
        "DANONE - Global Brand Innovation Manager, Volvic (6 months, 2024)\n"
        "• Managed innovation pipeline, supported countries, and identified synergies across global markets\n"
        "• Led cross-functional teams to deliver multi-year innovation initiatives by identifying consumer insights\n"
        "• Analyzed market research, developed concept and launch materials, benchmarked internal and external innovation trends\n"
        "• Briefed agencies on execution & delivery of toolkits, coordinated with suppliers & stakeholders\n"
        "• Automated internal financial management processes, reducing time spent by more than 50%\n\n"
        
        "L'ORÉAL - Assistant Project Manager Europe Zone, CeraVe (6 months, 2023)\n"
        "• Developed monthly performance reports for CeraVe and competitors across 10 countries and 7 different categories\n"
        "• Drove business growth by more than 85% through comprehensive dashboard creation and analysis\n"
        "• Led AntiAgeing and Suncare market analysis projects to identify growth opportunities\n"
        "• Aggregated pricing data for 100 SKUs across 4 categories to support new product launch pricing strategies\n"
        "• Conducted ad-hoc competitor analysis for DMI, Brand Managers, and General Managers\n\n"
        
        "COMMUNITY LEADERSHIP:\n"
        "UTOPIA ESSEC - Founding Member & Head of Events (12 months, 2024)\n"
        "• Founded and led France's largest student-led AI association\n"
        "• Hosted Healthcare x AI event with biotech startup founder, Sanofi Director, and VC partner (100+ attendees)\n"
        "• Organized events, hackathons, and workshops focused on entrepreneurial endeavors (average 100 attendees per event)\n\n"
        
        "Kula Connect - Founding Member & Head of Startups (6 months, 2024)\n"
        "• Community fostering connections between India and Europe\n"
        "• Grew community to 1600+ members across Paris, Milan, and Amsterdam\n"
        "• Organized 3 international events\n"
        "• Focus: Covered stories of Indian Entrepreneurs in France\n\n"
        
        "CORE VALUES & APPROACH:\n\n"
        "AMBITIOUS & DARING:\n"
        "• Founded France's largest student-led AI association from scratch\n"
        "• Built Just Build It with vision to create $100B company\n"
        "• Consistently takes on challenging roles across different industries (Healthcare, Food, Cosmetics)\n"
        "• Led high-impact projects delivering 85%+ business growth\n"
        "• Organized major events securing significant sponsorships from top tech companies\n\n"
        
        "HUMBLE & COLLABORATIVE:\n"
        "• Promotes consumer-focused approaches within teams\n"
        "• Excels at cross-functional collaboration and stakeholder coordination\n"
        "• Values learning from diverse sources and synthesizing insights for strategic decisions\n"
        "• Builds communities that bring people together around shared interests\n"
        "• Focus on team success over individual recognition\n\n"
        
        "INNOVATION & GROWTH MINDSET:\n"
        "• Passionate about AI and automation (founding member of AI association)\n"
        "• Consistently identifies growth opportunities and implements strategic recommendations\n"
        "• Automated processes to improve efficiency (50%+ time reduction achievements)\n"
        "• Benchmarks internal and external innovation trends to stay ahead\n"
        "• Uses cutting-edge tools like Lovable for MVP development\n\n"
        
        "EXECUTION EXCELLENCE:\n"
        "• Proven track record delivering results across different roles and industries\n"
        "• Strong analytical skills creating comprehensive dashboards and reports\n"
        "• Implements agile methodologies supporting rapid project execution\n"
        "• Experience managing large-scale events (500+ participants, 1M+ INR budgets)\n"
        "• Successfully coordinates complex projects across multiple countries\n\n"
        
        "TECHNICAL SKILLS:\n"
        "• Programming: Python, R, SQL, Machine Learning, Data Science\n"
        "• Tools: Microsoft Office Suite, N8N for automation, Lovable for MVP development\n"
        "• Analytics: Advanced Excel, dashboard creation, market research analysis\n"
        "• Project Management: Agile methodologies, cross-functional team leadership\n\n"
        
        "PERSONAL INTERESTS & ACTIVITIES:\n\n"
        "ENDURANCE ATHLETE:\n"
        "• Passionate about endurance sports and maintaining peak physical fitness\n"
        "• Has run more than 1000km in the last 12 months\n"
        "• Currently training for Ladakh Half Marathon - the world's highest half marathon\n"
        "• Uses athletic discipline and goal-setting mindset in professional endeavors\n"
        "• Certified Nutrition and Training Coach - operated coaching business for 8 months\n\n"
        
        "CONTENT CREATOR & THOUGHT LEADER:\n"
        "• Active on LinkedIn and Instagram with consistent content creation\n"
        "• Generated 400K+ impressions in the last 12 months through strategic writing\n"
        "• Runs Substack newsletter '1% Better' - weekly reflections on life experiences\n"
        "• Shares insights on entrepreneurship, personal development, and professional growth\n"
        "• Combines analytical thinking with creative expression in content\n\n"
        
        "COMMUNITY BUILDER:\n"
        "• Founded and leads multiple communities (Utopia ESSEC, Kula Connect, Just Build It)\n"
        "• Organizes events bringing people together around shared ambitious goals\n"
        "• Values collaboration and learning from diverse perspectives\n"
        "• Focuses on creating environments where people can achieve extraordinary results\n"
        "• International community building spanning Paris, Milan, Amsterdam\n\n"
        
        "CONTINUOUS LEARNER:\n"
        "• Currently learning Japanese (expanding his 6-language repertoire)\n"
        "• Stays current with technology trends, especially AI and automation\n"
        "• Combines academic excellence from top institutions with practical application\n"
        "• Always experimenting with new tools, technologies, and methodologies\n"
        "• Cross-cultural learning from European and Asian business environments\n\n"
        
        "CULTURAL BRIDGE & GLOBAL PERSPECTIVE:\n"
        "• Multilingual abilities enabling deep cross-cultural understanding\n"
        "• Experience bridging European and Asian markets and business cultures\n"
        "• Comfortable working in diverse, international environments\n"
        "• Brings unique perspective combining Eastern and Western business approaches\n"
        "• Understands nuances of different consumer behaviors across cultures\n\n"
        
        "KEY ACHIEVEMENTS & METRICS:\n"
        "• Drove 85%+ business growth at L'Oréal through strategic analysis\n"
        "• Reduced operational time by 50%+ through process automation at Danone\n"
        "• Organized events with 100+ attendees consistently\n"
        "• Secured 10K€+ in corporate sponsorships for community events\n"
        "• Built communities reaching 1600+ members across multiple countries\n"
        "• Generated 400K+ social media impressions through thought leadership\n"
        "• Managed projects spanning 10+ countries and multiple stakeholder groups\n\n"
        
        "PERSONALITY & WORKING STYLE:\n"
        "• Big ambition combined with humility - confident without arrogance\n"
        "• Curious and asks thoughtful questions to understand problems deeply\n"
        "• Daring in taking on challenges but humble in approach and collaboration\n"
        "• Professional yet personable - builds strong relationships across hierarchies\n"
        "• Data-driven decision making combined with creative problem-solving\n"
        "• Natural leader who empowers others and builds consensus\n"
        "• Adaptable and thrives in dynamic, fast-changing environments"
    )

def call_anthropic_api(question):
    """Direct API call to Anthropic with comprehensive context"""
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    
    if not api_key:
        return "API key not configured"
    
    # DEBUG: Print API key info
    print(f"API key exists: {api_key is not None}")
    print(f"API key length: {len(api_key) if api_key else 0}")
    print(f"API key starts correctly: {api_key.startswith('sk-ant-api03') if api_key else False}")
    
    # Get comprehensive context
    context = get_comprehensive_context()
    
    # Create professional prompt for VCs/HRs
    prompt = (
        f"You are Satvik Puti's personal AI assistant, designed specifically for VCs, HR professionals, and potential business partners.\n\n"
        f"PERSONALITY: Embody Satvik's approach - big ambition, daring, but humble. Be professional yet personable, confident without arrogance.\n\n"
        f"COMPREHENSIVE CONTEXT ABOUT SATVIK:\n{context}\n\n"
        f"RESPONSE GUIDELINES:\n"
        f"1. Answer ONLY based on the provided context about Satvik\n"
        f"2. For company value questions: Focus on specific achievements, cross-industry experience, and proven results\n"
        f"3. For personal questions: Show his well-rounded nature while maintaining professionalism\n"
        f"4. For values questions: Draw from demonstrated actions and concrete examples\n"
        f"5. If specific information isn't available: 'I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly link: https://calendly.com/satvikputi/brainstorming'\n"
        f"6. Keep responses engaging, professional, and backed by concrete examples\n"
        f"7. Never fabricate information - stick to facts from the context\n"
        f"8. Think creatively about how Satvik's experience could apply to the question\n\n"
        f"QUESTION: {question}\n\n"
        f"Provide a thoughtful, professional response that showcases Satvik's value:"
    )
    
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
                'model': 'claude-3-5-sonnet-20241022',
                'max_tokens': 400,
                'messages': [
                    {'role': 'user', 'content': prompt}
                ]
            },
            timeout=30
        )
        
        # DEBUG: Print response details
        print(f"Anthropic API Status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Anthropic API call successful")
            return data['content'][0]['text']
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"Error response: {response.text}")
            return "I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly link: https://calendly.com/satvikputi/brainstorming"
            
    except Exception as e:
        print(f"❌ Request exception: {e}")
        return "I'm having trouble processing that request. I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly link: https://calendly.com/satvikputi/brainstorming"

@app.route('/')
def home():
    return jsonify({
        "status": "Satvik AI Backend is running!",
        "message": "Advanced AI assistant with comprehensive context and direct API calls",
        "features": [
            "Comprehensive professional profile",
            "Smart context selection",
            "Professional responses for VCs/HRs",
            "Direct Anthropic API integration"
        ]
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
        
        print(f"Processing question: {question}")
        
        # Get AI response with comprehensive context
        answer = call_anthropic_api(question)
        
        print(f"Response generated successfully")
        return jsonify({"answer": answer})
        
    except Exception as e:
        print(f"Error in ask endpoint: {e}")
        return jsonify({
            "answer": "I'm having trouble processing that request. I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly link: https://calendly.com/satvikputi/brainstorming"
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)