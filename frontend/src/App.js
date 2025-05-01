// frontend/src/App.js
import React from 'react';
import Canvas from './components/Canvas';
import InfoSection from './components/InfoSection';
import './App.css';

function App() {
  return (
    <div className="page-container">

    <header className="header">
      <div className="header-content">
        <div className="github-left">
          <a
            href="https://github.com/McKlay/DigitRecognizerWebApp"
            target="_blank"
            rel="noopener noreferrer"
            className="github-link"
          >
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"
              alt="GitHub"
              className="github-icon"
            />
            <span className="github-text">Get Code on GitHub</span>
          </a>
        </div>

        <div className="header-center">
          <h1>Hand Digit Recognizer ✍️</h1>
          <p className="subtitle">
            Draw a digit (0–9) and our custom-built neural network will try to guess it!
          </p>
        </div>
      </div>
    </header>

      <main className="content">
        <section className="canvas-card">
          <Canvas />
        </section>

        <section className="info-section">
          <InfoSection />
        </section>
      </main>

      <footer className="footer">
        <p>
          Built with ❤️ using <strong>Python</strong>, <strong>NumPy</strong>, <strong>React</strong>, and <strong>FastAPI</strong> —
          by Clay Mark Sarte
        </p>
        <div className="footer-links">
          <a href="/#">Contact </a>
          <a href="/#">Privacy </a>
          <a href="/#">Blog </a>
          <a href="/#">Careers</a>
        </div>
      </footer>

    </div>
  );
}

export default App;
