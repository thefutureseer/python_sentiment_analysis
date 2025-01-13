// import logo from './logo.svg';
// import './App.css';
import React, { useState } from "react";
import axios from "axios";

function App() {
  const [inputText, setInputText] = useState("");
  const [result, setResult] = useState(null);

  const analyzeSentiment = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/analyze/", { text: inputText });
      setResult({
        text: inputText, // Add the input text here for display
        sentiment: response.data.label, // Use "label" from the backend response
        score: response.data.score, // Use "score" from the backend response
      });    
    } catch (error) {
      console.error("Error analyzing sentiment:", error);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Sentiment Analysis App</h1>
      <textarea
        rows="4"
        cols="50"
        placeholder="Enter text here..."
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        style={{ marginBottom: "10px", width: "100%" }}
      />
      <br />
      <button onClick={analyzeSentiment} style={{ padding: "10px 20px", cursor: "pointer" }}>
        Analyze Sentiment
      </button>
      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Results:</h2>
          <p><strong>Text:</strong> {result.text}</p>
          <p><strong>Sentiment:</strong> {result.sentiment}</p>
          <p><strong>Confidence Score:</strong> {result.score.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
}

export default App;