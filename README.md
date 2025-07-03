# 🧠 Chat With Gemini-Pro 

A lightweight Streamlit-based chatbot powered by Google's Gemini Pro model.
Click [here](https://geminipro-aibot.streamlit.app/) to acess the Streamlit Web App
##Features

- Chat interface using Streamlit's `chat_input` and `chat_message`
- Integrated with Google Generative AI (`gemini-pro`)
- Environment variables managed via `.env` and `python-dotenv`
- Custom UI config via `.streamlit/config.toml`

##Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/ara2102/Gemini-Pro-Streamlit-Chatbot.git
   cd Gemini-Pro-Streamlit-Chatbot
   ```
2. **Create a virtual environment**
   ```bash
   conda create -n ML python=3.12
   conda activate ML
   ```

4. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```
5. **Set your Google API key**
```python
GOOGLE_API_KEY=your_api_key_here
```
6. **Run the App**
```bash
streamlit run main.py
```
