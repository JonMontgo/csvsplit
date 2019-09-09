#! /usr/bin/env python3
import csv
import argparse
import os


def main(args):
    # Check if file exists
    if not os.path.isfile(args.file_path):
        raise FileNotFoundError(f"{args.file_path} does not exist!")

    with open(args.file_path, "r") as fh:
        csv_reader = csv.DictReader(fh)
        chunks = []
        current_chunk = 0
        for row in csv_reader:
            chunks.append(row)
            if len(chunks) % args.chunk_size == 0:
                with open(chunk_path(args.file_path,
                                     current_chunk),
                          "w") as fh2:
                    csv_writer = csv.DictWriter(fh2, chunks[0].keys())
                    csv_writer.writeheader()
                    csv_writer.writerows(chunks)
                    chunks = []
                    current_chunk += 1
        with open(chunk_path(args.file_path, current_chunk), "w") as fh2:
            csv_writer = csv.DictWriter(fh2, chunks[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(chunks)


def chunk_path(file_path: str, current_chunk: int) -> str:
    path_and_ext = os.path.splitext(args.file_path)
    return f"{path_and_ext[0]}_chunk_{current_chunk}{path_and_ext[1]}"


def cli_entry():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--chunk_size",
                        help="The number of lines to put into every chunk",
                        type=int, required=True)
    parser.add_argument("file_path",
                        help="The file name of the csv")
    args = parser.parse_args()
    main(args)


if __name__ == "__main__":
    cli_entry()
