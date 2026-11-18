#!/usr/bin/env python3
"""
ক্লাস ৭ — ল্যাব

গত ক্লাসের অ্যাসাইনমেন্টে মনে আছে? payment ধরে হিসাব করতে দশটা variable
লিখতে হয়েছিল — bkash_total, bkash_count, nagad_total... আর পাঁচটা elif।

আজ সেটা তিন লাইনে নামবে।

চালানোর নিয়ম (repo-র মূল ফোল্ডার থেকে):

    python3 module-04/starter/sales_dict.py

TODO লেখা জায়গাগুলো আপনি পূরণ করবেন।
"""

import os

import sales_tools          # গত ক্লাসের সেই ফাইলটাই, পাশে কপি করা আছে

PATH = os.path.join("module-02", "data", "raw_sales.txt")


def read_lines(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read().strip().split("\n")


# ---------- ধাপ ১: একটা লাইনকে dictionary বানান ----------
def parse_record(raw):
    """একটা কাঁচা লাইনকে পরিষ্কার dictionary বানিয়ে ফেরত দিন।

    এরকম ফেরত দেবে:

        {"order_id": "ORD100045", "order_date": "2026-10-07",
         "customer_name": "Rahim Uddin", "item_name": "Miniket Chal 5kg",
         "quantity": 2, "amount": 1240.5,
         "payment": "bkash", "status": "delivered"}
    """
    parts = raw.split(";")

    # ইঙ্গিত: দুইটা ঘর করে দিলাম, বাকি ছয়টা আপনি
    #
    #   return {
    #       "order_id": sales_tools.clean_id(parts[0]),
    #       "order_date": parts[1].strip(),
    #       ...
    #   }

    # TODO


# ---------- ধাপ ২: যেকোনো ঘর ধরে জমা করুন ----------
def totals_by(records, key):
    """key যেটা দেবেন, সেই ঘর ধরে টাকা আর সংখ্যা জমা করে ফেরত দিন।

    key = "payment"     →  কোন payment-এ কত
    key = "order_date"  →  কোন তারিখে কত

    একই function, শুধু key বদলায়। এটাই আজকের আসল জিনিস।
    """
    totals = {}
    counts = {}

    for rec in records:
        name = rec[key]

        # ইঙ্গিত — এই দুইটা লাইনই গত সপ্তাহের দশটা variable-এর বদলি:
        #
        #   totals[name] = totals.get(name, 0.0) + rec["amount"]
        #   counts[name] = counts.get(name, 0) + 1
        #
        # .get(name, 0) মানে — ঘরটা থাকলে তার মান দাও, না থাকলে শূন্য দাও।

        # TODO
        pass

    return totals, counts


def main():
    lines = read_lines(PATH)

    # ---------- ধাপ ৩: সব record বানান, বাতিলগুলো বাদ দিন ----------
    records = []
    cancelled = 0

    for raw in lines:
        rec = parse_record(raw)

        # TODO: status যদি "cancelled" হয় — cancelled বাড়ান, আর continue
        # TODO: নইলে records.append(rec)

        pass        # TODO দুইটা লেখা হলে এই লাইনটা মুছে দেবেন

    print(f"মোট লাইন: {len(lines)}টা  ·  বাতিল: {cancelled}টা  ·  হিসাবে: {len(records)}টা")
    print()

    # ---------- ধাপ ৪: একটা record দেখে নিন ----------
    # ইঙ্গিত:
    #   for k, v in records[0].items():
    #       print(f"   {k:<15} {v}")

    # TODO


    # ---------- ধাপ ৫: payment ধরে ছাপান ----------
    # ইঙ্গিত:
    #   totals, counts = totals_by(records, "payment")
    #   for name in sorted(totals):
    #       print(f"   {name:<18} {counts[name]}টা   {sales_tools.taka(totals[name])}")

    # TODO


    # ---------- ধাপ ৬: এবার তারিখ ধরে — একই function ----------
    # শুধু "payment"-এর জায়গায় "order_date" দিন। আর কিছু বদলাবে না।

    # TODO


    # ---------- ধাপ ৭: সবচেয়ে বেশি টাকার দিনটা ----------
    # ক্লাস ৫-এর সেই নিয়মেই — একটা ঘর বাইরে রেখে loop-এ মিলিয়ে দেখা।
    # শুধু এবার list-এর বদলে dictionary ঘুরবেন।

    # TODO


if __name__ == "__main__":
    main()


# ---------- মিলিয়ে দেখুন ----------
#   payment ধরে:  bkash ৳2484.00 · nagad ৳908.00 · card ৳812.00
#                 cash on delivery ৳661.50 · rocket ৳232.25
#   সব মিলিয়ে:    ৳5097.75   ← গত তিন ক্লাসের সেই একই সংখ্যা
#   সবচেয়ে বেশি টাকার দিন:  2026-10-07 — ৳1590.50
#
# ---------- বোনাস (সময় থাকলে) ----------
# - item ধরে হিসাব করুন — totals_by(records, "item_name")
# - status ধরে হিসাব করুন (বাতিল বাদ দেওয়ার আগের list দিয়ে)
# - গত সপ্তাহের payment_totals.py পাশে খুলুন। কত লাইন কমলো, গুনে দেখুন।
