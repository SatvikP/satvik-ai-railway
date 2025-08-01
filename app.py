# app.py - CORRECT Anthropic client initialization
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import anthropic

app = Flask(__name__)
CORS(app)

class SatvikAIAssistant:
    def __init__(self):
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        
        # CORRECT way to initialize Anthropic client
        self.client = anthropic.Anthropic(api_key=api_key, http_client=None)
        self.content = self.get_all_content()
    
    def get_all_content(self):
        """Complete content about Satvik"""
        return {
            "about_me": """
SATVIK PUTI - Professional Summary


EDUCATION:
• ESSEC Business School Paris, France - Grande École Master's in Management (#3 Top Master of Science Management) Since 2022
  - Specialized in Consumer Behaviour, Strategy and Management, Entrepreneurship Track
  - Key projects: Market Entry for Le Slip Français, Consumer Research, Growth Strategy for Coachhub
  - Founding member of Utopia (AI Association), responsible for events and hackathons

• M.S. Ramaiah Institute of Technology Bangalore, India - Bachelor of Technology, Information Science and Engineering (2016-2020)
  - Specialized in Machine Learning, Data Science with R and Python, Database Management
  - Tournament Director for Annual Debate Tournament (500 participants, 1M+ INR budget)

BACKGROUND:
Satvik Puti is a founder of Just Build It, a startup that helps people build their own businesses. 
The ambition is to build a 10 person company, $100B company. He is an Indian living in Paris for 3 years. 
He speaks 6 languages, and didn't speak a word of French when he arrived. He is an endurance athlete.
He has run more than 1000km in the last 12 months.
He is currently training for Ladakh Half Marathon - the world's highest half marathon.

TECHNICAL SKILLS:
• Programming: Python, R, SQL, Machine Learning, Data Science
• Tools: Microsoft Office Suite, N8N for automation, Lovable for MVP development
• Languages: English (Bilingual), French (B2-C1), Hindi (Bilingual), Telugu (Native), Japanese (Beginner)
""",

            "experience": """
PROFESSIONAL EXPERIENCE:


Just Build It - Founder (3 months, 2024-2025) START UP EXPERIENCE
• Founded a community for curious people in Paris to build ambitious projects together
• Organised 3 building sessions with more than 50 participants on building MVPs, AI Agents, and full stack applications
• Organised an 8 hour hackathon at Ecole 42 Paris with 100+ participants with more than 10K€ sponsorship from Anthropic, Lovable, Cerebras Systems and Windsurf

OPELLA (SANOFI CHC) - Global Insights Manager, Duclolax & Essentiale (12 months, 2024-2025)
• Promoted consumer-focused approach, liaising with internal departments to understand and respond to consumer needs
• Coordinated research activities across marketing and digital departments for strategic alignment and efficient resource use
• Managed insights for digital-first strategies and supported integration across consumer experience spectrum
• Synthesized data from diverse sources to develop insights fostering competitive growth and strategic decisions
• Implemented agile methodologies and contributed to global consumer insight efforts, supporting cross-functional teams

DANONE - Global Brand Innovation Manager, Volvic (6 months, 2024)
• Managed innovation pipeline, supported countries, and identified synergies across markets
• Led cross-functional teams to deliver multi-year innovation by identifying consumer insights
• Analyzed market research, developed concept and launch materials, benchmarked innovation trends
• Briefed agencies on execution & delivery, coordinated with suppliers & stakeholders
• Automated internal financial management, reducing time spent by more than 50%

L'ORÉAL - Assistant Project Manager Europe Zone, CeraVe (6 months, 2023)
• Developed monthly performance reports for CeraVe and competitors across 10 countries and 7 categories
• Drove business growth by more than 85% through comprehensive dashboard creation and analysis
• Led AntiAgeing and Suncare market analysis to identify growth opportunities and communicate recommendations
• Aggregated pricing data for 100 SKUs across 4 categories to support new product launch pricing strategy
• Conducted ad-hoc competitor analysis for DMI, Brand Managers, and General Managers

UTOPIA ESSEC - Founding Member & Head of Events (12 months, 2024)
• Founded and led France's largest student-led AI association
• Hosted Healthcare x AI event with biotech startup founder, Sanofi Director, and VC partner (100+ attendees)
• Organized events, hackathons, and workshops focused on entrepreneurial endeavors (average 100 attendees per event)

Kula Connect - Founding Member & Head of Startups (6 months, 2024) STARTUP EXPERIENCE
Kula Connect is a community that aims to foster stronger connections between India and Europe by uniting individuals and facilitating networking, exchange of ideas and collaboration. We grew the community to +1600 members and organised 3 events across Paris, Milan and Amsterdam.
My Focus: Covered stories of Indian Entrepreneurs in France.
""",

            "values": """
SATVIK'S CORE VALUES & APPROACH:

AMBITIOUS & DARING:
• Founded France's largest student-led AI association (Utopia ESSEC)
• Built "Just Build It" - a startup that started as a community to build ambitious projects together
• Consistently takes on challenging roles across different industries (Healthcare, Food, Cosmetics)
• Led high-impact projects that drove business growth (85%+ at L'Oréal)
• Organized major events with significant sponsorship (10K€+ from top tech companies)

HUMBLE & COLLABORATIVE:
• Focuses on promoting consumer-focused approaches within teams
• Excels at liaising with internal departments and cross-functional collaboration
• Coordinates effectively with multiple stakeholders including suppliers, agencies, and international teams
• Values learning from diverse sources and synthesizing insights for strategic decisions
• Building communities that bring people together around shared interests

INNOVATION & GROWTH MINDSET:
• Passionate about AI and automation (founding member of AI association, uses automation tools)
• Consistently identifies growth opportunities and implements strategic recommendations
• Automated processes to improve efficiency (reduced financial management time by 50%+)
• Benchmarks internal and external innovation trends to stay ahead
• Uses cutting-edge tools like Lovable for MVP development

EXECUTION EXCELLENCE:
• Proven track record of delivering results across different roles and industries
• Strong analytical skills with ability to create comprehensive dashboards and reports
• Implements agile methodologies and supports rapid project execution
• Tournament Director experience managing large-scale events (500+ participants, 1M+ INR budget)
• Successfully managed complex projects across multiple countries and stakeholders

CONTINUOUS LEARNING:
• Multilingual abilities (6 languages) showing adaptability and learning agility
• Cross-cultural experience bridging European and Asian markets
• Constantly expanding skills from technical (Python, R, ML) to business (strategy, innovation)
• Academic excellence at top institutions combined with practical application
""",

            "personal": """
WHAT SATVIK DOES WHEN NOT WORKING:

ENDURANCE ATHLETE:
• Passionate about endurance sports and maintaining physical fitness
• Has run more than 1000km in the last 12 months
• Currently training for Ladakh Half Marathon - the world's highest half marathon
• Uses athletic discipline and goal-setting mindset in professional endeavors
• Believes in pushing personal boundaries and continuous improvement
• Certified Nutrition and Training Coach - ran a coaching business for 8 months

CONTENT CREATOR & THOUGHT LEADER:
• Enjoys writing and making videos on LinkedIn and Instagram
• Got more than 400K impressions in the last 12 months through consistent writing
• Runs a Substack - "1% Better" - weekly reflections from his life experiences
• Shares insights on entrepreneurship, personal development, and professional growth
• Combines creativity with analytical thinking in content creation

COMMUNITY BUILDER:
• Building "Just Build It!" - a community where curious people in Paris build ambitious projects together
• Organizes events and brings people together around shared interests
• Founded and leads multiple communities (Utopia ESSEC, Kula Connect, Just Build It)
• Values collaboration and learning from diverse perspectives
• Focuses on creating environments where people can achieve ambitious goals together

CONTINUOUS LEARNER: 
• Currently learning Japanese (adding to his 6-language repertoire)
• Stays current with technology trends, especially AI and automation
• Combines academic learning (from top institutions) with practical application
• Sports and Health Geek with deep knowledge of nutrition and training
• Always experimenting with new tools and technologies

CULTURAL BRIDGE:
• Multilingual with deep understanding of both European and Asian markets
• Brings cross-cultural perspectives to business challenges
• Comfortable working in international, diverse environments
• Has built communities spanning multiple countries (Paris, Milan, Amsterdam)
• Understands the nuances of different business cultures and consumer behaviors

The combination of athletic discipline, creative expression, community building, and continuous learning reflects Satvik's well-rounded approach to both professional and personal growth.
"""
        }
    
    def find_relevant_content(self, question):
        """Smart content selection based on question"""
        question_lower = question.lower()
        relevant_sections = []
        
        # Keywords for different content types
        content_keywords = {
            "about_me": ["background", "education", "skills", "experience", "qualifications", "bio", "who is"],
            "experience": ["work", "job", "career", "professional", "company", "role", "position", "projects"],
            "values": ["values", "approach", "personality", "character", "beliefs", "principles", "mindset"],
            "personal": ["personal", "hobbies", "interests", "not working", "free time", "athlete", "content", "community"]
        }
        
        # Company value questions get comprehensive content
        if ("company" in question_lower and "value" in question_lower) or "hire" in question_lower or "benefit" in question_lower:
            relevant_sections = [self.content["about_me"], self.content["experience"], self.content["values"]]
        else:
            # Score each content section based on keyword matches
            section_scores = {}
            for section, keywords in content_keywords.items():
                score = sum(1 for keyword in keywords if keyword in question_lower)
                if score > 0:
                    section_scores[section] = score
            
            # Select top scoring sections
            if section_scores:
                sorted_sections = sorted(section_scores.items(), key=lambda x: x[1], reverse=True)
                top_sections = [section for section, score in sorted_sections[:2]]
                relevant_sections = [self.content[section] for section in top_sections]
            else:
                # Default to about_me for general questions
                relevant_sections = [self.content["about_me"]]
        
        return "\n\n".join(relevant_sections)
    
    def get_response(self, question):
        """Get AI response using Claude"""
        try:
            # Find relevant content
            relevant_content = self.find_relevant_content(question)
            
            # Create professional prompt
            prompt = f"""You are Satvik Puti's personal AI assistant, designed for VCs, HR professionals, and potential business partners.

PERSONALITY: Embody Satvik's approach - big ambition, daring, but humble. Be professional yet personable, confident without arrogance.

CONTEXT ABOUT SATVIK:
{relevant_content}

RESPONSE GUIDELINES:
1. Answer ONLY based on the provided context about Satvik
2. For company value questions: Focus on specific achievements, cross-industry experience, and proven results
3. For personal questions: Show his well-rounded nature while maintaining professionalism  
4. For general questions: Provide comprehensive information that showcases his capabilities
5. If specific information isn't available: "I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly link: https://calendly.com/satvikputi/brainstorming"
6. Keep responses engaging and backed by concrete examples from his experience
7. Never fabricate information - stick to facts from the context
8. Think creatively about how Satvik's experience could apply to the question being asked

QUESTION: {question}

Provide a thoughtful, professional response that showcases Satvik's value:"""
            
            # CORRECT way to call Claude API
            message = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Handle API response properly
            if message.content and len(message.content) > 0:
                return message.content[0].text
            else:
                return "I'm having trouble processing that request. I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly link: https://calendly.com/satvikputi/brainstorming"
            
        except Exception as e:
            print(f"Error in get_response: {e}")
            return "I'm having trouble processing that request. I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly link: https://calendly.com/satvikputi/brainstorming"

# Initialize the assistant
assistant = None
try:
    assistant = SatvikAIAssistant()
    print("✅ Satvik AI Assistant initialized successfully!")
except Exception as e:
    print(f"❌ Failed to initialize assistant: {e}")

@app.route('/')
def home():
    status = "running" if assistant else "error"
    return jsonify({
        "status": f"Satvik AI Backend is {status} on Railway!",
        "message": "Advanced AI assistant with full content and Claude integration"
    })

@app.route('/api/ask', methods=['POST', 'OPTIONS'])
def ask():
    if request.method == 'OPTIONS':
        return '', 200
    
    if not assistant:
        return jsonify({
            "answer": "AI assistant not available. Please check configuration."
        }), 500
    
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({"answer": "Please provide a question about Satvik."})
        
        # Get AI response
        answer = assistant.get_response(question)
        return jsonify({"answer": answer})
        
    except Exception as e:
        return jsonify({
            "answer": "I'm having trouble processing that request. I'd recommend booking a call with Satvik to discuss this directly. Here's his Calendly link: https://calendly.com/satvikputi/brainstorming"
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)