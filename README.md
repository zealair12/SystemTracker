# 🤖 Intelligent Bible Assistant

A powerful, AI-powered Bible search and conversation tool that combines natural language processing, speech recognition, and intelligent verse analysis.

## ✨ Features

### 🧠 **Intelligent AI Processing**
- **Natural Language Understanding**: Ask questions in plain English
- **LLM-Powered Analysis**: Google Gemini AI provides intelligent explanations
- **Query Refinement**: AI automatically improves search queries for better results
- **Confidence Scoring**: See how confident the AI is in its responses

### 🎤 **Voice Interaction**
- **Speech Recognition**: Speak your questions naturally
- **Text-to-Speech**: AI responses can be spoken back to you
- **Real-time Processing**: Instant voice-to-text conversion

### 📖 **Advanced Bible Search**
- **Multi-API Integration**: Searches across multiple Bible APIs
- **Smart Context**: Understands partial verses and phrases
- **Conversational Memory**: Remembers your search history
- **Intelligent Filtering**: AI filters and ranks results by relevance

### 💬 **Conversational Interface**
- **Chat-like Experience**: Natural back-and-forth conversations
- **Context Awareness**: AI remembers previous questions
- **Explanatory Responses**: Get detailed explanations of verses found
- **Reasoning Display**: See how the AI arrived at its conclusions

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Modern web browser with speech recognition support
- Google Gemini API key (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd SystemTracker
   ```

2. **Install Python dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Set up API keys**
   ```bash
   # Copy the example environment file
   cp env_example.txt .env
   
   # Edit .env and add your API keys:
   # - Get Gemini API key: https://makersuite.google.com/app/apikey
   # - Bible API key is already included
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   http://localhost:5000
   ```

## 🔧 Configuration

### Required API Keys

1. **Google Gemini AI** (Required for LLM features)
   - Visit: https://makersuite.google.com/app/apikey
   - Create a free account
   - Generate an API key
   - Add to `.env`: `GEMINI_API_KEY=your_key_here`

2. **Bible API** (Already configured)
   - Uses public Bible APIs
   - No additional setup required

### Optional: OpenAI API
- For alternative LLM processing
- Add to `.env`: `OPENAI_API_KEY=your_key_here`

## 💡 Usage Examples

### Natural Language Queries
```
"What does the Bible say about love?"
"I remember something about golden lampstands"
"Tell me about the verse that says 'for God so loved the world'"
"What does Jesus say about forgiveness?"
```

### Voice Commands
- Click the microphone button
- Speak your question naturally
- The AI will process and respond

### Features
- **Intelligent Search**: AI understands context and refines queries
- **Conversational Memory**: Previous questions are remembered
- **Confidence Scoring**: See how reliable the results are
- **Multi-Source Results**: Combines results from multiple Bible APIs

## 🏗️ Architecture

### Backend (Flask)
- **IntelligentBibleSearch**: Core AI-powered search engine
- **LLM Integration**: Google Gemini for natural language processing
- **Multi-API Search**: Biblia.com and Bible API integration
- **Conversation Management**: Maintains chat history and context

### Frontend (HTML/JavaScript)
- **Modern UI**: Clean, responsive design
- **Speech Recognition**: Web Speech API integration
- **Real-time Updates**: Dynamic result display
- **Conversational Interface**: Chat-like user experience

## 🔍 API Endpoints

- `POST /api/intelligent-search` - Main AI-powered search
- `POST /api/speech-to-text` - Process voice input
- `POST /api/text-to-speech` - Generate speech output
- `GET /api/conversation-history` - Get chat history
- `POST /api/clear-history` - Clear conversation history
- `GET /api/health` - Health check

## 🎯 Key Features Explained

### 1. **Natural Language Processing**
The AI understands queries like:
- "I remember something about golden lampstands" → Searches for "golden candlesticks" (KJV term)
- "What does the Bible say about love?" → Searches multiple love-related verses
- "Tell me about John 3:16" → Direct verse lookup with explanation

### 2. **Intelligent Query Refinement**
- User: "I remember something about God loving the world"
- AI: Refines to "for God so loved the world" for better search results
- Returns: John 3:16 with detailed explanation

### 3. **Conversational Context**
- Remembers previous questions
- Builds context over conversation
- Provides relevant follow-up suggestions

### 4. **Confidence Scoring**
- **High**: Exact matches with clear context
- **Medium**: Good matches with some interpretation needed
- **Low**: Approximate matches requiring clarification

## 🛠️ Development

### Adding New Features
1. **New Bible API**: Add to `IntelligentBibleSearch` class
2. **LLM Enhancement**: Modify `process_with_llm` method
3. **UI Improvements**: Update `templates/index.html`

### Testing
```bash
# Test the API
curl -X POST http://localhost:5000/api/intelligent-search \
  -H "Content-Type: application/json" \
  -d '{"query": "What does the Bible say about love?"}'
```

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🆘 Troubleshooting

### Common Issues

1. **Speech Recognition Not Working**
   - Ensure you're using HTTPS or localhost
   - Check browser permissions for microphone
   - Try a different browser (Chrome recommended)

2. **LLM Not Responding**
   - Verify your Gemini API key is correct
   - Check API quota limits
   - Ensure internet connection

3. **No Bible Results**
   - Check internet connection
   - Verify Bible API endpoints are accessible
   - Try different search terms

### Getting Help
- Check the browser console for errors
- Verify all API keys are set correctly
- Ensure all dependencies are installed

---

**Built with ❤️ using Flask, Google Gemini AI, and modern web technologies**