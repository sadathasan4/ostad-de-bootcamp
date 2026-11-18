#!/usr/bin/env python3
"""
ক্লাস ১ — ল্যাব
ThelaGari-র অক্টোবর মাসের অর্ডারের ফাইলটা পড়ে চারটা জিনিস বের করুন:

    ১. ফাইলের সাইজ কত (MB-তে)
    ২. মোট কয়টা সারি (header বাদে)
    ৩. কলামের নামগুলো কী কী
    ৪. প্রতিটা কলামে কী ধরনের data আছে — সংখ্যা, তারিখ, নাকি লেখা

চালানোর নিয়ম (repo-র মূল ফোল্ডার থেকে):

    python3 module-01/starter/explore_csv.py

TODO লেখা জায়গাগুলো আপনি পূরণ করবেন। আটকে গেলে নিচের ইঙ্গিতগুলো দেখুন।
"""

import csv
import os

CSV_PATH = os.path.join("module-01", "data", "orders_oct2026.csv")


def file_size_mb(path):
    """ফাইলের সাইজ MB-তে ফেরত দিন।

    ইঙ্গিত: os.path.getsize(path) বাইট দেয়। ১ MB = ১০২৪ × ১০২৪ বাইট।
    """
    # TODO
    return 0.0


def read_header_and_rows(path):
    """ফাইলটা পড়ে (header, rows) ফেরত দিন।

    ইঙ্গিত:
        with open(path, newline="", encoding="utf-8") as fh:
            reader = csv.reader(fh)
            header = next(reader)      # প্রথম সারিটা কলামের নাম
            rows = list(reader)        # বাকি সব সারি
    """
    # TODO
    return [], []


def guess_type(values):
    """কয়েকটা মান দেখে অনুমান করুন কলামটা কী ধরনের।

    "integer", "decimal", "datetime" বা "text" — এর একটা ফেরত দিন।

    ইঙ্গিত:
        - int(v) চালিয়ে দেখুন, না পারলে ValueError আসবে — try/except দিয়ে ধরুন
        - float(v) একইভাবে
        - তারিখের জন্য: "2026-10-01 16:19:09" — এর গড়নটা দেখে বোঝা যায়
        - ফাঁকা মান ("") হিসাবের বাইরে রাখুন
    """
    # TODO
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

    # ----- বোনাস (সময় থাকলে) -----
    # - কোন কলামে কয়টা ঘর ফাঁকা?
    # - status কলামে কী কী মান আছে, কোনটা কতবার?
    # - সবচেয়ে বেশি অর্ডার কোন এলাকা থেকে?


if __name__ == "__main__":
    main()
