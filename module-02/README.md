# মডিউল ২ — Version Control & Python Entry

**সপ্তাহ ২** · দুইটা লাইভ ক্লাস

---

## ক্লাস ৩ — Git & GitHub

### যা শিখবো

- version control কেন লাগে — pipeline-এর কাজে কেন আরও বেশি লাগে
- Git-এর তিনটা জায়গা: working directory, staging area, repository
- commit, branch, merge, remote
- `.gitignore` — কোন ফাইল GitHub-এ যাবে না
- merge conflict — কেন হয়, কীভাবে সামলায়
- pull request-এর নিয়ম
- README লেখা

### ল্যাব

নিজের নামে একটা repo বানাবেন — `data-engineering-journey`। ছয় মাস ধরে
এখানেই আপনার সব কাজ জমা হবে, আর শেষে এটাই আপনার পোর্টফোলিওর একটা অংশ।

ধাপগুলো:

1. GitHub-এ `data-engineering-journey` নামে repo খুলুন (Public)
2. নিজের মেশিনে ফোল্ডার বানিয়ে `git init`
3. একটা README লিখুন — `templates/journey-README.md` থেকে শুরু করতে পারেন
4. `.gitignore` বসান — `templates/gitignore-template.txt` দেখুন
5. ক্লাস ২-এর কাজগুলো (log নিয়ে যে কমান্ডগুলো চালিয়েছিলেন) একটা ফাইলে
   রেখে commit করুন
6. GitHub-এ push করুন
7. একটা নতুন branch বানান, সেখানে কিছু যোগ করুন, push করুন
8. GitHub-এ pull request খুলে নিজেই merge করুন

### সাথে রাখুন

`GIT_CHEATSHEET.md` — রোজ যে কমান্ডগুলো লাগে, এক পাতায়। সাথে ভুল হলে
কী করবেন তার তালিকাও আছে।

---

## ক্লাস ৪ — Python Core I

### যা শিখবো

- variable, আর কয়েক রকম data type
- type casting — `"24"` থেকে `24`
- operator, f-string
- string নিয়ে কাজ — `.strip()`, `.split()`, `.replace()`, `.lower()`

### ল্যাব

এলোমেলো কাঁচা sales record পরিষ্কার করে ঠিক type-এ বসানো।

| ফাইল | কী |
|---|---|
| `data/raw_sales.txt` | দশটা এলোমেলো record — ল্যাব আর অ্যাসাইনমেন্টের কাঁচামাল |
| `starter/clean_record.py` | ছয়টা TODO — ক্লাসে এটাই পূরণ করবেন |
| `solution/clean_record.py` | সমাধান — নিজে চেষ্টা করার পরে দেখবেন |
| `solution/EXPECTED_OUTPUT_class4.txt` | ঠিক কী ছাপা হওয়ার কথা |

চালানোর নিয়ম (repo-র মূল ফোল্ডার থেকে):

```bash
python3 module-02/starter/clean_record.py
```

---

## অ্যাসাইনমেন্ট

- ক্লাস ৩: `assignments/class-03.md`
- ক্লাস ৪: `assignments/class-04.md`

---

## ফোল্ডার

```
module-02/
  data/           ল্যাবের কাঁচা ফাইল
  starter/        TODO ভরা ফাইল — আপনি পূরণ করবেন
  solution/       সমাধান — পরে দেখবেন
  templates/      নিজের repo-তে বসানোর জন্য নমুনা ফাইল
  assignments/    ক্লাসের পরের কাজ
  GIT_CHEATSHEET.md
```
