from pyscript import display
from pyodide.http import pyfetch  # ✅ Corrected here

async def translate_english(event=None):
    try:
        from js import document
    except ImportError:
        display("⚠️ Please run in a PyScript environment.", target="output")
        return

    english_text = document.getElementById("english").value.strip()

    if not english_text:
        display("⚠️ Please enter some text.", target="output")
        return

    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=gu&dt=t&q={english_text}"

    try:
        response = await pyfetch(url)
        data = await response.json()
        translated_text = data[0][0][0]
        display(translated_text, target="output")
    except Exception as e:
        display(f"❌ Error: {str(e)}", target="output")
