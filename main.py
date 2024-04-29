import re

def analyze_log(log_file, pattern):
    with open(log_file, 'r') as file:
        log_content = file.read()
        matches = re.findall(pattern, log_content)
        if matches:
            print("Folgende Übereinstimmungen wurden gefunden:")
            for match in matches:
                print(match)
        else:
            print("Keine Übereinstimmungen gefunden.")

if __name__ == "__main__":
    log_file = input("Gib den Pfad der Logdatei ein: ")
    pattern = input("Gib das Muster ein, nach dem gesucht werden soll: ")
    analyze_log(log_file, pattern)
