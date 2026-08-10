#!/usr/bin/env python3
"""
Subnetting drill generator — timed CIDR/VLSM practice.

Usage:
    python3 subnet_drill.py            # 10 questions, untimed
    python3 subnet_drill.py -n 20      # 20 questions
    python3 subnet_drill.py -t 30      # 30-second limit per question

No dependencies beyond the standard library.
"""

import argparse
import ipaddress
import random
import time


def random_network():
    """Generate a random private-range base network and a random new prefix."""
    base_octet = random.choice([10, 172, 192])
    if base_octet == 10:
        base = f"10.{random.randint(0,255)}.{random.randint(0,255)}.0"
        base_prefix = 24
    elif base_octet == 172:
        base = f"172.{random.randint(16,31)}.{random.randint(0,255)}.0"
        base_prefix = 24
    else:
        base = f"192.168.{random.randint(0,255)}.0"
        base_prefix = 24

    new_prefix = random.randint(base_prefix + 1, min(base_prefix + 8, 30))
    return ipaddress.ip_network(f"{base}/{base_prefix}", strict=False), new_prefix


def ask_question(network, new_prefix):
    print(f"\nGiven {network} subnetted to /{new_prefix}:")
    q_type = random.choice(["num_subnets", "hosts_per_subnet", "first_subnet", "broadcast"])

    if q_type == "num_subnets":
        answer = 2 ** (new_prefix - network.prefixlen)
        print("  How many subnets does this create?")
    elif q_type == "hosts_per_subnet":
        answer = (2 ** (32 - new_prefix)) - 2
        print("  How many usable hosts per subnet?")
    elif q_type == "first_subnet":
        subnets = list(network.subnets(new_prefix=new_prefix))
        answer = str(subnets[0])
        print("  What is the first subnet (network address/prefix)?")
    else:  # broadcast
        subnets = list(network.subnets(new_prefix=new_prefix))
        first = subnets[0]
        answer = str(first.broadcast_address)
        print(f"  What is the broadcast address of {first}?")

    return q_type, str(answer)


def main():
    parser = argparse.ArgumentParser(description="CCNA subnetting drill")
    parser.add_argument("-n", "--num-questions", type=int, default=10)
    parser.add_argument("-t", "--time-limit", type=int, default=0,
                         help="seconds allowed per question, 0 = untimed")
    args = parser.parse_args()

    correct = 0
    times = []

    for i in range(1, args.num_questions + 1):
        print(f"\n--- Question {i}/{args.num_questions} ---")
        network, new_prefix = random_network()
        q_type, answer = ask_question(network, new_prefix)

        start = time.time()
        user_answer = input("  Your answer: ").strip()
        elapsed = time.time() - start
        times.append(elapsed)

        if user_answer.rstrip("/0123456789").strip() == "" and "/" not in user_answer:
            is_correct = user_answer == answer
        else:
            is_correct = user_answer.lower().replace(" ", "") == answer.lower().replace(" ", "")

        if is_correct:
            print(f"  Correct! ({elapsed:.1f}s)")
            correct += 1
        else:
            print(f"  Wrong. Correct answer: {answer}  ({elapsed:.1f}s)")

        if args.time_limit and elapsed > args.time_limit:
            print(f"  (over your {args.time_limit}s target)")

    print("\n=== Results ===")
    print(f"Score: {correct}/{args.num_questions} ({100*correct/args.num_questions:.0f}%)")
    if times:
        print(f"Average time: {sum(times)/len(times):.1f}s per question")
        print(f"Fastest: {min(times):.1f}s  Slowest: {max(times):.1f}s")


if __name__ == "__main__":
    main()
