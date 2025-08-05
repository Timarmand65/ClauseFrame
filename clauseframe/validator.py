import yaml
import argparse

def load_logic(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def validate_input(logic, user_input):
    for rule in logic.get("rules", []):
        if rule["trigger"] in user_input:
            return rule["response"]
    return "No match found."

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Text to validate")
    parser.add_argument("--logic", type=str, default="dcaa_audit_logic_engine_v0.1.yaml")
    args = parser.parse_args()

    logic = load_logic(args.logic)
    result = validate_input(logic, args.input)
    print(result)
