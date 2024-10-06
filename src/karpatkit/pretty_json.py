import argparse
import glob
import json
import os
import sys


def main_cli():
    parser = argparse.ArgumentParser(prog="pretty_json")
    parser.add_argument("--check", action="store_true", help="just check, no file writting")
    parser.add_argument("root_dir", nargs="+")
    args = parser.parse_args()

    check_mode = args.check
    for root_dir in args.root_dir:
        for json_file in glob.glob(os.path.join(root_dir, "**", "*.json"), recursive=True):
            if check_mode:
                with open(json_file, "r", encoding="utf-8") as f:
                    current = f.read()
                    obj = json.loads(current)
                    expected = json.dumps(obj, indent=2, ensure_ascii=False)
                    if current != expected + "\n":
                        sys.exit(f"pretty_json: Oh noooo por dios!.\nFound a sneaky file not formatted: {json_file}")

            if not check_mode:
                with open(json_file, "r", encoding="utf-8") as f:
                    obj = json.load(f)
                with open(json_file, "w", encoding="utf-8") as f:
                    json.dump(obj, f, indent=2, ensure_ascii=False)
                    f.write("\n")
