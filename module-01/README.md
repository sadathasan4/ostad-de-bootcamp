# মডিউল ১ — Getting Started with Data Engineering

**সপ্তাহ ১** · দুইটা লাইভ ক্লাস

---

## ক্লাস ১ — The Data Engineering Landscape & Dev Environment Setup

### যা শিখবো

- Data Engineering জিনিসটা আসলে কী, আর Data Analyst / Data Scientist / ML
  Engineer-এর সাথে এর পার্থক্য কোথায়
- একটা কোম্পানিতে data কোন পথ ধরে যায় — ThelaGari-র উদাহরণে
- modern data stack-টা একনজরে
- নিজের মেশিনে কাজের পরিবেশ তৈরি: WSL, Python, VS Code, git

### ল্যাব

ThelaGari-র অক্টোবর মাসের অর্ডারের ফাইলটা পড়ে বের করুন:

1. ফাইলের সাইজ কত
2. কয়টা সারি আছে
3. কলামের নাম কী কী
4. কোন কলামে কী ধরনের data

```bash
# আপনি যেটা পূরণ করবেন
python3 module-01/starter/explore_csv.py

# মিলিয়ে দেখার জন্য (আগে নিজে চেষ্টা করুন)
python3 module-01/solution/explore_csv.py
```

**ফাইল:** `data/orders_oct2026.csv` — ৪৬,৯০৭টা অর্ডার, ১৪টা কলাম, ৫.৫ MB

সব ঘর ভরা নেই — কিছু জায়গা ফাঁকা। কেন ফাঁকা, সেটা নিয়ে ভাবুন। এই প্রশ্নটাই
পরের সপ্তাহগুলোর ভিত্তি।

---

## ক্লাস ২ — Linux Command Line for Data Work

### যা শিখবো

- ফাইল খোঁজা, দেখা, কাটা, জোড়া দেওয়া — সব terminal থেকে
- pipe আর redirection — ছোট ছোট টুল জুড়ে বড় কাজ
- file permission, environment variable
- `cron`-এর পরিচয়

### ল্যাব

`data/app_2026-10.log` ফাইলটায় ThelaGari-র server-এর এক মাসের log আছে —
১,০০,০০০ লাইন। **শুধু terminal ব্যবহার করে** (Python ছাড়া) বের করুন:

1. মোট কয়টা ERROR আছে
2. তারিখ অনুযায়ী কয়টা করে ERROR
3. ফলটা একটা নতুন ফাইলে লিখুন

সমাধান আর উত্তর মেলানোর জন্য: `solution/class2_commands.sh` আর
`solution/ANSWERS.md` — ক্লাস ২-এর পরে দেখবেন।

---

## ফোল্ডার

```
module-01/
  data/        ল্যাবের ফাইল — এগুলো বদলাবেন না
  starter/     আপনি যেগুলো পূরণ করবেন
  solution/    মেলানোর জন্য
```
