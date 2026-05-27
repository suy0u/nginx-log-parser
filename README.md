# Nginx Log Parser → CSV

Simple CLI tool for parsing nginx access logs and converting them into CSV format with optional filtering and sorting.

### CLI Options

| Argument | Description            | Example                    |
| -------- | ---------------------- | -------------------------- |
| --log    | Path to nginx log file | --log nginx log            |
| --output | Output CSV file        | --output output/result.csv |
| --status | Filter by HTTP status  | --status 200               |
| --sort   | Sort by field          | --sort request_time        |
| --order  | Sort order (asc/desc)  | --order desc               |

## Basic run

```bash
python parser.py --log nginx.log
```

### Filter by status code

```bash
python parser.py --log nginx.log --status 404
```

### Sort results

```bash
python parser.py --log nginx.log --sort request_time --order desc
```

Available order options:

- asc (default)
- desc

## Run with Docker

### Build image

```bash
docker build -t nginx-parser .
```

### Run container

```bash
docker run --rm -v $(pwd)/output:/app/output nginx-parser
```

### Custom run with parameters

```bash
docker run --rm \
  -v $(pwd)/output:/app/output \
  nginx-parser \
  python parser.py --log nginx.log --sort status --order desc
```

## CSV file will be saved in: `output/result.csv`
