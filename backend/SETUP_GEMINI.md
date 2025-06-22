# 🔑 Google Gemini API Setup

## Quick Setup Guide

### 1. Get Your Free Gemini API Key

1. **Visit Google AI Studio**: https://makersuite.google.com/app/apikey
2. **Sign in** with your Google account
3. **Click "Create API Key"**
4. **Copy your API key** (it looks like: `AIzaSyC...`)

### 2. Configure Your App

Create a `.env` file in the `backend` directory with:

```env
# Bible API Configuration
BIBLE_API_KEY=a1692756d99fab00256e70dbda406cc7

# Google Gemini AI (Required for LLM features)
GEMINI_API_KEY=your_actual_gemini_api_key_here

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### 3. Replace the Placeholder

Replace `your_actual_gemini_api_key_here` with your actual API key from step 1.

### 4. Run the App

```bash
python app.py
```

## Features You'll Get

✅ **Natural Language Processing**: Ask questions in plain English
✅ **Intelligent Query Refinement**: AI improves your search terms
✅ **Conversational AI**: Remembers context and builds conversations
✅ **Confidence Scoring**: See how reliable the results are
✅ **Voice Interaction**: Speak your questions naturally

## Example Queries

- "What does the Bible say about love?"
- "I remember something about golden lampstands"
- "Tell me about John 3:16"
- "What does Jesus say about forgiveness?"

## Free Tier Limits

- **60 requests per minute**
- **15 million characters per month**
- **Perfect for personal use and testing**

---

**That's it! Your intelligent Bible assistant will be ready to use! 🤖📖** 