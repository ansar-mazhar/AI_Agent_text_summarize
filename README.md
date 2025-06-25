# AI_Agent_text_summarize

📄 AI Text Summarizer (Gemini API)

A simple Python agent that summarizes `.txt` files using Google’s Gemini 1.5 Flash model via the Gemini API.


⚙️ Tech Stack

* Python 3
* Gemini API (1.5 Flash)
* `dotenv` for environment variable management

🚀 How It Works

1. User inputs a file path to a `.txt` file.
2. The script reads the file and sends it to the Gemini model.
3. A summary is generated and displayed in the terminal.

✅ Setup

1. Clone this repo
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Add your API key to a `.env` file

   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the agent

   ```bash
   python summarizer_agent.py
   ```
🧠 Model Used

`gemini-1.5-flash-latest`: Fast, low-latency model ideal for quick summarization tasks. Optimized for real-time use with good cost efficiency.


