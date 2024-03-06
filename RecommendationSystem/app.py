from flask import Flask, render_template, request

app = Flask(__name__)

# Sample content data (you can replace this with your own dataset)
content_data = {
    'article1': {'title': 'Introduction to Python', 'tags': ['python', 'programming']},
    'article2': {'title': 'Web Development with Flask', 'tags': ['python', 'flask', 'web']},
    'article3': {'title': 'Data Analysis with Pandas', 'tags': ['python', 'pandas', 'data']},
    'article4': {'title': 'Machine Learning Basics', 'tags': ['python', 'machine learning']},
    'article5': {'title': 'Deep Learning Fundamentals', 'tags': ['python', 'deep learning']}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user preferences from the form
    preferences = request.form.getlist('preferences')

    # Generate recommendations based on user preferences
    recommendations = generate_recommendations(preferences)

    return render_template('recommendations.html', recommendations=recommendations)

def generate_recommendations(preferences):
    # Simple content-based filtering: Recommend articles with matching tags
    recommendations = []
    for content_id, content_info in content_data.items():
        if any(tag in preferences for tag in content_info['tags']):
            recommendations.append(content_info['title'])
    return recommendations

if __name__ == '__main__':
    app.run(debug=True)
