#!/usr/bin/env python3
"""
ক্লাস ৬ — ল্যাবের সমাধান (২/২)

গত ক্লাসের সেই একই কাজ, একই উত্তর। পার্থক্য শুধু — পরিষ্কার করার কাজগুলো
এখন আলাদা একটা module-এ, আর এই ফাইলটা সেগুলো ডেকে আনে।

চালান:  python3 module-03/solution/report.py
"""

import os
import statistics

import sales_tools

PATH = os.path.join("module-02", "data", "raw_sales.txt")


def read_lines(path):
    """ফাইলটা পড়ে প্রতিটা লাইনকে list-এর একটা ঘরে বসিয়ে ফেরত দেয়।"""
    with open(path, encoding="utf-8") as fh:
        return fh.read().strip().split("\n")


def summarise(lines):
    """সব record ঘুরে দেখে — মোট, গড়, সবচেয়ে বড়টা ফেরত দেয়।"""
    amounts = []
    cancelled = 0
    biggest_id = ""
    biggest_amount = 0.0

    for raw in lines:
        parts = raw.split(";")

        order_id = sales_tools.clean_id(parts[0])
        name     = sales_tools.clean_name(parts[2])
        item     = parts[3].strip()
        quantity = int(parts[4].strip())
        amount   = sales_tools.clean_amount(parts[5])
        status   = parts[7]

        if sales_tools.is_cancelled(status):
            print(f"সতর্কতা: {order_id} বাতিল — হিসাবে ধরা হলো না")
            cancelled = cancelled + 1
            continue

        print(f"{order_id}  {name:<18} {item:<20} {quantity}টা  {sales_tools.taka(amount)}")

        amounts.append(amount)

        if amount > biggest_amount:
            biggest_amount = amount
            biggest_id = order_id

    return amounts, cancelled, biggest_id, biggest_amount


def main():
    lines = read_lines(PATH)
    print(f"ফাইলে লাইন আছে: {len(lines)}টা")
    print()

    amounts, cancelled, biggest_id, biggest_amount = summarise(lines)

    print()
    print("--------- সারাংশ ---------")
    print(f"মোট অর্ডার (বাতিল বাদে): {len(amounts)}টা")
    print(f"বাতিল: {cancelled}টা")
    print(f"মোট টাকা: {sales_tools.taka(sum(amounts))}")
    print(f"গড় অর্ডার: {sales_tools.taka(statistics.mean(amounts))}")
    print(f"সবচেয়ে বড়: {biggest_id} — {sales_tools.taka(biggest_amount)}")
    print()


if __name__ == "__main__":
    main()
