from langchain_core.prompts import load_prompt

prompt_yaml_1 = load_prompt("10_여명구\data\fruit_color.yaml", encoding="utf-8")
print(prompt_yaml_1)