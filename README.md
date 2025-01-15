# Sentiment Analysis App

A simple web application for performing sentiment analysis on text input. The app has two main components:

1. **Frontend**: Built with React.
2. **Backend**: Powered by Python, FastAPI, and Hugging Face Transformers.

---

## Features

- Analyze text sentiment (Positive/Negative/Neutral).
- Confidence score for the sentiment analysis.
- Interactive and user-friendly UI.

---

## Prerequisites

### General Requirements

- **Node.js** (version 16+)
- **Python** (version 3.8+)
- **Virtual Environment** (recommended)

### Python Libraries

- `fastapi`
- `uvicorn`
- `transformers`
- `pydantic`
- `pytest` (for testing)

### React Libraries

- `axios`

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/thefutureseer/python_sentiment_analysis.git
cd python_sentiment_analysis
```

### 2. Backend Setup

#### Navigate to the backend directory:
```bash
cd sentiment-backend
```

#### Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate   # Windows
```

#### Install Python dependencies:
```bash
pip install -r requirements.txt
```

#### Run the FastAPI server:
```bash
uvicorn main:app --reload
```
The backend will start on `http://127.0.0.1:8000`.

### 3. Frontend Setup

#### Navigate to the frontend directory:
```bash
cd python_sentiment_analysis [root]
```

#### Install Node.js dependencies:
```bash
npm install
```

#### Start the React development server:
```bash
npm start
```
The frontend will start on `http://localhost:3000`.

---

## Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Enter text in the input box and click "Analyze Sentiment."
3. View the sentiment results, including the confidence score.

---

## File Structure

```
python_sentiment_analysis root directory/
│
├── sentiment-backend/       # Backend code (FastAPI)
│   ├── main.py              # FastAPI entry point
│   ├── models.py            # Pydantic models
│   ├── requirements.txt     # Python dependencies
│   ├── test_main.py         # Unit tests for the backend
│
├── # Frontend code (React)
|-- public
│── src/
│   ├── App.js           # Main React component
│   ├── index.js         # React entry point
│── package.json         # Node.js dependencies
│
└── README.md                # Project documentation
```

---

## Running Tests

### Backend Tests
Ensure your virtual environment is active, then run:
```bash
python3 -m unittest test_main.py
```

### Frontend Tests
Add tests as needed using your preferred testing framework (e.g., Jest, React Testing Library).

---

## Deployment

### Backend
- Deploy using services like AWS, Azure, Heroku, or Render.

### Frontend
- Build the production-ready files using:
  ```bash
  npm run build
  ```
- Deploy using Vercel, Netlify, or any other static site hosting service.

---

## Future Enhancements

- Add more detailed error handling.
- Implement support for other languages.
- Enhance UI with additional features.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for backend framework.
- [Hugging Face](https://huggingface.co/) for sentiment analysis models.
- [React](https://reactjs.org/) for frontend development.