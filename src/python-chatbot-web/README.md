# Python Chatbot Web Application

This project is a web-based chatbot application that utilizes the Groq API to provide customer support for an online Japanese snack shop. The application is built using Python and Flask, and it allows users to interact with the chatbot through a web interface.

## Project Structure

```
python-chatbot-web
├── src
│   ├── chatbot.py        # Contains the chatbot logic using the Groq API
│   ├── app.py            # Entry point for the web application
│   ├── templates
│   │   └── index.html    # Main HTML template for the web interface
│   └── static
│       └── style.css     # CSS styles for the web application
├── requirements.txt       # Lists the Python dependencies required for the project
└── README.md              # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd python-chatbot-web
   ```

2. **Create a virtual environment:**
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API key:
   ```
   API_KEY=your_api_key_here
   ```

## Usage

1. **Run the application:**
   ```
   python src/app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

3. **Interact with the chatbot:**
   Use the input field to send messages to the chatbot and receive responses.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.