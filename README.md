🌟 **Sahridaya Mood Guesser**

🧠 Discover Your Emotional State with Sentiment Analysis

Welcome to Sahridaya Mood Guesser! This app helps you explore your emotions by analyzing responses to various psychological questions. Powered by Hugging Face's DistilBERT model, it identifies positive or negative sentiments in your answers and provides motivational tips to support your well-being. 🌈

✨ **Features**
🕵️‍♂️ Sentiment Analysis: Detects the sentiment of your responses with a Hugging Face DistilBERT model.
🌈 Motivational Tips: Encouraging messages to uplift your mood.
📊 Graphical Visualization: View a bar chart summary of positive and negative responses.
🌐 Helpful Resources: Direct links to external resources for mental health support.
🔄 Restart Feature: Start a new session whenever you like!


🚀 **Getting Started**
🛠️ Prerequisites
1) Make sure you have Python 3.x installed along with these packages:
2) tkinter (usually included with Python)
3) transformers
4) matplotlib

Install missing packages by running:
```
pip install transformers matplotlib

```
 
 💻 **Installation**

```
# Clone this repository:

git clone https://github.com/saisaranya2005/Mood-guesser.git

# Move inside the project directory

cd Mood-guesser

# Run the main application file

python sentimental.py

```
🎉 **Usage**
Start the App: Run the program to open the main window.
Answer the Questions: Type your response and click Next after each question.
View Your Report: After answering, check the sentiment report and graphical summary.
Motivational Tips: Access positive quotes to boost your mood!
Helpful Resources: Click the external link to find more information on mental health.
Restart: Click the "Restart" button to begin a new session if needed.

🔍 **Code Overview**
Sentiment Analysis Pipeline: Utilizes Hugging Face’s DistilBERT model for analyzing sentiments.
Tkinter GUI: Manages buttons, labels, and various pages for results, tips, and graphs.
Matplotlib Visualization: Generates a bar chart summarizing positive and negative response counts.
Motivational Tips: Provides supportive messages and practical guidance.
