# src/project.py
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Data conversion tool')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")
