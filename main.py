import dagger
from dagger import dag, function, object_type

@object_type
class CodingAgent:
    @function
    def run_pubmed_agent(self, query: str = "AI in heart surgery") -> str:
        return (
            dag.container()
            .from_("python:3.10")
            .with_env_variable("QUERY", query)
            .with_env_variable("HF_TOKEN", "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")
            .with_mounted_directory("/app", dag.current_module().source().directory("."))
            .with_workdir("/app")
            .with_exec(["python", "-m", "pip", "install", "--upgrade", "pip"])
            .with_exec(["pip", "install", "-r", "requirements.txt"])
            # Only after transformers/torch installed, download model weights:
            .with_exec(["python", "-c", "from transformers import pipeline; pipeline('summarization', model='t5-base')"])
            .with_exec(["python", "agent.py"])
            .stdout()
        )
