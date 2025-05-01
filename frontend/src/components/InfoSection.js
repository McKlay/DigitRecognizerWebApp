import React from 'react';
import './InfoSection.css';

const InfoSection = () => {
  return (
    <div className="info-wrapper">
      <h2>Tech Stack</h2>
      <ul>
        <li><b>Python</b> — for model logic and backend (FastAPI)</li>
        <li><b>NumPy</b> — to build the neural network from scratch</li>
        <li><b>React + Axios</b> — for the frontend and image upload</li>
        <li><b>FastAPI</b> — to serve predictions from the trained model</li>
      </ul>

      <h2>Dataset & Preprocessing</h2>
      <p>The model uses the MNIST dataset, converted to grayscale and resized to <b>28×28</b> pixels. The image is centered using center-of-mass shift for better accuracy.</p>

      <h2>Model Architecture</h2>
      <ul>
        <li><b>Layer 1:</b> Fully connected (784 → 128) with ReLU activation</li>
        <li><b>Layer 2:</b> Fully connected (128 → 10) with Softmax</li>
      </ul>

      <h2>Training & Evaluation</h2>
      <p>Trained using cross-entropy loss and stochastic gradient descent (SGD). Performance is evaluated on test data accuracy.</p>

      <h2>Prediction Pipeline</h2>
      <p>Draw on the canvas → Save as image → Upload to FastAPI → Run through NumPy neural net → Return prediction.</p>

      <h2>Deployment</h2>
      <p>This app is deployable using <b>Railway</b> (for backend) and <b>Vercel</b> (for frontend), fully containerized with free-tier support.</p>

    </div>
  );
};

export default InfoSection;
