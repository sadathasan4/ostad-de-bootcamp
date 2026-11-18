#!/usr/bin/env python3
"""
ক্লাস ৬ — ল্যাব (২/২)

গত ক্লাসের সেই একই কাজ, একই উত্তর। পার্থক্য শুধু — পরিষ্কার করার কাজগুলো
এখন sales_tools module-এ, আর এই ফাইলটা সেগুলো ডেকে আনে।

চালান (repo-র মূল ফোল্ডার থেকে):

    python3 module-03/starter/report.py

আগে sales_tools.py শেষ করবেন, তারপর এটা।
"""

import os
import statistics

import sales_tools          # পাশের ফাইলটা — নামের শেষে .py লিখবেন না

PATH = os.path.join("module-02", "data", "raw_sales.txt")


# ---------- ১ ----------
def read_lines(path):
    """ফাইলটা পড়ে প্রতিটা লাইনকে list-এর একটা ঘরে বসিয়ে ফেরত দিন।"""
    # ইঙ্গিত: গত ক্লাসের সেই with open(...) অংশটাই, শুধু return দিতে হবে
    # TODO


# ---------- ২ ----------
def summarise(lines):
    """সব record ঘুরে দেখে — মোট, গড়, সবচেয়ে বড়টা ফেরত দিন।

    ফেরত দেবে চারটা জিনিস:  amounts, cancelled, biggest_id, biggest_amount
    """
    amounts = []
    cancelled = 0
    biggest_id = ""
    biggest_amount = 0.0

    for raw in lines:
        parts = raw.split(";")

        # TODO: sales_tools-এর function গুলো ডেকে ঘরগুলো বানান
        #
        #   order_id = sales_tools.clean_id(parts[0])
        #   name     = sales_tools.clean_name(parts[2])
        #   item     = parts[3].strip()
        #   quantity = int(parts[4].strip())
        #   amount   = sales_tools.clean_amount(parts[5])
        #   status   = parts[7]

        # TODO: বাতিল হলে সতর্কবার্তা, cancelled বাড়ান, আর continue

        # TODO: এক লাইনে ছাপান, আর amounts.append(amount)
        #       খেয়াল করুন — list-এ append করলে ফল বসাতে হয় না

        # TODO: সবচেয়ে বড়টা মিলিয়ে দেখুন

        pass        # সব TODO লেখা হলে এই লাইনটা মুছে দেবেন

    return amounts, cancelled, biggest_id, biggest_amount


# ---------- ৩ ----------
def main():
    """পুরো কাজটা এখান থেকে চলবে।"""
    lines = read_lines(PATH)
    print(f"ফাইলে লাইন আছে: {len(lines)}টা")
    print()

    amounts, cancelled, biggest_id, biggest_amount = summarise(lines)

    # TODO: সারাংশ ছাপান — গত ক্লাসের মতোই, কিন্তু টাকার জায়গায়
    #       sales_tools.taka() ব্যবহার করবেন
    #
    #   মোট অর্ডার (বাতিল বাদে): 9টা
    #   বাতিল: 1টা
    #   মোট টাকা: ৳5097.75          ← sum(amounts)
    #   গড় অর্ডার: ৳566.42          ← statistics.mean(amounts)
    #   সবচেয়ে বড়: ORD100045 — ৳1240.50


if __name__ == "__main__":
    main()


# ---------- বোনাস (সময় থাকলে) ----------
# - sales_tools-এ আরেকটা function যোগ করুন: unit_price(amount, quantity)
# - summarise() কে দুইটা ছোট function-এ ভাগ করা যায় কি না ভেবে দেখুন
# - গত ক্লাসের loop_records.py পাশে খুলে দেখুন — একই উত্তর, কিন্তু কোনটা
#   ছয় মাস পরে পড়তে সহজ লাগবে?
