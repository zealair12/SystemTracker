# SystemTracker
Real-time monitoring interface for VLSI Physical Design workflows.

## Project Overview
This project creates a real-time tracking dashboard that simulates monitoring of automated systems (e.g., servers running chip design tasks). It's built with a Python (Flask) backend, Perl for log simulation, and a React/JavaScript frontend.

## Tech Stack
- **Backend**: Python Flask with REST API
- **Frontend**: React (JavaScript/JSX)
- **Simulation**: Perl script to generate mock log entries
- **Data Format**: JSON via HTTP/REST

## Project Structure
```
SystemTracker/
├── backend/               # Flask API
│   ├── app.py            # Main Flask application
│   ├── simulate.pl       # Perl script for log generation
│   └── requirements.txt  # Python dependencies
└── frontend/             # React frontend
    └── pd-dashboard/     # React application
        ├── public/       # Static assets
        └── src/          # React components
```

## Development Log

### Day 1
- Initialized repository
- Cloned project
- Revised git basics
- Set up project structure
- Created backend with Flask API
- Implemented Perl script for log simulation
- Created React frontend for dashboard

## Setup Instructions

### Backend Setup
1. Navigate to the backend directory:
   ```
   cd backend
   ```
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```
   python app.py
   ```
   The API will be available at `http://localhost:5000`

### Frontend Setup
1. Navigate to the React app directory:
   ```
   cd frontend/pd-dashboard
   ```
2. Install Node.js dependencies:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm start
   ```
   The application will be available at `http://localhost:3000`

## API Endpoints

- **GET /api/hello**: Test endpoint returning a simple greeting
- **GET /api/events**: Returns all events and generates a new random event

## Features
- Real-time monitoring of simulated VLSI Physical Design tasks
- Automatic updates every 5 seconds
- Manual refresh option
- Displays timestamps and machine activity

## Future Improvements
- Add authentication
- Implement WebSockets for true real-time updates
- Add filtering and search capabilities
- Integrate with real log sources