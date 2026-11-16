# মডিউল ৩ — Python Core II ও III

conditional, loop, function আর module। গত মডিউলে যে কোড বারবার লিখতে
হচ্ছিল, এই মডিউলে সেটা একবার লিখেই চলবে।

---

## 🚀 ইন্টার‍্যাক্টিভ নোটবুক — ব্রাউজারেই চালান

দুইটা ক্লাসের সব বিষয় এক জায়গায়, নিজের হাতে চালিয়ে শেখার জন্য।
**কিছু ইনস্টল করা লাগবে না** — শুধু একটা Google অ্যাকাউন্ট।

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sadathasan4/ostad-de-bootcamp/blob/main/module-03/ThelaGari_Python_Lab_Module3.ipynb)

উপরের বোতামে ক্লিক করুন, অথবা এই লিংকটা:

```
https://colab.research.google.com/github/sadathasan4/ostad-de-bootcamp/blob/main/module-03/ThelaGari_Python_Lab_Module3.ipynb
```

ভেতরে যা আছে — ব্যাখ্যা, চালানোর মতো কোড, **নিজে চেষ্টা করুন** অনুশীলন,
লুকানো উত্তর, আর দুইটা মিনি-ল্যাব যেগুলো নিজেই মিলিয়ে দেখে বলে দেবে ঠিক
হয়েছে কি না।

> WSL-এ কাজ করতে অসুবিধা হলে এটা দিয়ে শুরু করুন। তবে অ্যাসাইনমেন্ট নিজের
> মেশিনেই করবেন — আসল কাজ ওখানেই হয়।

---

## ক্লাস ৫ — if, loop, list

### যা শিখবো

- `list` — একাধিক জিনিস এক নামে, আর শূন্য থেকে গোনা
- `for` loop — list-এর উপর দিয়ে হাঁটা, আর indentation
- `if / elif / else` — শর্ত দিয়ে পথ বাছা
- `and`, `or`, `not`, `in` — শর্ত জোড়া লাগানো
- `continue`, `break`, আর `while` চিনে রাখা
- জমা করা (accumulator) — total, count, সবচেয়ে বড়টা
- `.split()` আর `" ".join()` — একাধিক স্পেস সরানোর সুন্দর উপায়

### ল্যাব

গত ক্লাসের দশটা এলোমেলো record — এবার একটা loop-এ, কোড না বাড়িয়ে।

| ফাইল | কী |
|---|---|
| `starter/loop_records.py` | সাতটা TODO — ক্লাসে এটাই পূরণ করবেন |
| `solution/loop_records.py` | সমাধান — নিজে চেষ্টা করার পরে দেখবেন |
| `solution/EXPECTED_OUTPUT_class5.txt` | ঠিক কী ছাপা হওয়ার কথা |

data আসছে গত মডিউল থেকে — `module-02/data/raw_sales.txt`. নতুন কিছু
নামাতে হবে না।

চালানোর নিয়ম (repo-র **মূল ফোল্ডার** থেকে):

```bash
python3 module-03/starter/loop_records.py
```

### যে সংখ্যাগুলো মিলতে হবে

```
মোট অর্ডার (বাতিল বাদে): 9টা
বাতিল: 1টা
মোট টাকা: ৳5097.75
গড় অর্ডার: ৳566.42
সবচেয়ে বড়: ORD100045 — ৳1240.50
```

---

## ক্লাস ৬ — function আর module

### যা শিখবো

- `def` — কাজটাকে একটা নাম দেওয়া
- parameter আর argument — বাইরে থেকে জিনিস পাঠানো
- `return` — আর print বনাম return-এর পার্থক্য
- একাধিক parameter, default value
- scope — ভেতরের variable বাইরে নেই
- module — নিজের ফাইল `import` করা, আর `if __name__ == "__main__"`
- standard library — `statistics`, `os`, `datetime`

### ল্যাব

ক্লাস ৫-এর কোডটাই, এবার দুই ফাইলে গোছানো। উত্তর বদলাবে না।

| ফাইল | কী |
|---|---|
| `starter/sales_tools.py` | পাঁচটা function — পরিষ্কার করার যন্ত্রপাতি |
| `starter/report.py` | ফাইল পড়া, loop, হিসাব — sales_tools import করে |
| `solution/sales_tools.py` · `solution/report.py` | সমাধান |
| `solution/EXPECTED_OUTPUT_class6.txt` | ঠিক কী ছাপা হওয়ার কথা |

চালানোর নিয়ম — **আগে** `sales_tools.py`, **তারপর** `report.py`:

```bash
python3 module-03/starter/sales_tools.py
python3 module-03/starter/report.py
```

> `report.py` প্রথমবার চালালে `TypeError: ... 'NoneType' has no len()`
> আসবে। এটা স্বাভাবিক — `read_lines()` এখনো কিছু `return` করে না।

---

## অ্যাসাইনমেন্ট

**নিয়ম বদলেছে** — এখন থেকে প্রতি ক্লাসে না, প্রতি মডিউলে একটা
অ্যাসাইনমেন্ট, দুইটা ক্লাসের বিষয় মিলিয়ে।

- **মডিউল ৩: `assignments/module-03.md`** ← এটাই জমা দেবেন
- `assignments/class-05.md` — এখন মডিউল অ্যাসাইনমেন্টের লেভেল ১

---

## ফোল্ডার

```
module-03/
  starter/        TODO ভরা ফাইল — আপনি পূরণ করবেন
  solution/       সমাধান — পরে দেখবেন
  assignments/    মডিউলের শেষের কাজ
```
