# Git — যেটুকু রোজ লাগে

ক্লাস ৩-এর সাথে রাখার জন্য। মুখস্থ করবেন না — দরকারের সময় দেখে নেবেন।

---

## একবারের সেটআপ

```bash
git config --global user.name "আপনার নাম"
git config --global user.email "আপনার@ইমেইল"
git config --global init.defaultBranch main
git config --global credential.helper store    # একবার টোকেন দিলে মনে রাখবে
```

ইমেইলটা GitHub অ্যাকাউন্টের ইমেইলই দেবেন, নইলে commit আপনার নামে দেখাবে না।

## রোজকার চারটা কমান্ড

| কমান্ড | কী করে |
|---|---|
| `git status` | এখন কী অবস্থা — সবচেয়ে বেশি লাগে এটাই |
| `git add file.py` | এই ফাইলটা পরের commit-এ যাবে |
| `git add .` | সব বদলানো ফাইল |
| `git commit -m "বার্তা"` | ছবি তুলে রাখা |
| `git push` | GitHub-এ পাঠানো |

> আটকে গেলে সবার আগে `git status`. ও বলে দেয় এখন কী অবস্থা, আর পরের
> কাজটা কী হতে পারে।

## দেখা

| কমান্ড | কী করে |
|---|---|
| `git log --oneline` | commit-এর তালিকা, এক লাইনে করে |
| `git log --oneline -5` | শেষ পাঁচটা |
| `git diff` | যা বদলেছে কিন্তু এখনো add করা হয়নি |
| `git diff --staged` | যা add করা হয়েছে কিন্তু commit হয়নি |
| `git show` | শেষ commit-এ ঠিক কী বদলেছিল |

## নতুন repo শুরু করা

```bash
mkdir data-engineering-journey && cd data-engineering-journey
git init
echo "# আমার Data Engineering যাত্রা" > README.md
git add README.md
git commit -m "প্রথম commit"
git remote add origin https://github.com/USERNAME/data-engineering-journey.git
git push -u origin main
```

`-u` শুধু প্রথমবার লাগে। এরপর থেকে `git push` লিখলেই হবে।

## আগের repo নামানো

```bash
git clone https://github.com/sadathasan4/ostad-de-bootcamp.git
cd ostad-de-bootcamp
git pull            # পরে নতুন কিছু এলে
```

## Branch

| কমান্ড | কী করে |
|---|---|
| `git branch` | কী কী branch আছে, আমি কোনটায় |
| `git switch -c add-notes` | নতুন branch বানিয়ে ওখানে চলে যাওয়া |
| `git switch main` | main-এ ফেরা |
| `git merge add-notes` | ওই branch-এর কাজ এখানে জুড়ে দেওয়া |
| `git push -u origin add-notes` | নতুন branch GitHub-এ পাঠানো |

branch মানে — মূল কাজটা ঠিক রেখে পাশে বসে নতুন কিছু চেষ্টা করা। ভালো
হলে জুড়ে দেবেন, না হলে ফেলে দেবেন।

## Merge conflict হলে

দুইটা branch-এ একই লাইন বদলালে Git নিজে ঠিক করতে পারে না। তখন ফাইলে
এরকম দেখাবে:

```
<<<<<<< HEAD
main-এ যা লেখা ছিল
=======
অন্য branch-এ যা লেখা ছিল
>>>>>>> add-notes
```

করণীয়:

1. ফাইলটা খুলুন
2. ঠিক করে লিখুন কোনটা রাখবেন (বা দুইটাই মিলিয়ে)
3. `<<<<<<<`, `=======`, `>>>>>>>` — এই তিনটা লাইন মুছে দিন
4. `git add file.md` তারপর `git commit`

ভয়ের কিছু নেই। conflict মানে Git আপনাকে জিজ্ঞেস করছে — কোনটা রাখবো?

## Pull request

GitHub-এর জিনিস, Git-এর না।

1. branch-টা push করুন
2. GitHub-এ গেলে একটা হলুদ পট্টি দেখাবে — **Compare & pull request**
3. কী বদলেছেন লিখে **Create pull request**
4. **Merge pull request** → **Confirm merge**
5. নিজের মেশিনে ফিরে: `git switch main` তারপর `git pull`

চাকরিতে আপনি নিজের PR নিজে merge করবেন না — অন্য কেউ দেখে দেবে। কিন্তু
নিয়মটা একই।

## .gitignore

যে ফাইলগুলো GitHub-এ যাবে না, তার তালিকা। repo-র মূল ফোল্ডারে
`.gitignore` নামে একটা ফাইল:

```
.venv/
__pycache__/
*.pyc
.env
*.csv
.DS_Store
```

**`.env` কখনো push করবেন না।** ওখানে পাসওয়ার্ড আর API key থাকে। একবার
GitHub-এ উঠে গেলে মুছলেও ইতিহাসে থেকে যায়।

## ভুল হলে

| অবস্থা | কী করবেন |
|---|---|
| commit বার্তা ভুল লিখেছি | `git commit --amend -m "নতুন বার্তা"` (push করার আগে) |
| ফাইল add করে ফেলেছি, চাই না | `git restore --staged file.py` |
| ফাইলের বদল ফেলে দিতে চাই | `git restore file.py` — **ফেরত পাবেন না** |
| push করতে গিয়ে rejected | আগে `git pull` দিন, তারপর push |
| ভুল branch-এ কাজ করে ফেলেছি | commit করে ফেলুন, তারপর গ্রুপে জিজ্ঞেস করুন |

## commit বার্তা কেমন হবে

```
খারাপ                       ভালো
-----                       ----
update                      Add log parsing commands from class 2
fix                         Fix wrong date range in error count
asdf                        Add README with project summary
changes                     Remove hardcoded API key, use .env
```

নিয়মটা সহজ — ছয় মাস পরে আপনি নিজে পড়ে যেন বুঝতে পারেন কী করেছিলেন।

---

## আটকে গেলে

```bash
git status      # প্রায় সব প্রশ্নের উত্তর এখানে আছে
```

আর গ্রুপে লেখার সময় তিনটা জিনিস দেবেন — কী করতে চেয়েছিলেন, কোন কমান্ড
দিয়েছিলেন, আর `git status` কী বলছে।
