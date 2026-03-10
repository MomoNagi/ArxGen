import os
import markdown
from weasyprint import HTML, CSS
from dotenv import load_dotenv  
from arxgen.crew import ArxGenCrew

load_dotenv()

def run():
    base_url = os.getenv("OLLAMA_BASE_URL")
    model = os.getenv("OLLAMA_MODEL")
    print(f"Connexion à Ollama : {base_url} (Modèle : {model})")

    topics = input("Quels sujets de recherche ArXiv voulez-vous explorer ? (ex: 'LLM agents') : ")
    max_results = input("Nombre maximum de résultats (par défaut 5) : ") or "5"

    inputs = {
        "topics": topics,
        "max_results": int(max_results)
    }
    os.makedirs("src/arxgen/outputs", exist_ok=True)

    print(f"## Lancement de la veille sur : {topics}...")
    result = ArxGenCrew().crew().kickoff(inputs=inputs)

    print("Génération du rapport final en pdf : ")
    html_content = markdown.markdown(str(result))
    html = f"<html><body><h1>Rapport : {topics}</h1>{html_content}</body></html>"

    try:
        css_file = "src/arxgen/style/style.css"
        pdf_path = os.path.join("src/arxgen/outputs", f"arxgen_report_{topics.replace(' ', '_')}.pdf")

        HTML(string=html).write_pdf(
            pdf_path,
            stylesheets=[CSS(css_file)]
        )
        print(f"Rapport généré avec succès : {pdf_path}")
    except Exception as e:
        print(f"Erreur lors de la génération du PDF : {e}")

if __name__ == "__main__":
    run()