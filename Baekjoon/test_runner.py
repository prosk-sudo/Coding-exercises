#!/usr/bin/env python3

import sys
import subprocess
import os

def run_single_test(program, input_data):
    try:
        result = subprocess.run(
            [f'./{program}'], 
            input=input_data, 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 test_runner.py <program_name>")
        sys.exit(1)

    program = sys.argv[1]

    if not os.path.exists(f'./{program}'):
        print(f"Error: Program './{program}' not found")
        sys.exit(1)

    try:
        with open(f'{program}.in', 'r') as f:
            all_input = f.read()
        with open(f'{program}.out', 'r') as f:
            all_expected = f.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    input_cases = all_input.split('\n\n')
    expected_cases = all_expected.split('\n\n')

    if len(input_cases) != len(expected_cases):
        print(f"Warning: Mismatch in test case count (input: {len(input_cases)}, output: {len(expected_cases)})")

    passed = 0
    total = len(input_cases)

    print(f"Running {total} test case(s)...")
    print("=" * 50)

    for i, (inp, expected) in enumerate(zip(input_cases, expected_cases)):
        if not inp.strip():
            continue

        print(f"Test Case {i+1}:")
        print(f"Input: {repr(inp.strip())}")

        actual = run_single_test(program, inp.strip())
        expected = expected.strip()

        print(f"Expected: {repr(expected)}")
        print(f"Actual:   {repr(actual)}")

        if actual == expected:
            print("✅ PASSED")
            passed += 1
        else:
            print("❌ FAILED")

        print("-" * 30)

    print(f"Results: {passed}/{total} test cases passed")

if __name__ == "__main__":
    main()
