# Oracle

This project presents a voice-activated chatbot that harnesses the power of OpenAI's GPT-3.5 model as its language model. It employs OpenAI's Whisper API for speech-to-text conversion and Google Cloud's Text-to-Speech engine for vocalizing responses. The application is designed to listen to user's verbal inputs, translate the spoken sentences into text, and feed it to the GPT-3 model to generate a response. This response is then transformed into audible speech.

## Project Structure

The project consists of three main Python files:

1. `app.py`: This is the main file which initializes the microphone for capturing user inputs and runs an infinite loop for continuous interaction with the user. It also handles the conversation flow and integrates the speech-to-text and text-to-speech functionalities.

2. `chat.py`: This file defines the function for generating the assistant's responses using OpenAI's GPT-3 model.

3. `tts.py`: This file handles the text-to-speech conversion of the assistant's responses using Google's Text-to-Speech API.

## Setup and Installation

Before running the project, make sure to install the required dependencies with the following command:

```bash
pip install -r requirements.txt
```

The project requires API keys for OpenAI and Google Cloud. You must create `.env` file in the project root directory with the following keys:

```dotenv
OPENAI_API_KEY=your_openai_key
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_cloud_keyfile.json
```

Replace `your_openai_key` and `path_to_your_google_cloud_keyfile.json` with your actual OpenAI API key and the path to your Google Cloud key file.

## Usage

To start the assistant, simply run:

```bash
python app.py
```

Speak into your microphone after running the command. The assistant will listen to your speech, convert it to text, generate a response, and then vocalize the response.

## Contributions

Contributions to this project are welcome. Please feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the terms of the MIT license.
