import os

ENTRY = "Error: I have bread but not the courage to toast it."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
