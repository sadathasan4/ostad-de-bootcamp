#!/usr/bin/env python3
"""
ক্লাস ৫ — ল্যাব

গত ক্লাসে একটা record পরিষ্কার করতে আপনার লেগেছিল প্রায় বিশ লাইন। দুইটা
record করতে চল্লিশ। আজ দশটা record করবো — কোড বাড়বে না।

এটাই loop-এর পুরো ব্যাপার।

চালানোর নিয়ম (repo-র মূল ফোল্ডার থেকে):

    python3 module-03/starter/loop_records.py

TODO লেখা জায়গাগুলো আপনি পূরণ করবেন।
"""

import os

# গত ক্লাসের সেই ফাইলটাই — নতুন কিছু না
PATH = os.path.join("module-02", "data", "raw_sales.txt")


# ---------- এই অংশটা দেওয়াই আছে ----------
# ফাইলটা পড়ে প্রতিটা লাইনকে list-এর একটা করে ঘরে বসায়
with open(PATH, encoding="utf-8") as fh:
    lines = fh.read().strip().split("\n")

print(f"ফাইলে লাইন আছে: {len(lines)}টা")
print()


# ---------- ধাপ ১: জমা রাখার ঘর বানান ----------
# loop শুরুর আগে বানাতে হবে, ভেতরে না। ভেতরে বানালে প্রতিবার শূন্য হয়ে যাবে।
#
#   total_amount = 0.0
#   good_orders  = 0
#   cancelled    = 0

# TODO


# ---------- ধাপ ২: প্রতিটা লাইনের উপর loop চালান ----------
# ইঙ্গিত:
#
#   for raw in lines:
#       parts = raw.split(";")
#       ...
#
# ভেতরের কোডটা গত ক্লাসেরটাই — শুধু এবার একবার লিখছেন, দশবার না।

# TODO


# ---------- ধাপ ৩: loop-এর ভেতরে record পরিষ্কার করুন ----------
# order_id      → .strip().upper()
# customer_name → .strip().title()
# quantity      → int
# amount        → ৳ আর কমা সরিয়ে float
# payment       → .strip().lower()
# status        → .strip().lower()
#
# নামের ব্যাপারে একটা নতুন জিনিস:
#   গত ক্লাসে আমরা .replace("  ", " ") দিয়ে কাজ চালিয়েছিলাম। কিন্তু
#   "mim   begum"-এ তিনটা স্পেস — replace ওটা ধরতে পারে না।
#   আজ list শিখেছেন বলে সুন্দর সমাধানটা হাতে আছে:
#
#       name = " ".join(name.split())
#
#   .split() ফাঁকা জায়গা ধরে শব্দ আলাদা করে list বানায়, আর " ".join()
#   সেগুলো একটা করে স্পেস দিয়ে আবার জোড়া লাগায়।

# TODO


# ---------- ধাপ ৪: cancelled হলে বাদ দিন ----------
# ইঙ্গিত:
#
#   if status == "cancelled":
#       print(f"সতর্কতা: {order_id} বাতিল — হিসাবে ধরা হলো না")
#       cancelled = cancelled + 1
#       continue
#
# continue মানে — এই record-টা এখানেই ছেড়ে দাও, পরেরটায় যাও।

# TODO


# ---------- ধাপ ৫: এক লাইনে ছাপান, আর জমা করুন ----------
# প্রতিটা ঠিকঠাক record-এর জন্য:
#
#   print(f"{order_id}  {customer_name}  {item_name} — {quantity}টা  ৳{amount:.2f}")
#   total_amount = total_amount + amount
#   good_orders  = good_orders + 1

# TODO


# ---------- ধাপ ৬: সবচেয়ে বড় অর্ডারটা খুঁজুন ----------
# ইঙ্গিত: loop-এর আগে একটা ঘর রাখুন —
#
#   biggest_amount = 0.0
#   biggest_id     = ""
#
# আর loop-এর ভেতরে প্রতিবার মিলিয়ে দেখুন:
#
#   if amount > biggest_amount:
#       biggest_amount = amount
#       biggest_id     = order_id

# TODO


# ---------- ধাপ ৭: loop শেষ হলে সারাংশ ----------
# এই অংশটা loop-এর বাইরে, বাঁ দিক ঘেঁষে। ভেতরে রাখলে দশবার ছাপবে।
#
#   মোট অর্ডার (বাতিল বাদে): 9টা
#   বাতিল: 1টা
#   মোট টাকা: ৳5097.75
#   গড় অর্ডার: ৳566.42
#   সবচেয়ে বড়: ORD100045 — ৳1240.50

# TODO


# ---------- বোনাস (সময় থাকলে) ----------
# - যে অর্ডারগুলো bkash-এ হয়েছে, শুধু সেগুলোর মোট টাকা বের করুন
# - ৫০০ টাকার বেশি অর্ডার কয়টা, গুনুন
# - গত ক্লাসের কোডটা খুলে পাশে রাখুন। কত লাইন কমলো, গুনে দেখুন।
