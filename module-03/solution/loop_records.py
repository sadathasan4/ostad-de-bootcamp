#!/usr/bin/env python3
"""
ক্লাস ৫ — ল্যাবের সমাধান

starter ফাইলটার হুবহু একই গড়ন, শুধু TODO-গুলো পূরণ করা।
নিজে চেষ্টা করার পরেই এটা দেখুন।

চালান:  python3 module-03/solution/loop_records.py
"""

import os

PATH = os.path.join("module-02", "data", "raw_sales.txt")

with open(PATH, encoding="utf-8") as fh:
    lines = fh.read().strip().split("\n")

print(f"ফাইলে লাইন আছে: {len(lines)}টা")
print()


# ---------- ধাপ ১: জমা রাখার ঘর ----------
# loop শুরুর আগে। ভেতরে বানালে প্রতিবার শূন্য হয়ে যেত।
total_amount   = 0.0
good_orders    = 0
cancelled      = 0
biggest_amount = 0.0
biggest_id     = ""


# ---------- ধাপ ২-৬: loop ----------
for raw in lines:
    parts = raw.split(";")

    order_id      = parts[0].strip().upper()
    order_date    = parts[1].strip()
    customer_name = parts[2].strip().title()
    item_name     = parts[3].strip()
    quantity      = int(parts[4].strip())
    amount        = float(parts[5].strip().replace("৳", "").replace(",", ""))
    payment       = parts[6].strip().lower()
    status        = parts[7].strip().lower()

    # একাধিক স্পেস এক করা — .replace() এখানে কাজ করে না,
    # কারণ "mim   begum"-এ তিনটা স্পেস
    customer_name = " ".join(customer_name.split())

    # বাতিল অর্ডার হিসাবে ধরবো না
    if status == "cancelled":
        print(f"সতর্কতা: {order_id} বাতিল — হিসাবে ধরা হলো না")
        cancelled = cancelled + 1
        continue

    print(f"{order_id}  {customer_name:<18} {item_name:<20} {quantity}টা  ৳{amount:.2f}")

    total_amount = total_amount + amount
    good_orders  = good_orders + 1

    if amount > biggest_amount:
        biggest_amount = amount
        biggest_id     = order_id


# ---------- ধাপ ৭: সারাংশ ----------
# খেয়াল করুন — এই অংশটা বাঁ দিক ঘেঁষে, loop-এর বাইরে
print()
print("--------- সারাংশ ---------")
print(f"মোট অর্ডার (বাতিল বাদে): {good_orders}টা")
print(f"বাতিল: {cancelled}টা")
print(f"মোট টাকা: ৳{total_amount:.2f}")
print(f"গড় অর্ডার: ৳{total_amount / good_orders:.2f}")
print(f"সবচেয়ে বড়: {biggest_id} — ৳{biggest_amount:.2f}")
print()


# ---------- বোনাস ১: শুধু bkash ----------
bkash_total = 0.0
for raw in lines:
    parts = raw.split(";")
    if parts[7].strip().lower() == "cancelled":
        continue
    if parts[6].strip().lower() == "bkash":
        bkash_total = bkash_total + float(parts[5].strip().replace("৳", "").replace(",", ""))

print(f"bkash-এ মোট: ৳{bkash_total:.2f}")


# ---------- বোনাস ২: ৫০০ টাকার বেশি অর্ডার ----------
big = 0
for raw in lines:
    parts = raw.split(";")
    if float(parts[5].strip().replace("৳", "").replace(",", "")) > 500:
        big = big + 1

print(f"৫০০ টাকার বেশি অর্ডার: {big}টা")
print()


# ---------- গত ক্লাসের সাথে মিলিয়ে দেখুন ----------
# ক্লাস ৪-এ দুইটা record করতে লেগেছিল প্রায় ৪০ লাইন।
# আজ দশটা record হলো একটা loop-এ। একশোটা হলেও কোড একই থাকতো।
