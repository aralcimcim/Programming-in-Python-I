import argparse
import subprocess

def arbitrarizer():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--program", type=str, required=True)
    parser.add_argument("-a", "--args", nargs="+", default=[])
    parser.add_argument("-t", "--timeout", type=float, default=60.0)
    args = parser.parse_args()

    try:
        if args.args:
            print(f"Running program {args.program} with arguments {args.args} with a {args.timeout}s timeout")
        
        else:
            print(f"Running program {args.program} without any arguments with a {args.timeout}s timeout")

        runner = subprocess.run([args.program] + args.args, timeout=args.timeout, capture_output=True, encoding="utf-8")

        print(f"The '{args.program}' finished with exit code {runner.returncode}")

        if runner.stdout:
            print(f"The '{args.program}' produced the following standard output:\n{runner.stdout}")
        
        if runner.stderr:
            print(f"The '{args.program}' produced the following error output:\n{runner.stderr}")

    except FileNotFoundError:
        print(f"The specified program '{args.program}' could not be found")
    
    except subprocess.TimeoutExpired:
        print("The program execution timed out")

