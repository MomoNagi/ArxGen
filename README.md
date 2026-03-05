# ArxGen : Veille Scientifique Automatisée

ArxGen est un système d'intelligence artificielle conçu pour automatiser l'analyse et la synthèse de publications scientifiques. À partir de mots-clés ou de thématiques, il récupère les derniers papiers sur ArXiv liés et utilise l'IA générative pour produire des résumés critiques et identifier les innovations majeures.

## Points forts

+ Multi-agents : Orchestration de deux agents spécialisés via le framework CrewAI.

+ Intelligence Locale : Inférence 100% locale via Ollama, garantissant la confidentialité de vos axes de recherche.

+ Data Sourcing Réel : Intégration directe avec l'API officielle d'ArXiv pour des données fraîches et vérifiables.

+ Architecture : Gestion des dépendances modernes et structure en src layout pour une meilleure maintenabilité.

## The Crew

| Agent | Tâche | Outil |
| :--------- | :---------: | --------: |
| Researcher | Explore ArXiv et extrait méticuleusement les abstracts et URLs | ArxivSearchTool |
| Analyste | Synthétise les méthodologies, innovations et résultats | Ollama |

## Stack Technique
- Langage : Python 3.12+
- Orchestration : CrewAI
- Modèles (LLM) : Ollama
- Extraction : ArXiv API Wrapper
- Validation : Pydantic v2