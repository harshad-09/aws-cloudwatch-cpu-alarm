#!/usr/bin/env python3
"""Simple CPU stress script used to trigger the CloudWatch alarm.

Usage: python3 scripts/stress.py [cores] [seconds]
"""
import multiprocessing
import sys
import time


def burn(duration):
    end = time.time() + duration
    while time.time() < end:
        _ = 123456789 * 987654321  # busy loop to keep the CPU at 100%


if __name__ == "__main__":
    cores = int(sys.argv[1]) if len(sys.argv) > 1 else multiprocessing.cpu_count()
    duration = int(sys.argv[2]) if len(sys.argv) > 2 else 600
    print(f"Stressing {cores} core(s) for {duration} seconds...")
    procs = [multiprocessing.Process(target=burn, args=(duration,)) for _ in range(cores)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print("Done.")
