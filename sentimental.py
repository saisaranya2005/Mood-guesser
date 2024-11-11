import tkinter as tk
from tkinter import messagebox, Toplevel
from transformers import pipeline
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser
from tkinter import PhotoImage

# Initialize the Hugging Face sentiment-analysis pipeline with DistilBERT
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# List of psychological questions
questions = [
    "How are you feeling today?",
    "Have you been stressed out lately?",
    "Do you often feel sad or low?",
    "Are you sleeping well?",
    "Do you feel motivated to work on your goals?",
    "Have you been enjoying the things you usually like?",
    "Do you find yourself getting anxious frequently?",
    "Are you able to relax easily?",
    "Do you feel supported by the people around you?",
    "How do you feel when you wake up in the morning?"
]

# Motivational tips with GIFs
motivational_tips = [
    "🌞 Start each day with a positive thought to boost your mood.",
    "🌱 Take time to manage your stress, whether through exercise, meditation, or journaling.",
    "🌻 Remember that it's okay to feel low sometimes. Give yourself permission to rest.",
    "💤 A good night's sleep is essential. Try to maintain a consistent sleep schedule.",
    "💪 Focus on your goals one step at a time; small progress is still progress!",
    "🎉 Make time for activities that bring you joy and refresh your spirit.",
    "🌬️ Practice deep breathing exercises to manage anxiety.",
    "🌾 Relaxation is key to maintaining mental clarity; unwind with activities you enjoy.",
    "👫 Surround yourself with people who lift you up and provide support.",
    "🌅 Start your morning with gratitude; it sets a positive tone for the day."
]
# Tkinter UI Setup
root = tk.Tk()
root.title("Psychological Sentiment Analysis")
root.geometry("800x700")
root.config(bg="#e0f7fa")

# Display Title and Description
title_label = tk.Label(root, text="Sahridaya Mood Guesser", font=("Arial", 20, "bold"), bg="#e0f7fa", fg="#2c6e49")
title_label.pack(pady=20)

description_label = tk.Label(root, text="Discover Your Emotional State with Sentiment Analysis", font=("Arial", 14), bg="#e0f7fa", fg="#616161")
description_label.pack(pady=10)

# Initialize variables
current_question_index = 0
sentiment_results = []
positive_count = 0
negative_count = 0

# Function to display the question page
def show_question_page():
    global current_question_index
    question_label.config(text=questions[current_question_index])
    user_input.delete(1.0, tk.END)

# Display a question label
question_label = tk.Label(root, text=questions[current_question_index], font=("Arial", 14), bg="#e0f7fa", wraplength=700)
question_label.pack(pady=20)

# Text input field
user_input = tk.Text(root, height=4, width=60, font=("Arial", 12), bg="#f0f4c3")
user_input.pack(pady=10)

# Function to analyze sentiment and update sentiment results
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Function to handle moving to the next question
def next_question():
    global current_question_index, positive_count, negative_count
    user_text = user_input.get("1.0", tk.END).strip()
    
    if user_text:
        label, score = analyze_sentiment(user_text)
        sentiment_results.append({"question": questions[current_question_index], "label": label, "score": score})
        
        if label == 'POSITIVE':
            positive_count += 1
        else:
            negative_count += 1

        if current_question_index < len(questions) - 1:
            current_question_index += 1
            question_label.config(text=questions[current_question_index])
            user_input.delete(1.0, tk.END)
        else:
            show_report_page()
    else:
        messagebox.showwarning("Input Required", "Please enter a response before moving to the next question.")

# Button for proceeding to the next question
next_button_question = tk.Button(root, text="Next", command=next_question, font=("Arial", 12), bg="#81c784", width=10)
next_button_question.pack(pady=10)

# Function to display the report page in a new window
def show_report_page():
    report_window = Toplevel(root)
    report_window.title("Final Report")
    report_window.geometry("600x500")
    report_text = f"Final Report:\n\nTotal Positive Responses: {positive_count}\nTotal Negative Responses: {negative_count}\n\n"
    
    for idx, result in enumerate(sentiment_results):
        report_text += f"Q{idx + 1}: {result['question']}\nSentiment: {result['label']} | Score: {result['score']:.2f}\n\n"
    
    report_label = tk.Label(report_window, text=report_text, font=("Arial", 12), bg="#e0f7fa", justify="left")
    report_label.pack(pady=20)

# Function to display the motivational tips in a new window
def show_motivational_page():
    motivational_window = Toplevel(root)
    motivational_window.title("Motivational Tips")
    motivational_window.geometry("400x500")
    
    for tip in motivational_tips:
        motivational_label = tk.Label(motivational_window, text=tip, font=("Arial", 12), bg="#e0f7fa", wraplength=350, justify="left")
        motivational_label.pack(pady=10)
    
# Function to display the graph page in a new window
def show_graph_page():
    graph_window = Toplevel(root)
    graph_window.title("Sentiment Analysis Graph")
    graph_window.geometry("600x400")
    
    labels = ['Positive', 'Negative']
    sizes = [positive_count, negative_count]
    
    plt.clf()  # Clear any previous figures
    plt.figure(figsize=(6, 4))
    plt.bar(labels, sizes, color=['#81c784', '#ef5350'])
    plt.title('Sentiment Analysis Results')
    plt.ylabel('Number of Responses')
    
    canvas = FigureCanvasTkAgg(plt.gcf(), master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Button to go to motivational tips page
motivational_button = tk.Button(root, text="Get Motivational Tips", command=show_motivational_page, font=("Arial", 12), bg="#ffcc80", width=20)
motivational_button.pack(pady=10)

# Function to open a helpful resource link in the browser
def open_resource_link():
    webbrowser.open("https://www.verywellmind.com/")

# Button to view report page
report_button = tk.Button(root, text="View Report", command=show_report_page, font=("Arial", 12), bg="#ffcc80", width=15)
report_button.pack(pady=10)

# Button to view graph page
graph_button = tk.Button(root, text="View Graph", command=show_graph_page, font=("Arial", 12), bg="#ffcc80", width=15)
graph_button.pack(pady=10)

resource_button = tk.Button(root, text="Helpful Resource 🌐", command=open_resource_link, font=("Arial", 12), bg="#64b5f6", width=20)
resource_button.pack(pady=10)

# Function to restart the application
def restart_app():
    global current_question_index, positive_count, negative_count, sentiment_results
    current_question_index = 0
    positive_count = 0
    negative_count = 0
    sentiment_results = []
    show_question_page()

# Restart button
restart_button = tk.Button(root, text="Restart", command=restart_app, font=("Arial", 12), bg="#81c784", width=10)
restart_button.pack(pady=10)

# Start the application by showing the question page
show_question_page()

# Run the Tkinter event loop
root.mainloop()
