import pandas as pd
import json

# Extração

def extract_user_ids(csv_path: str) -> list:
    df = pd.read_csv(csv_path)
    return df["UserID"].tolist()

def extract_users(json_path: str, user_ids: list) -> list:
    with open(json_path, "r", encoding="utf-8") as f:
        users = json.load(f)

    return [user for user in users if user["id"] in user_ids]

# Transformação

def generate_message(user: dict) -> str:
    balance = user["account"]["balance"]
    name = user["name"]

    if balance >= 3000:
        return f"{name}, seu saldo demonstra uma ótima saúde financeira. Considere investir para potencializar seus ganhos."
    elif balance >= 1000:
        return f"{name}, investir pequenas quantias regularmente pode ajudar a construir uma boa reserva financeira."
    else:
        return f"{name}, mesmo com valores menores é possível começar a investir e planejar o futuro."


def transform_users(users: list) -> list:
    for index, user in enumerate(users):
        user["news"] = [{
            "id": index + 1,
            "icon": "https://cdn-icons-png.flaticon.com/512/3135/3135706.png",
            "description": generate_message(user)
        }]
    return users


# Load

def load_users(users: list, output_path: str):
    for user in users:
        print(f"Usuário {user['id']} processado com sucesso.")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


# PIPELINE

def run_pipeline():
    user_ids = extract_user_ids("SDW2025.csv")
    users = extract_users("users_mock.json", user_ids)
    transformed_users = transform_users(users)
    load_users(transformed_users, "users_final.json")


if __name__ == "__main__":
    run_pipeline()