import React, { useRef, useState, useEffect } from 'react';
import axios from 'axios';
import './Canvas.css';

const Canvas = () => {
  const canvasRef = useRef(null);
  const [prediction, setPrediction] = useState(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const ctx = canvasRef.current.getContext('2d');
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasRef.current.width, canvasRef.current.height);
  }, []);

  const startDrawing = (e) => {
    const ctx = canvasRef.current.getContext('2d');
    ctx.lineWidth = 20;
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'black';
    ctx.beginPath();
    ctx.moveTo(getOffsetX(e), getOffsetY(e));
    setIsDrawing(true);
  };

  const draw = (e) => {
    if (!isDrawing) return;
    const ctx = canvasRef.current.getContext('2d');
    ctx.lineTo(getOffsetX(e), getOffsetY(e));
    ctx.stroke();
  };

  const stopDrawing = () => setIsDrawing(false);
  const getOffsetX = (e) => e.nativeEvent.offsetX ?? e.touches[0].clientX - canvasRef.current.getBoundingClientRect().left;
  const getOffsetY = (e) => e.nativeEvent.offsetY ?? e.touches[0].clientY - canvasRef.current.getBoundingClientRect().top;

  const clearCanvas = () => {
    const ctx = canvasRef.current.getContext('2d');
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasRef.current.width, canvasRef.current.height);
    setPrediction(null);
  };

  const predictDigit = async () => {
    setLoading(true);
    const canvas = canvasRef.current;
    canvas.toBlob(async (blob) => {
      const formData = new FormData();
      formData.append('file', new File([blob], 'digit.png'));
      try {
        const res = await axios.post('https://digitrecognizerwebapp-production.up.railway.app/predict/', formData);
        setPrediction(res.data.prediction);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    });
  };

  return (
    <div className="digit-wrapper">
      <p className="subtitle">Draw and click Predict</p>
      <div className="canvas-container">
        <canvas
          ref={canvasRef}
          width={280}
          height={280}
          onMouseDown={startDrawing}
          onMouseMove={draw}
          onMouseUp={stopDrawing}
          onMouseLeave={stopDrawing}
          onTouchStart={startDrawing}
          onTouchMove={draw}
          onTouchEnd={stopDrawing}
        />
        <div className="button-group">
          <button onClick={predictDigit} disabled={loading}>
            {loading ? 'Predicting...' : 'Predict'}
          </button>
          <button onClick={clearCanvas}>Clear</button>
        </div>
        {prediction !== null && (
          <div className="prediction-box">
            <h3>Prediction</h3>
            <p className="result">{prediction}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Canvas;
