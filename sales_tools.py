#!/usr/bin/env python3
"""
ক্লাস ৬ — ল্যাব (১/২)

গত ক্লাসে পরিষ্কার করার কাজগুলো loop-এর ভেতরে ছড়িয়ে ছিল। আজ সেগুলোকে
নাম দিয়ে আলাদা করে রাখবো।

এই ফাইলটা নিজে কিছু হিসাব করে না — শুধু কয়েকটা function রাখে, যেগুলো
অন্য ফাইল থেকে ডেকে আনা যাবে। এরকম ফাইলকে বলে module.

পরীক্ষা করতে (repo-র মূল ফোল্ডার থেকে):

    python3 module-03/starter/sales_tools.py

TODO লেখা জায়গাগুলো আপনি পূরণ করবেন।
"""


# ---------- ১ ----------
def clean_id(text):
    """ফাঁকা জায়গা মুছে, সব বড় হাতের করে ফেরত দিন।

    "  ord100045 "  →  "ORD100045"
    """
    # ইঙ্গিত:  return text.strip().upper()
    # TODO


# ---------- ২ ----------
def clean_name(text):
    """নামের বাড়তি স্পেস সরিয়ে, প্রতি শব্দের প্রথম অক্ষর বড় করুন।

    "  RAHIM  uddin "  →  "Rahim Uddin"
    "mim   begum"      →  "Mim Begum"
    """
    # ইঙ্গিত: গত ক্লাসের সেই " ".join(...split()) কৌশলটা
    # TODO


# ---------- ৩ ----------
def clean_amount(text):
    """৳ আর কমা সরিয়ে টাকার অঙ্কটা সংখ্যায় ফেরত দিন।

    " ৳ 1,240.50 "  →  1240.5
    """
    # ইঙ্গিত: দুইবার .replace(), তারপর .strip(), তারপর float()
    # TODO


# ---------- ৪ ----------
def taka(amount):
    """সংখ্যাটাকে টাকার চেহারায় সাজিয়ে দিন।

    1240.5  →  "৳1240.50"
    """
    # ইঙ্গিত:  return f"৳{amount:.2f}"
    # TODO


# ---------- ৫ ----------
def is_cancelled(status):
    """অর্ডারটা বাতিল কি না — True বা False ফেরত দিন।"""
    # ইঙ্গিত: তুলনার ফলটাই True বা False, তাই সরাসরি return করা যায়
    # TODO


# ---------- নিজে চালালে একটা ছোট পরীক্ষা ----------
# এই অংশটা শুধু তখনই চলবে যখন আপনি এই ফাইলটা সরাসরি চালাবেন।
# report.py থেকে import করলে চলবে না। কেন — সেটা ক্লাসে বলবো।
if __name__ == "__main__":
    print("sales_tools — পরীক্ষা")
    print(clean_id("  ord100045 "))         # ORD100045
    print(clean_name("  RAHIM  uddin "))    # Rahim Uddin
    print(clean_name("mim   begum"))        # Mim Begum
    print(clean_amount(" ৳ 1,240.50 "))     # 1240.5
    print(taka(1240.5))                     # ৳1240.50
    print(is_cancelled(" CANCELLED "))      # True
