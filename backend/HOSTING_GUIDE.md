# 🚀 Hosting Guide - Intelligent Bible Assistant

## Why Host on HTTPS?

Microphone access requires a **secure HTTPS connection**. Local development won't work for speech recognition.

## Free Hosting Options

### 1. **Render** (Recommended - Free Tier)
- **URL**: https://render.com
- **Free Tier**: 750 hours/month
- **HTTPS**: Automatic
- **Deployment**: Easy Git integration

#### Setup Steps:
1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Connect to Render**:
   - Sign up at render.com
   - Click "New Web Service"
   - Connect your GitHub repo
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python app.py`
   - Add environment variables:
     - `GEMINI_API_KEY`: Your Gemini API key
     - `BIBLE_API_KEY`: a1692756d99fab00256e70dbda406cc7

### 2. **Railway** (Alternative - Free Tier)
- **URL**: https://railway.app
- **Free Tier**: $5 credit monthly
- **HTTPS**: Automatic
- **Deployment**: Very simple

#### Setup Steps:
1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Deploy**:
   ```bash
   railway login
   railway init
   railway up
   ```

3. **Add Environment Variables**:
   ```bash
   railway variables set GEMINI_API_KEY=your_key_here
   railway variables set BIBLE_API_KEY=a1692756d99fab00256e70dbda406cc7
   ```

### 3. **Heroku** (Legacy - Free Tier Discontinued)
- **URL**: https://heroku.com
- **Cost**: $7/month minimum
- **HTTPS**: Automatic
- **Deployment**: Git-based

## Required Files for Hosting

### 1. **Procfile** (for Heroku/Railway)
Create `Procfile` in the backend directory:
```
web: python app.py
```

### 2. **Runtime.txt** (for Python version)
Create `runtime.txt` in the backend directory:
```
python-3.11.0
```

### 3. **Update app.py** for Production
Add this to the bottom of `app.py`:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

## Environment Variables Setup

### For Render:
1. Go to your service dashboard
2. Click "Environment"
3. Add these variables:
   ```
   GEMINI_API_KEY=your_actual_gemini_api_key
   BIBLE_API_KEY=a1692756d99fab00256e70dbda406cc7
   FLASK_ENV=production
   ```

### For Railway:
```bash
railway variables set GEMINI_API_KEY=your_actual_gemini_api_key
railway variables set BIBLE_API_KEY=a1692756d99fab00256e70dbda406cc7
railway variables set FLASK_ENV=production
```

## Custom Domain (Optional)

### Render:
1. Go to your service dashboard
2. Click "Settings" → "Custom Domains"
3. Add your domain
4. Update DNS records

### Railway:
1. Go to your project dashboard
2. Click "Settings" → "Domains"
3. Add custom domain

## Testing Your Deployment

1. **Check HTTPS**: Your URL should start with `https://`
2. **Test Microphone**: Click the MIC button
3. **Test AI Features**: Ask a question like "What does the Bible say about love?"

## Troubleshooting

### Common Issues:

1. **Microphone Still Not Working**:
   - Ensure you're on HTTPS
   - Check browser permissions
   - Try Chrome browser

2. **App Not Starting**:
   - Check environment variables
   - Verify Python version
   - Check logs in hosting dashboard

3. **API Errors**:
   - Verify Gemini API key is correct
   - Check API quota limits
   - Ensure internet connectivity

## Performance Optimization

### For Better Performance:
1. **Enable Caching**:
   ```python
   from flask_caching import Cache
   cache = Cache(app, config={'CACHE_TYPE': 'simple'})
   ```

2. **Add Rate Limiting**:
   ```python
   from flask_limiter import Limiter
   limiter = Limiter(app, key_func=get_remote_address)
   ```

3. **Compress Responses**:
   ```python
   from flask_compress import Compress
   Compress(app)
   ```

## Security Considerations

1. **Environment Variables**: Never commit API keys to Git
2. **HTTPS Only**: Always use HTTPS in production
3. **Rate Limiting**: Implement to prevent abuse
4. **Input Validation**: Sanitize user inputs

## Monitoring

### Add Health Check Endpoint:
```python
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'llm_status': 'configured' if GEMINI_API_KEY else 'not_configured'
    })
```

---

## Quick Start Checklist

- [ ] Push code to GitHub
- [ ] Set up hosting account (Render/Railway)
- [ ] Connect repository
- [ ] Add environment variables
- [ ] Deploy
- [ ] Test HTTPS and microphone
- [ ] Test AI features
- [ ] Share your live URL!

**Your app will be live at**: `https://your-app-name.onrender.com` (or similar)

---

**Need help?** Check the hosting platform's documentation or community forums! 