import re
import csv

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ '
    r'\[(?P<time>.*?)\] '
    r'"(?P<request>.*?)" '
    r'(?P<status>\d+) '
    r'(?P<size>\d+) '
    r'"(?P<referer>.*?)" '
    r'"(?P<user_agent>.*?)" '
    r'(?P<request_length>\d+) '
    r'(?P<request_time>[\d\.]+) '
    r'\[(?P<upstream_name>.*?)\] '
    r'(?P<upstream_addr>\S+) '
    r'(?P<upstream_response_length>\d+) '
    r'(?P<upstream_response_time>[\d\.]+) '
    r'(?P<upstream_status>\d+) '
    r'(?P<request_id>\S+)'
)

def parse_log(file_path):
    rows = []

    with open(file_path) as f:
        for line in f:
            match = LOG_PATTERN.match(line)

            if match:
                rows.append(match.groupdict())

    return rows

def save_csv(data, output_file):
    if not data:
        print("No data found")
        return
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=data[0].keys()
        )

        writer.writeheader()
        writer.writerows(data)


def main():
    data = parse_log("nginx.log")
    save_csv(data, "output.csv")

    print("Done!")


if __name__ == "__main__":
    main()