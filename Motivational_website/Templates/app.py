from flask import Flask, render_template_string

app = Flask(__name__)

quotes = [
        "Wish it, Plan it, Do it."
        "Change the world by being yourself."
        "Believe in yourself cause why not."
        "Push yourself, because no one else is going to do it for you."
        "If you can change your mind, you can change your life."
        "The struggle you feel today creates the success you'll enjoy tomorrow."
        "Everyday is a chance to learn."
        "Never stop chasing your dreams. It will be worth it."
        "Choose to be optimistic, it fells better."
        "Do more of what makes you happy."
        "Stay positive, better days are on their way."
        "It is never too late to be what you might have been."
        "Make at least one definite move daily toward your goal."
        "Work hard dream big never give up."
        "Never stop learning, because life never stops teaching."
        "Nothing ever becomes real till it is experienced."
        "The future belongs to those who believe in the beauty of their dreams."
        "The highest result of education is tolerance."
        "The mind is not a vessel to be filled, but a fire to be kindled."
        "The power of education lies in its ability to transform lives."
        "If you want to achieve greatness, stop asking for permission."
        "Learn today, lead tomorrow."
        "If you want to be powerful, educate yourself."
        "If you don't know the think to do is not get scared, but to learn."
        "The trick to having happy students is to first be happy yourself."
        "Learning is never done without errors and defeat."
        "Your talent and abilities will improve over time, but for that you have to start."
        "There's no elavator to success, you have to take the stairs."
        "Success consists of going from failure to failure without loss of enthusiasm."
        "Just do your best."
        "Coming together is beginning, keeping together is progress, working together is success."
        "Never give up because great things take time."
        "Knowledge is the key to success in life."
        "Study now, shine later."
        "Stay curious, keep learning, never stop growing."
        "The roots of education are bitter, but the fruit is so sweet."
        "Your hardwork will pay off."
        "Don't stop until you're proud."
        "Every expert was once a beginner."
        "Education is the most powerful weapon you can use to change the world."
]

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__=="__main__":
    app.run(debug=True)