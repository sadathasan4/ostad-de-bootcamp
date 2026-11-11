# মডিউল ৩ — Python Core II

conditional আর loop। গত মডিউলে যে কোড বারবার লিখতে হচ্ছিল, এই মডিউলে
সেটা একবার লিখেই চলবে।

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

## অ্যাসাইনমেন্ট

- ক্লাস ৫: `assignments/class-05.md`

---

## ফোল্ডার

```
module-03/
  starter/        TODO ভরা ফাইল — আপনি পূরণ করবেন
  solution/       সমাধান — পরে দেখবেন
  assignments/    ক্লাসের পরের কাজ
```
