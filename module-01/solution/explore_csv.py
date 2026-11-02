#!/usr/bin/env python3
"""
ক্লাস ১ — ল্যাবের সমাধান

starter ফাইলটার হুবহু একই গড়ন, শুধু TODO-গুলো পূরণ করা। পাশাপাশি রেখে
মিলিয়ে দেখতে পারবেন।

নিজে চেষ্টা করার পরেই এটা দেখুন — কোড পড়ে বোঝা আর নিজে লিখতে পারা এক জিনিস না।

চালানোর নিয়ম (repo-র মূল ফোল্ডার থেকে):

    python3 module-01/solution/explore_csv.py
"""

import csv
import os
from collections import Counter

CSV_PATH = os.path.join("module-01", "data", "orders_oct2026.csv")


def file_size_mb(path):
    """ফাইলের সাইজ MB-তে ফেরত দিন।"""
    size_in_bytes = os.path.getsize(path)
    return size_in_bytes / (1024 * 1024)


def read_header_and_rows(path):
    """ফাইলটা পড়ে (header, rows) ফেরত দিন।"""
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = next(reader)      # প্রথম সারিটা কলামের নাম
        rows = list(reader)        # বাকি সব সারি
    return header, rows


def looks_like_datetime(value):
    """"2026-10-01 16:19:09" — এরকম গড়নের কি না, সেটা দেখে।

    মনে রাখবেন: এটা গড়ন মেলায়, তারিখটা বাস্তব কি না যাচাই করে না।
    """
    parts = value.split(" ")
    if len(parts) != 2:
        return False

    date_bits = parts[0].split("-")     # 2026, 10, 01
    time_bits = parts[1].split(":")     # 16, 19, 09
    if len(date_bits) != 3 or len(time_bits) != 3:
        return False

    return all(bit.isdigit() for bit in date_bits + time_bits)


def is_int(value):
    """int() দিয়ে রূপান্তর হয় কি না।"""
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value):
    """float() দিয়ে রূপান্তর হয় কি না।"""
    try:
        float(value)
        return True
    except ValueError:
        return False


def guess_type(values):
    """কয়েকটা মান দেখে অনুমান করুন কলামটা কী ধরনের।"""
    # ফাঁকা ঘরগুলো হিসাবের বাইরে — int("") ভেঙে যায়
    clean = [v for v in values if v != ""]
    if not clean:
        return "empty"

    if all(looks_like_datetime(v) for v in clean):
        return "datetime"

    # int আগে, float পরে — প্রতিটা integer-ই বৈধ float,
    # তাই উল্টো করলে সব সংখ্যাই decimal হয়ে যেত
    if all(is_int(v) for v in clean):
        return "integer"
    if all(is_float(v) for v in clean):
        return "decimal"

    return "text"


def main():
    print()
    print("ফাইল:", CSV_PATH)

    # ----- ১. সাইজ -----
    print("সাইজ: {:.2f} MB".format(file_size_mb(CSV_PATH)))

    # ----- ২ ও ৩. সারি আর কলাম -----
    header, rows = read_header_and_rows(CSV_PATH)
    print("মোট সারি:", len(rows))
    print("কলাম সংখ্যা:", len(header))
    print()

    # ----- ৪. প্রতিটা কলামের ধরন -----
    print("{:<22} {:<12} {}".format("কলাম", "ধরন", "উদাহরণ"))
    print("-" * 64)
    for i, name in enumerate(header):
        sample = [r[i] for r in rows[:500] if i < len(r)]
        kind = guess_type(sample)
        example = next((v for v in sample if v != ""), "")
        print("{:<22} {:<12} {}".format(name, kind, example[:28]))
    print()

    # ----- বোনাস -----
    # নাম থেকে কলামের নম্বর — r[11] লিখলে ছয় মাস পরে কেউ বুঝবে না
    idx = {name: i for i, name in enumerate(header)}

    # ক. কোন কলামে কয়টা ঘর ফাঁকা
    print("ফাঁকা ঘর (পুরো ফাইলের হিসাব):")
    for i, name in enumerate(header):
        blanks = sum(1 for r in rows if i < len(r) and r[i] == "")
        if blanks:
            print("   {:<20} {:>6}  ({:.1f}%)".format(
                name, blanks, 100 * blanks / len(rows)))
    print()

    # খ. status কলামে কী কী মান, কোনটা কতবার
    print("status অনুযায়ী:")
    status_counts = Counter(r[idx["status"]] for r in rows)
    for value, count in status_counts.most_common():
        print("   {:<12} {:>7}  ({:.1f}%)".format(
            value, count, 100 * count / len(rows)))
    print()

    # গ. সবচেয়ে বেশি অর্ডার কোন এলাকা থেকে
    print("সবচেয়ে বেশি অর্ডার যে পাঁচটা এলাকা থেকে:")
    areas = Counter(r[idx["area"]] for r in rows if r[idx["area"]] != "")
    for value, count in areas.most_common(5):
        print("   {:<14} {:>7}".format(value, count))
    print()

    # ঘ. ডেলিভারির গড় সময় — ফাঁকা ঘর বাদ দিয়ে
    delivered = [int(r[idx["delivery_minutes"]]) for r in rows
                 if r[idx["delivery_minutes"]] != ""]
    print("ডেলিভারির গড় সময়: {:.1f} মিনিট ({} টা অর্ডারের হিসাব)".format(
        sum(delivered) / len(delivered), len(delivered)))
    print()


if __name__ == "__main__":
    main()
