import json


def iter_test_jsonl_samples(filepath):
    with open(filepath, "r") as f:
        for line in f.readlines():
            yield json.loads(line)