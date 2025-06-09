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
            <p>Artificial intelligence continues to evolve at an unprecedented pace, transforming how we work, live, and interact. In 2025, we're seeing AI integration across virtually every industry, from healthcare to finance to entertainment.</p>
            
            <h2>Advancements in Machine Learning</h2>
            <p>The latest generation of machine learning models has achieved remarkable breakthroughs in understanding context, generating creative content, and solving complex problems. These advancements have led to more intuitive user experiences and more efficient business operations.</p>
            
            <blockquote><p>"AI is not just a tool; it's a paradigm shift that's redefining what's possible." - Tech Visionary</p></blockquote>
            
            <h3>Key Trends</h3>
            <ul>
                <li>Improved natural language processing enabling more human-like conversations</li>
                <li>Ethical AI frameworks becoming standard practice in development</li>
                <li>AI-driven automation creating new categories of jobs</li>
                <li>Personalized AI assistants becoming integral to daily productivity</li>
            </ul>
            
            <p>As we look to the future, the line between human and artificial intelligence capabilities continues to blur, raising important questions about responsibility, ethics, and the nature of consciousness itself.</p>
            
            <pre><code>// Example of modern AI integration
const aiAssistant = new AI({
  learningRate: 0.5,
  ethicsFramework: 'responsible-ai-2025',
  capabilities: ['nlp', 'creative', 'analytical']
});

aiAssistant.solve('climate-change-mitigation');</code></pre>
            
            <p>The coming years will undoubtedly bring even more innovation as AI technologies mature and find new applications across our society.</p>
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
            <p>The digital age has accelerated cultural exchange at an unprecedented rate, creating both homogenization and diversification of global cultures. As we navigate 2025, we're witnessing fascinating shifts in how people around the world connect, create, and define their identities.</p>
            
            <h2>Cultural Influences</h2>
            <p>Social media platforms continue to function as cultural melting pots, with trends, art forms, and social movements spreading globally within hours. This interconnectedness has led to new hybrid art forms and cultural expressions that transcend traditional boundaries.</p>
            
            <h3>Emerging Cultural Phenomena</h3>
            <p>Micro-cultures centered around niche interests have gained mainstream recognition, while traditional cultural institutions adapt to remain relevant in the digital landscape. The concept of cultural heritage itself is being redefined as digital preservation techniques evolve.</p>
            
            <blockquote><p>"Culture is no longer confined by geography—it flows freely across networks, transforming as it travels." - Cultural Anthropologist</p></blockquote>
            
            <p>These shifts raise important questions about authenticity, appropriation, and the future of cultural identity in an increasingly connected world.</p>
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
            <p>Design continues to evolve rapidly in response to changing user expectations, technological capabilities, and cultural shifts. In 2025, we're seeing several key trends dominate the UI/UX landscape.</p>
            
            <h2>Design Principles for 2025</h2>
            <p>Accessibility has moved from a compliance requirement to a core design principle, with inclusive design practices becoming standard across the industry. Meanwhile, AI-assisted design tools have democratized creation, allowing non-designers to produce professional-quality interfaces.</p>
            
            <h3>Visual Trends</h3>
            <ul>
                <li>Adaptive interfaces that respond to user behavior and context</li>
                <li>Immersive 3D elements in everyday applications</li>
                <li>Abstract data visualization becoming more intuitive</li>
                <li>Sustainable design practices that optimize for energy efficiency</li>
            </ul>
            
            <p>Perhaps most notably, the line between physical and digital interfaces continues to blur as augmented reality becomes more integrated into daily life.</p>
            
            <h3>User Experience Evolution</h3>
            <p>Emotion-aware interfaces that respond to user sentiment are gaining traction, creating more human-centered digital experiences. Voice and gesture controls have become refined enough to replace traditional interfaces in many contexts.</p>
            
            <p>As we move forward, the most successful designs will be those that can adapt to increasingly diverse user needs while maintaining simplicity and clarity.</p>
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
            <p>As our digital lives grow increasingly complex, many people are turning to minimalism as a counterbalance. In 2025, minimalist living has evolved beyond aesthetic choices to become a comprehensive approach to navigating modern life.</p>
            
            <h2>Minimalism Tips</h2>
            <p>Today's minimalism emphasizes intentionality rather than deprivation. The focus is on curating physical and digital environments that support well-being and purpose rather than simply owning fewer things.</p>
            
            <h3>Digital Minimalism</h3>
            <p>With the average person now managing dozens of digital accounts and services, digital minimalism has emerged as a critical practice. This involves intentionally selecting digital tools that provide genuine value while eliminating those that create noise or distraction.</p>
            
            <blockquote><p>"The question isn't 'What can I live without?' but rather 'What truly enriches my life?'" - Minimalist Author</p></blockquote>
            
            <h3>Practical Steps</h3>
            <ul>
                <li>Conduct quarterly digital audits of subscriptions and services</li>
                <li>Implement "slow tech" practices like designated offline hours</li>
                <li>Design physical spaces around activities rather than possessions</li>
                <li>Practice mindful consumption by waiting 48 hours before purchases</li>
            </ul>
            
            <p>As environmental concerns continue to grow, minimalism has also become increasingly aligned with sustainable living practices, creating a natural synergy between personal well-being and ecological responsibility.</p>
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
        return render_template("post.html", name=name, post=None, posts=posts)
    return render_template("post.html", name=name, post=post, posts=posts)

if __name__ == "__main__":
    app.run(debug=True)