# মডিউল ৪ — dictionary আর ডেটা নিয়ে কাজ

মডিউল ৩-এর অ্যাসাইনমেন্টে payment ধরে হিসাব করতে দশটা variable আর পাঁচটা
`elif` লাগছিল। এই মডিউলে সেটা তিন লাইনে নামবে।

---

## 🚀 ইন্টার‍্যাক্টিভ নোটবুক — ব্রাউজারেই চালান

ক্লাসের সব বিষয় এক জায়গায়, নিজের হাতে চালিয়ে শেখার জন্য।
**কিছু ইনস্টল করা লাগবে না** — শুধু একটা Google অ্যাকাউন্ট।

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sadathasan4/ostad-de-bootcamp/blob/main/module-04/ThelaGari_Python_Lab_Module4.ipynb)

```
https://colab.research.google.com/github/sadathasan4/ostad-de-bootcamp/blob/main/module-04/ThelaGari_Python_Lab_Module4.ipynb
```

ভেতরে — ব্যাখ্যা, চালানোর মতো কোড, **নিজে চেষ্টা করুন** অনুশীলন, লুকানো
উত্তর, একটা মিনি-ল্যাব আর দুইটা চ্যালেঞ্জ। সবগুলোই নিজে মিলিয়ে দেখে বলে
দেবে ঠিক হয়েছে কি না।

> ক্লাস ৮-এর অংশ (CSV আর JSON) সোমবারের ক্লাসের পরে এই নোটবুকেই যোগ হবে।
> মডিউল ৩-এর নোটবুক: `module-03/ThelaGari_Python_Lab_Module3.ipynb`

---

## ক্লাস ৭ — dictionary

### যা শিখবো

- `dictionary` — নাম ধরে জিনিস রাখা আর খোঁজা
- পড়া — `[]` বনাম `.get()`, আর `KeyError`
- যোগ, বদল, মোছা — `del`, `.pop()`
- loop — `for k in d`, `.values()`, `.items()`, `sorted()`
- **গোনা আর জমা করার প্যাটার্ন** — `d[k] = d.get(k, 0) + x`
- record = dictionary — `parts[5]` আর মনে রাখতে হবে না
- list-এর ভেতরে dictionary — API আর JSON-এর আসল গড়ন

### ল্যাব

গত মডিউলের সেই একই হিসাব, এবার dictionary দিয়ে।

| ফাইল | কী |
|---|---|
| `starter/sales_dict.py` | সাতটা TODO — ক্লাসে এটাই পূরণ করবেন |
| `starter/sales_tools.py` | গত মডিউলের সেই ফাইলটাই, পাশে কপি করা |
| `solution/sales_dict.py` | সমাধান — নিজে চেষ্টা করার পরে দেখবেন |
| `solution/EXPECTED_OUTPUT_class7.txt` | ঠিক কী ছাপা হওয়ার কথা |

data আসছে মডিউল ২ থেকে — `module-02/data/raw_sales.txt`.

চালানোর নিয়ম (repo-র **মূল ফোল্ডার** থেকে):

```bash
python3 module-04/starter/sales_dict.py
```

### যে সংখ্যাগুলো মিলতে হবে

```
bkash              3টা   ৳2484.00
nagad              2টা   ৳908.00
card               1টা   ৳812.00
cash on delivery   2টা   ৳661.50
rocket             1টা   ৳232.25
সব মিলিয়ে                ৳5097.75

সবচেয়ে বেশি টাকার দিন: 2026-10-07 — ৳1590.50
সবচেয়ে বড় অর্ডার: ORD100045 — ৳1240.50
```

> **৳5097.75** — এই সংখ্যাটা ক্লাস ৫, ৬ আর ৭-এ একই। কোড তিনবার বদলেছে,
> উত্তর বদলায়নি। এটাই ঠিক পথে আছেন তার প্রমাণ।

---

## ক্লাস ৮ — (আসছে)

CSV আর JSON — আসল ফাইল পড়া আর লেখা।

---

## অ্যাসাইনমেন্ট

প্রতি মডিউলে একটা, মডিউলের শেষে। **মডিউল ৪-এর অ্যাসাইনমেন্ট ক্লাস ৮-এ
পাবেন** — দুই ক্লাসের বিষয় মিলিয়ে।

যাঁদের মডিউল ৩-এরটা এখনো বাকি: `module-03/assignments/module-03.md`

---

## ফোল্ডার

```
module-04/
  starter/        TODO ভরা ফাইল — আপনি পূরণ করবেন
  solution/       সমাধান — পরে দেখবেন
  assignments/    মডিউলের শেষের কাজ (ক্লাস ৮-এ আসবে)
```
