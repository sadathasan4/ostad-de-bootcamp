#!/usr/bin/env python3
"""
ক্লাস ১ — ল্যাবের সমাধান

নিজে চেষ্টা করার পরেই এটা দেখুন। কোড পড়ে বোঝা আর নিজে লিখতে পারা এক জিনিস না।

চালান:  python3 module-01/solution/explore_csv.py
"""

import csv
import os
from collections import Counter

CSV_PATH = os.path.join("module-01", "data", "orders_oct2026.csv")


def file_size_mb(path):
    return os.path.getsize(path) / (1024 * 1024)


def read_header_and_rows(path):
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = list(reader)
    return header, rows


def looks_like_datetime(value):
    # "2026-10-01 16:19:09" — তারিখ আর সময়, মাঝখানে একটা ফাঁকা জায়গা
    parts = value.split(" ")
    if len(parts) != 2:
        return False
    date_bits, time_bits = parts[0].split("-"), parts[1].split(":")
    if len(date_bits) != 3 or len(time_bits) != 3:
        return False
    return all(b.isdigit() for b in date_bits + time_bits)


def guess_type(values):
    clean = [v for v in values if v != ""]
    if not clean:
        return "empty"

    if all(looks_like_datetime(v) for v in clean):
        return "datetime"

    def is_int(v):
        try:
            int(v)
            return True
        except ValueError:
            return False

    def is_float(v):
        try:
            float(v)
            return True
        except ValueError:
            return False

    if all(is_int(v) for v in clean):
        return "integer"
    if all(is_float(v) for v in clean):
        return "decimal"
    return "text"


def main():
    print()
    print("ফাইল:", CSV_PATH)
    print("সাইজ: {:.2f} MB".format(file_size_mb(CSV_PATH)))

    header, rows = read_header_and_rows(CSV_PATH)
    print("মোট সারি:", len(rows))
    print("কলাম সংখ্যা:", len(header))
    print()

    print("{:<22} {:<12} {:<10} {}".format("কলাম", "ধরন", "ফাঁকা", "উদাহরণ"))
    print("-" * 74)
    for i, name in enumerate(header):
        column = [r[i] for r in rows if i < len(r)]
        kind = guess_type(column[:500])
        blanks = sum(1 for v in column if v == "")
        example = next((v for v in column if v != ""), "")
        print("{:<22} {:<12} {:<10} {}".format(name, kind, blanks, example[:28]))
    print()

    # ---------- বোনাস ----------
    idx = {name: i for i, name in enumerate(header)}

    print("status অনুযায়ী:")
    for value, count in Counter(r[idx["status"]] for r in rows).most_common():
        print("   {:<12} {:>7}  ({:.1f}%)".format(value, count, 100 * count / len(rows)))
    print()

    print("সবচেয়ে বেশি অর্ডার যে পাঁচটা এলাকা থেকে:")
    areas = Counter(r[idx["area"]] for r in rows if r[idx["area"]] != "")
    for value, count in areas.most_common(5):
        print("   {:<14} {:>7}".format(value, count))
    print()

    delivered = [int(r[idx["delivery_minutes"]]) for r in rows
                 if r[idx["delivery_minutes"]] != ""]
    print("ডেলিভারির গড় সময়: {:.1f} মিনিট ({} টা অর্ডারের হিসাব)".format(
        sum(delivered) / len(delivered), len(delivered)))

    total = sum(float(r[idx["total_bdt"]]) for r in rows
                if r[idx["status"]] == "delivered")
    print("অক্টোবরে ডেলিভার হওয়া অর্ডারের মোট টাকা: {:,.0f}".format(total))
    print()


if __name__ == "__main__":
    main()
