import json
import yaml
import datetime
from openai import OpenAI

client = OpenAI()

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def log_event(event):
    event["timestamp"] = datetime.datetime.utcnow().isoformat()
    with open("logs/runs.jsonl", "a") as f:
        f.write(json.dumps(event) + "\n")

def run_stage(stage_file, system_prompt, temperature):
    stage = load_yaml(stage_file)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": stage["stage_prompt"]},
        {"role": "user", "content": stage["task"]}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        temperature=temperature
    )

    output = response.choices[0].message.content

    log_event({
        "stage": stage["stage_name"],
        "prompt": messages,
        "output": output
    })

    print(f"\n--- {stage['stage_name']} OUTPUT ---\n")
    print(output)
    input("\nHUMAN APPROVAL REQUIRED — press Enter to continue...\n")

    return output

def main():
    config = load_yaml("config.yaml")
    system_prompt = config["system_prompt"]

    run_stage(
        "stages/01_requirements.yaml",
        system_prompt,
        config["temperature"]["requirements"]
    )

    run_stage(
        "stages/02_data_sources.yaml",
        system_prompt,
        config["temperature"]["data_sources"]
    )

    run_stage(
        "stages/03_implementation.yaml",
        system_prompt,
        config["temperature"]["implementation"]
    )

    run_stage(
        "stages/04_validation.yaml",
        system_prompt,
        config["temperature"]["validation"]
    )

if __name__ == "__main__":
    main()
