import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchEvents = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/events');
      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }
      const data = await response.json();
      setEvents(data.events);
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  useEffect(() => {
    // Fetch events initially
    fetchEvents();

    // Set up polling interval (every 5 seconds)
    const interval = setInterval(() => {
      fetchEvents();
    }, 5000);

    // Clean up interval on component unmount
    return () => clearInterval(interval);
  }, []);

  const refreshData = () => {
    fetchEvents();
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Live ASIC Lab Monitor</h1>
        <button className="refresh-button" onClick={refreshData}>
          Refresh
        </button>
      </header>

      <main className="content">
        {loading && <div className="loading">Loading events...</div>}
        
        {error && <div className="error">Error: {error}</div>}
        
        {!loading && !error && events.length === 0 && (
          <div className="no-events">No events recorded yet</div>
        )}
        
        {!loading && !error && events.length > 0 && (
          <div className="events-container">
            <h2>Recent Activity</h2>
            <ul className="events-list">
              {events.map((event, index) => (
                <li key={index} className="event-item">
                  <span className="timestamp">{event.time}</span>
                  <span className="message">{event.message}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
      </main>
    </div>
  );
}

export default App; 