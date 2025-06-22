#!/usr/bin/env python3
"""
Setup script for Intelligent Bible Assistant
This script helps you configure your Gemini API key
"""

import os
import sys

def create_env_file():
    """Create .env file with user input"""
    print("🤖 Intelligent Bible Assistant Setup")
    print("=" * 40)
    
    # Check if .env already exists
    if os.path.exists('.env'):
        print("⚠️  .env file already exists!")
        overwrite = input("Do you want to overwrite it? (y/N): ").lower()
        if overwrite != 'y':
            print("Setup cancelled.")
            return
    
    print("\n📝 To get your Gemini API key:")
    print("1. Go to https://makersuite.google.com/app/apikey")
    print("2. Sign in with your Google account")
    print("3. Click 'Create API Key'")
    print("4. Copy the generated key")
    print()
    
    gemini_key = input("Enter your Gemini API key (or press Enter to skip): ").strip()
    
    # Create .env content
    env_content = f"""# Bible API Key (using default if not provided)
BIBLE_API_KEY=a1692756d99fab00256e70dbda406cc7

# Gemini AI API Key - Get yours from https://makersuite.google.com/app/apikey
GEMINI_API_KEY={gemini_key}

# Flask Environment
FLASK_ENV=development
"""
    
    # Write .env file
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("\n✅ .env file created successfully!")
        
        if gemini_key:
            print("🎉 Gemini AI is now configured!")
            print("You can now run: python app.py")
        else:
            print("⚠️  No Gemini API key provided.")
            print("The app will work for basic Bible searches, but AI analysis will be limited.")
            print("You can add the key later by editing the .env file.")
            
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False
    
    return True

def install_dependencies():
    """Install required Python packages"""
    print("\n📦 Installing dependencies...")
    try:
        os.system("pip install -r requirements.txt")
        print("✅ Dependencies installed successfully!")
        return True
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Welcome to Intelligent Bible Assistant Setup!")
    
    # Create .env file
    if not create_env_file():
        return
    
    # Install dependencies
    install_dependencies()
    
    print("\n🎯 Setup Complete!")
    print("=" * 40)
    print("To start the app:")
    print("1. cd backend")
    print("2. python app.py")
    print("3. Open http://localhost:5000 in your browser")
    print()
    print("For deployment:")
    print("1. Push to GitHub")
    print("2. Deploy on Render.com")
    print("3. Add environment variables in Render dashboard")
    print()
    print("Happy Bible searching! 📖")

if __name__ == "__main__":
    main() 