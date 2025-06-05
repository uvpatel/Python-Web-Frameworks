from flask import Flask, render_template

app = Flask(__name__)

# Dummy blog post data
posts = [
    {
        "id": 1,
        "title": "The Future of AI in 2025",
        "author": "John Doe",
        "date": "May 14, 2025",
        "tag": "Technology",
        "summary": "Explore how artificial intelligence is shaping industries and daily life.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            <h2>Advancements in Machine Learning</h2>
            <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
            <blockquote><p>"AI is not just a tool; it's a paradigm shift." - Tech Visionary</p></blockquote>
            <h3>Key Trends</h3>
            <ul>
                <li>Improved natural language processing</li>
                <li>Ethical AI frameworks</li>
                <li>AI-driven automation</li>
            </ul>
            <pre><code>console.log('AI is transforming the world!');</code></pre>
        """,
        "image": "assets/post1.jpg"
    },
    {
        "id": 2,
        "title": "Global Cultural Shifts",
        "author": "Jane Smith",
        "date": "May 13, 2025",
        "tag": "Culture",
        "summary": "A look at how global cultures are evolving in the digital age.",
        "content": """
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            <h2>Cultural Influences</h2>
            <p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        """,
        "image": "assets/post2.jpg"
    },
    {
        "id": 3,
        "title": "Modern UI/UX Trends",
        "author": "Alex Brown",
        "date": "May 12, 2025",
        "tag": "Design",
        "summary": "Discover the latest trends in user interface and experience design.",
        "content": """
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.
            <h2>Design Principles</h2>
            <p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.</p>
        """,
        "image": "assets/post3.jpg"
    },
    {
        "id": 4,
        "title": "Minimalist Living in 2025",
        "author": "Emma Wilson",
        "date": "May 11, 2025",
        "tag": "Lifestyle",
        "summary": "Tips for embracing a minimalist lifestyle in a tech-driven world.",
        "content": """
            At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum.
            <h2>Minimalism Tips</h2>
            <p>Quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.</p>
        """,
        "image": "assets/post4.jpg"
    }
]

# Home route
@app.route("/")
def home():
    name = "Urvil"
    return render_template("index.html", name=name, posts=posts)

# About route
@app.route("/about")
def about():
    name = "Urvil"
    return render_template("about.html", name=name)

# Post route (dynamic)
@app.route("/post/<int:post_id>")
def post(post_id):
    name = "Urvil"
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return "Post not found", 404
    return render_template("post.html", name=name, post=post)

if __name__ == "__main__":
    app.run(debug=True)