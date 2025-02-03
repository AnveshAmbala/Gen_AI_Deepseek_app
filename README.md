
# AI Coding Assistant with Deepseek r1 Distilled Model

## Overview
This project is an AI-powered chat application built using **Streamlit**, **LangChain**, and **Ollama**. It leverages the **Deepseek r1 distilled model** with 1.5 billion parameters to provide intelligent coding assistance. Users can interact with the app to get code suggestions, debug errors, receive explanations on best practices, and more.

## Features
- Intelligent Code Suggestions: Get relevant code snippets based on your input.
- Debugging & Error Analysis: Identify and fix bugs in your code with helpful insights.
- Code Documentation: Receive auto-generated documentation and coding best practices.
- Optimized Solution Design: Get recommendations on more efficient ways to solve coding problems.

## Tech Stack
- Streamlit: For creating the interactive web UI.
- LangChain: A framework for building language model applications.
- Ollama: A tool for integrating AI models.
- Deepseek r1 Model: AI model with 1.5 billion parameters used for generating responses.

## Installation

### Prerequisites
Ensure you have Python 3.7+ installed, and the following libraries:

1. Streamlit
2. LangChain
3. Ollama
4. re (regular expressions for cleaning the response)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-coding-assistant.git
   cd ai-coding-assistant
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. The application will open in your default browser.

## Code Overview

### User Interface
- Streamlit is used to create a clean, user-friendly interface with dark mode and modern design elements.
- The sidebar allows users to select between different Deepseek models and provides information about the features of the app.

### AI Model Integration
- The AI model is powered by **Deepseek r1** with **Ollama** integration.
- The model can provide intelligent code suggestions, debugging, and more.

### Prompt Chain Logic
The code uses a **prompt chain** to structure the conversation:
- **SystemMessagePromptTemplate**: Initial instructions for the AI to act as a coding assistant.
- **HumanMessagePromptTemplate**: Handles the user input.
- **AIMessagePromptTemplate**: Handles the AI's response.

### Response Processing
The AI's response is processed by removing unnecessary tags using regular expressions to ensure clean output.

## Running the Application
1. After setting up the application as described above, open a terminal and navigate to the project folder.
2. Use the following command to run the app:
   ```bash
  

3. You should now be able to interact with the AI assistant via your web browser.

## Demo
You can watch a demo of the application in action here:  
[Demo Video Link](insert demo link)

## Contributing
Feel free to fork this repository and contribute by creating issues, submitting pull requests, or improving documentation.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- **LinkedIn**: [Your LinkedIn Profile](insert LinkedIn URL)
- **Email**: [Your Email](insert email)
```

I’ve removed the Markdown ** for bold formatting and fixed the text styling. You can now preview it without issues. Let me know if you need any other adjustments!
