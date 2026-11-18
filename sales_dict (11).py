#!/usr/bin/env python3
"""
ক্লাস ৭ — ল্যাবের সমাধান

গত ক্লাসের অ্যাসাইনমেন্টে payment ধরে হিসাব করতে দশটা variable লাগছিল।
আজ সেটা একটা dictionary-তে নেমে আসবে।

চালান:  python3 module-04/solution/sales_dict.py
"""

import os

import sales_tools

PATH = os.path.join("module-02", "data", "raw_sales.txt")

# ফাইলের কোন ঘরে কী আছে — নাম দিয়ে রাখলে parts[5] আর মনে রাখতে হয় না
COLUMNS = ["order_id", "order_date", "customer_name", "item_name",
           "quantity", "amount", "payment", "status"]


def read_lines(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read().strip().split("\n")


def parse_record(raw):
    """একটা কাঁচা লাইনকে পরিষ্কার dictionary বানিয়ে ফেরত দেয়।"""
    parts = raw.split(";")
    return {
        "order_id":      sales_tools.clean_id(parts[0]),
        "order_date":    parts[1].strip(),
        "customer_name": sales_tools.clean_name(parts[2]),
        "item_name":     parts[3].strip(),
        "quantity":      int(parts[4].strip()),
        "amount":        sales_tools.clean_amount(parts[5]),
        "payment":       parts[6].strip().lower(),
        "status":        parts[7].strip().lower(),
    }


def totals_by(records, key):
    """যেকোনো একটা ঘর ধরে টাকা আর সংখ্যা জমা করে।

    key = "payment" দিলে payment ধরে, "order_date" দিলে তারিখ ধরে।
    একই function, শুধু key বদলায় — এটাই dictionary-র আসল শক্তি।
    """
    totals = {}
    counts = {}

    for rec in records:
        name = rec[key]
        totals[name] = totals.get(name, 0.0) + rec["amount"]
        counts[name] = counts.get(name, 0) + 1

    return totals, counts


def main():
    lines = read_lines(PATH)

    # প্রতিটা লাইন এখন একটা dictionary
    records = []
    cancelled = 0

    for raw in lines:
        rec = parse_record(raw)
        if rec["status"] == "cancelled":
            cancelled = cancelled + 1
            continue
        records.append(rec)

    print(f"মোট লাইন: {len(lines)}টা  ·  বাতিল: {cancelled}টা  ·  হিসাবে: {len(records)}টা")
    print()

    # ---------- একটা record দেখতে কেমন ----------
    first = records[0]
    print("প্রথম record:")
    for k, v in first.items():
        print(f"   {k:<15} {v}")
    print()

    # ---------- payment ধরে ----------
    print("payment ধরে হিসাব")
    totals, counts = totals_by(records, "payment")
    for name in sorted(totals):
        print(f"   {name:<18} {counts[name]}টা   {sales_tools.taka(totals[name])}")
    print(f"   {'সব মিলিয়ে':<18} {len(records)}টা   {sales_tools.taka(sum(totals.values()))}")
    print()

    # ---------- তারিখ ধরে — একই function ----------
    print("তারিখ ধরে হিসাব")
    by_date, date_counts = totals_by(records, "order_date")
    for day in sorted(by_date):
        print(f"   {day}   {date_counts[day]}টা   {sales_tools.taka(by_date[day])}")
    print()

    # সবচেয়ে বড়টা খোঁজা — ক্লাস ৫-এর সেই নিয়মেই, শুধু এবার dictionary ঘুরে
    best_day = ""
    best_money = 0.0
    for day in by_date:
        if by_date[day] > best_money:
            best_money = by_date[day]
            best_day = day
    print(f"সবচেয়ে বেশি টাকার দিন: {best_day} — {sales_tools.taka(best_money)}")

    biggest = {"order_id": "", "amount": 0.0}
    for rec in records:
        if rec["amount"] > biggest["amount"]:
            biggest = rec
    print(f"সবচেয়ে বড় অর্ডার: {biggest['order_id']} — {sales_tools.taka(biggest['amount'])}")
    print()


if __name__ == "__main__":
    main()
