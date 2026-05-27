import re
import csv
import argparse

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
    parser = argparse.ArgumentParser()

    parser.add_argument("--log",  default="nginx.log")
    parser.add_argument("--output", default="result.csv")
    parser.add_argument("--status")
    parser.add_argument("--sort")
    parser.add_argument("--order", choices=["asc", "desc"], default="asc")

    args = parser.parse_args()

    data = parse_log(args.log)

    if args.status:
        data = [x for x in data if x["status"] == args.status]

    if args.sort:
        data = sorted(data, key=lambda x: x[args.sort], reverse=(args.order == "desc"))

    save_csv(data, args.output)

    print("Done!")


if __name__ == "__main__":
    main()