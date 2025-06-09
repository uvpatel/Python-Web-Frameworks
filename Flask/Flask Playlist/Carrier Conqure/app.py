from flask import Flask, request, jsonify, render_template
from resume_processor import gemini_resume

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze_resume', methods=['POST'])
def analyze_resume():
    prompt = request.form.get("prompt")
    file = request.files.get("resume")

    if not prompt or not file:
        return jsonify({"error": "Missing prompt or resume"}), 400

    try:
        if file.filename.endswith('.pdf'):
            text = gemini_resume.extract_text_from_pdf(file)
            if not text.strip():
                return jsonify({"error": "Empty PDF or image-based"}), 422
            result = gemini_resume.analyze_resume_text(prompt, text)

        elif file.filename.endswith('.docx'):
            text = gemini_resume.extract_text_from_docx(file)
            result = gemini_resume.analyze_resume_text(prompt, text)

        elif file.filename.lower().endswith(('jpg', 'jpeg', 'png')):
            result = gemini_resume.analyze_resume_image(prompt, file)

        else:
            return jsonify({"error": "Unsupported file type"}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
