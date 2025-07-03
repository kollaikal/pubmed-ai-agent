# 🧠 PubMed Summarization AI Agent

[![Built with Dagger](https://img.shields.io/badge/Built%20with-Dagger-3178c6?logo=docker)](https://dagger.io/)
[![Powered by Transformers](https://img.shields.io/badge/Powered%20by-Transformers-ffcc00?logo=huggingface)](https://huggingface.co/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)

---

##  Overview

**PubMed Summarization AI Agent** is a fully containerized, offline-friendly pipeline that fetches the latest research articles from PubMed and generates concise summaries using a local transformer model (e.g. `t5-base`). Everything is orchestrated using [Dagger](https://dagger.io/) for reproducible, zero-hassle automation.

>  No external API calls at runtime — everything runs locally, inside your container.

---

##  Features

-  **Automated PubMed Search**: Pass a query and receive titles, abstracts, links, and AI-generated summaries.
-  **Abstractive Summarization**: Uses HuggingFace’s `t5-base` model for high-quality summarization.
-  **Fully Containerized**: Works the same across any environment via Docker + Dagger.
-  **Secure & Offline-Ready**: Data never leaves your system after the initial model pull.
-  **Easy to Extend**: Swap out models, add a FastAPI or Streamlit UI, or batch process queries.

---

##  Setup

### 1. **Clone the Repo**

```bash
git clone https://github.com/<yourusername>/pubmed-ai-agent.git
cd pubmed-ai-agent
```

### 2. Install Dagger & Docker
Install Docker

Install Dagger CLI

### 3. Update your Hugging Face token
For public models like t5-base, no token is required.

For private models or more reliability, add your Hugging Face access token to main.py as an environment variable.

### Usage
Run this command from the repo folder:

```
dagger call run-pubmed-agent --query "AI in cardiovascular imaging"
```
The agent will print titles, abstracts, AI-generated summaries, and direct PubMed links for the top articles.


### File Structure
File	Purpose
agent.py	PubMed search, parsing, and summarization
main.py	Dagger pipeline and orchestration
requirements.txt	Python dependencies
LICENSE	Software license
.gitignore	Git exclusions (cache, envs, etc)
README.md	This documentation

###  Example Output

🔍 PubMed AI Agent Query: AI in cardiovascular imaging
<img width="900" alt="Screenshot 2025-07-03 at 7 00 28 AM" src="https://github.com/user-attachments/assets/86ac4946-9503-40a1-a265-13af506829c6" />
--- Article 1 ---
 Title   : Advances in AI-Based Cardiac Imaging Diagnostics
 Abstract: Artificial intelligence is transforming...
 Summary : This paper reviews the impact of AI on cardiac imaging diagnostics, highlighting accuracy and workflow improvements.
 URL     : https://pubmed.ncbi.nlm.nih.gov/12345678
 
### Extending This Project
Change models: Use t5-base, distilbart-cnn-12-6, or your favorite local transformer/LLMs.

Add output formats: Save results as CSV, HTML, or PDF.

Integrate UI: Plug into Streamlit or FastAPI for interactive clinical search.

Scale up: Batch queries, add error handling, or implement semantic search.

###  License
Distributed under the MIT License.

### 🤝 Contributing & Support
PRs and issues are welcome!
Open an issue or reach out for collaboration.

### Credits
Built with Dagger, Transformers, and ❤️ by Kollaikal Rupesh.
