#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="Path to first file")
    parser.add_argument("second_file", help="Path to second file")
    
    args = parser.parse_args()
    
    # Пока просто заглушка
    print(f"First file: {args.first_file}")
    print(f"Second file: {args.second_file}")

if __name__ == "__main__":
    main()
