# অ্যাসাইনমেন্ট ৫ — loop আর শর্ত দিয়ে হিসাব

**মডিউল ৩ · ক্লাস ৫** · সময় লাগবে ৩০–৪০ মিনিট · জমা দেবেন পরের ক্লাসের আগে

---

## কী করতে হবে

ক্লাসের ল্যাবে আপনি দশটা record-এর **মোট** বের করেছেন। এবার বের করবেন
**কোন payment method-এ কত টাকা**।

একই ফাইল, একই loop — শুধু ভেতরে কয়েকটা `if` যোগ হবে।

শেষে জমা দেবেন **আপনার repo-র লিংকটা**।

আটকে গেলে `module-03/starter/loop_records.py` খুলুন, ইঙ্গিত ওখানেই আছে।
আর না হলে সাপোর্ট ক্লাসে আসুন (রবি, মঙ্গল, বৃহস্পতি — রাত ৯টা)।

---

## ধাপ ১ — নতুন ফাইলগুলো নামিয়ে নিন

```bash
cd ~/de-bootcamp/ostad-de-bootcamp
git pull
```

> ফোল্ডারের নামের শেষে `-main` থাকলে ওটা ZIP, clone না — `git pull` চলবে না।
> একবার `git clone` করে নিন, তাহলে প্রতি সপ্তাহে শুধু `git pull` দিলেই হবে।

---

## ধাপ ২ — নিজের repo-তে জায়গা বানান

```bash
cd ~/de-bootcamp/data-engineering-journey
mkdir -p week-03
```

এখানে একটা ফাইল বানাবেন — `payment_totals.py`.

---

## ধাপ ৩ — ফাইলটা পড়ুন

এই অংশটা ল্যাবের মতোই, হুবহু কপি করতে পারেন:

```python
import os

PATH = os.path.join("module-02", "data", "raw_sales.txt")

with open(PATH, encoding="utf-8") as fh:
    lines = fh.read().strip().split("\n")
```

> চালাবেন repo-র **মূল ফোল্ডার** থেকে, নইলে ফাইলটা খুঁজে পাবে না।

---

## ধাপ ৪ — পাঁচটা জমার ঘর বানান

loop শুরুর **আগে**। ভেতরে বানালে প্রতিবার শূন্য হয়ে যাবে।

```python
bkash_total = 0.0
nagad_total = 0.0
card_total  = 0.0
rocket_total = 0.0
cash_total  = 0.0
```

গোনার জন্য আরো পাঁচটা ঘর লাগবে — `bkash_count`, `nagad_count`, এভাবে।

---

## ধাপ ৫ — loop চালান

প্রতিটা লাইনের জন্য:

| ধাপ | কী |
|---|---|
| ১ | `.split(";")` দিয়ে টুকরো করুন |
| ২ | `amount` আর `payment` আর `status` বের করুন |
| ৩ | `status` যদি `cancelled` হয় — `continue` |
| ৪ | `payment` মিলিয়ে ঠিক ঘরে যোগ করুন |

চার নম্বর ধাপটা `if / elif / else` দিয়ে:

```python
if payment == "bkash":
    bkash_total = bkash_total + amount
    bkash_count = bkash_count + 1
elif payment == "nagad":
    ...
else:
    cash_total = cash_total + amount
    cash_count = cash_count + 1
```

> `cash on delivery` ফাইলে দুই বানানে আছে — `Cash on Delivery` আর
> `CASH ON DELIVERY`। `.lower()` দিলে দুইটাই এক হয়ে যাবে।

---

## ধাপ ৬ — loop-এর বাইরে ছাপান

এই অংশটা **বাঁ দিক ঘেঁষে**, নইলে দশবার ছাপবে।

```
payment ধরে হিসাব (বাতিল বাদে)

bkash             3টা   ৳2484.00
nagad             2টা   ৳908.00
card              1টা   ৳812.00
rocket            1টা   ৳232.25
cash on delivery  2টা   ৳661.50

সব মিলিয়ে: ৳5097.75
```

এই সংখ্যাগুলোই আসতে হবে। **সব মিলিয়ে ৳5097.75** — এটা ল্যাবের মোট টাকার
সমান। না মিললে কোথাও একটা ঘর বাদ পড়েছে।

---

## ধাপ ৭ — জমা দিন

```bash
cd ~/de-bootcamp/data-engineering-journey
git add week-03/payment_totals.py
git commit -m "Add payment-wise totals using loop and conditions"
git push
```

তারপর GitHub-এ দেখে নিন ফাইলটা উঠেছে কি না, আর repo-র লিংক জমা দিন।

---

## বোনাস (যাঁরা এগিয়ে)

কোন **তারিখে** সবচেয়ে বেশি টাকার অর্ডার হয়েছে, সেটা বের করুন। পাঁচটা
তারিখ আছে — `2026-10-07` থেকে `2026-10-11`।

নিয়মটা একই: পাঁচটা ঘর, আর `if / elif` দিয়ে ঠিক ঘরে যোগ।

> দশটা ঘর, তারপর আরো পাঁচটা — বিরক্তিকর লাগছে, তাই না? ঠিক এই
> বিরক্তিটার সমাধান **dictionary**, যেটা সোমবারের ক্লাসে। তখন এই পুরো
> জিনিসটা তিন লাইনে নেমে আসবে। আজকের বিরক্তিটা মনে রাখুন।

---

## আটকে গেলে

| যা দেখছেন | কী করবেন |
|---|---|
| `IndentationError` | কোলনের পরের লাইন চার স্পেস ভেতরে ঠেলুন |
| `SyntaxError: invalid syntax` | কোলন নেই, অথবা `==` এর জায়গায় `=` দিয়েছেন |
| সব টাকা একটাই ঘরে ঢুকছে | `.lower()` দিতে ভুলে গেছেন — `BKASH` আর `bkash` এক না |
| মোট মিলছে না | `cancelled`-টা বাদ দিয়েছেন তো? |
| হিসাব দশবার ছাপছে | `print`-গুলো loop-এর ভেতরে রয়ে গেছে, বাইরে আনুন |
| `FileNotFoundError` | repo-র মূল ফোল্ডার থেকে চালাচ্ছেন কি না দেখুন |

error-এর **শেষ লাইনটা** পড়বেন — ওখানেই বলা থাকে কী সমস্যা।
