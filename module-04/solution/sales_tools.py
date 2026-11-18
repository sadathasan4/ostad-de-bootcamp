#!/usr/bin/env python3
"""
ক্লাস ৬ — ল্যাবের সমাধান (১/২)

ThelaGari-র record পরিষ্কার করার যন্ত্রপাতি। এই ফাইলটা নিজে কিছু ছাপায় না —
এটা শুধু কয়েকটা function রাখে, যেগুলো অন্য ফাইল থেকে ব্যবহার করা যায়।

এরকম ফাইলকে বলে module.
"""


def clean_id(text):
    """ঘরের আগে-পরের ফাঁকা জায়গা মুছে, সব বড় হাতের করে ফেরত দেয়।

    "  ord100045 "  →  "ORD100045"
    """
    return text.strip().upper()


def clean_name(text):
    """নামের বাড়তি স্পেস সরিয়ে, প্রতি শব্দের প্রথম অক্ষর বড় করে দেয়।

    "  RAHIM  uddin "  →  "Rahim Uddin"
    "mim   begum"      →  "Mim Begum"
    """
    return " ".join(text.strip().title().split())


def clean_amount(text):
    """৳ আর কমা সরিয়ে টাকার অঙ্কটা সংখ্যায় ফেরত দেয়।

    " ৳ 1,240.50 "  →  1240.5
    """
    text = text.replace("৳", "").replace(",", "").strip()
    return float(text)


def taka(amount):
    """সংখ্যাটাকে টাকার চেহারায় সাজিয়ে দেয়।

    1240.5  →  "৳1240.50"
    """
    return f"৳{amount:.2f}"


def is_cancelled(status):
    """অর্ডারটা বাতিল কি না — True বা False ফেরত দেয়।"""
    return status.strip().lower() == "cancelled"


# ---------- নিজে চালালে একটা ছোট পরীক্ষা ----------
# এই অংশটা শুধু তখনই চলবে যখন আপনি এই ফাইলটা সরাসরি চালাবেন।
# অন্য ফাইল থেকে import করলে চলবে না।
if __name__ == "__main__":
    print("sales_tools — পরীক্ষা")
    print(clean_id("  ord100045 "))
    print(clean_name("  RAHIM  uddin "))
    print(clean_name("mim   begum"))
    print(clean_amount(" ৳ 1,240.50 "))
    print(taka(1240.5))
    print(is_cancelled(" CANCELLED "))
