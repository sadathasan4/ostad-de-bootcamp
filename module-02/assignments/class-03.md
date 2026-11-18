# অ্যাসাইনমেন্ট ৩ — Git আর GitHub

**মডিউল ২ · ক্লাস ৩** · সময় লাগবে ৩০–৪০ মিনিট · জমা দেবেন পরের ক্লাসের আগে

---

## কী করতে হবে

আজকের ক্লাসে যেটা শুরু করেছেন, সেটাই শেষ করা। সাতটা ধাপ।

শেষে জমা দেবেন **আপনার repo-র লিংকটা** — আর কিছু না। আমি খুলে দেখে নেবো।

আটকে গেলে `module-02/GIT_CHEATSHEET.md` খুলুন, আর না হলে সাপোর্ট ক্লাসে আসুন।

---

## ধাপ ১ — পরিচয় দেওয়া আছে কি না দেখুন

```bash
git config --global user.name
git config --global user.email
```

দুইটাই খালি এলে বসিয়ে নিন:

```bash
git config --global user.name "আপনার নাম"
git config --global user.email "আপনার@ইমেইল"
```

> ইমেইলটা GitHub অ্যাকাউন্টের ইমেইলই দেবেন। না দিলে commit আপনার নামে
> দেখাবে না।

## ধাপ ২ — repo দাঁড় করান

ক্লাসে যদি শেষ না হয়ে থাকে:

```bash
cd ~/de-bootcamp
mkdir -p data-engineering-journey && cd data-engineering-journey
git init
```

GitHub-এ `data-engineering-journey` নামে একটা **Public** repo খুলুন।

## ধাপ ৩ — README লিখুন

অন্তত তিন লাইন। কী কী থাকবে:

- এই repo-তে কী আছে
- আপনি কে, দুই লাইনে
- এখন পর্যন্ত কী কী শিখেছেন

নমুনা আছে `module-02/templates/journey-README.md`-তে। কপি করে নিজের মতো
বদলে নিন — হুবহু রাখবেন না।

## ধাপ ৪ — .gitignore বসান

```bash
cp ~/de-bootcamp/ostad-de-bootcamp-main/module-02/templates/gitignore-template.txt .gitignore
```

(পথটা আপনার মেশিনে আলাদা হতে পারে — টেমপ্লেটটা যেখানে আছে সেখান থেকে নেবেন)

## ধাপ ৫ — অন্তত তিনটা commit

একবারে সব add করে একটা commit দেবেন না। ছোট ছোট করে করুন:

```bash
git add README.md
git commit -m "Add README with intro and progress"

git add .gitignore
git commit -m "Add gitignore for python and data files"
```

তৃতীয় commit-এ ক্লাস ২-এর কাজটা যোগ করুন — log নিয়ে যে কমান্ডগুলো
চালিয়েছিলেন, সেগুলো একটা ফাইলে রেখে:

```bash
mkdir -p week-02
nano week-02/linux-commands.md      # কমান্ডগুলো লিখে রাখুন
git add week-02/
git commit -m "Add class 2 linux commands"
```

**commit বার্তা কেমন হবে** — ছয় মাস পরে আপনি নিজে পড়ে যেন বুঝতে পারেন
কী করেছিলেন।

```
খারাপ           ভালো
update          Add README with intro and progress
fix             Add gitignore for python and data files
asdf            Add class 2 linux commands
```

## ধাপ ৬ — GitHub-এ পাঠান

```bash
git remote add origin https://github.com/আপনার-ইউজারনেম/data-engineering-journey.git
git push -u origin main
```

পাসওয়ার্ড চাইলে **টোকেন** দেবেন, GitHub-এর পাসওয়ার্ড না।

## ধাপ ৭ — একটা pull request

```bash
git switch -c update-readme
```

README-তে একটা লাইন যোগ করুন (যেমন — আজ Git শিখেছেন, সেটা লিখুন)।

```bash
git add README.md
git commit -m "Add Git to skills section"
git push -u origin update-readme
```

এবার GitHub-এ যান। হলুদ পট্টিতে **Compare & pull request** → বর্ণনায়
দুই লাইন লিখুন → **Create pull request** → **Merge pull request**।

শেষে নিজের মেশিনে ফিরুন:

```bash
git switch main
git pull
```

---

## বোনাস — কোর্সের repo clone করুন

```bash
cd ~/de-bootcamp
git clone https://github.com/sadathasan4/ostad-de-bootcamp.git
```

এরপর থেকে নতুন সপ্তাহের ফাইল পেতে শুধু:

```bash
cd ostad-de-bootcamp
git pull
```

আর কখনো ZIP নামাতে হবে না। পুরোনো ফোল্ডারটা মুছবেন না — ওখানে আপনার
নিজের কাজ আছে, হাতে কপি করে নতুনটায় নিয়ে নেবেন।

---

## জমা দেওয়ার নিয়ম

শুধু আপনার repo-র লিংক পাঠাবেন:

```
https://github.com/আপনার-ইউজারনেম/data-engineering-journey
```

আমি খুলে দেখবো —

- README-তে অন্তত তিন লাইন আছে কি না
- `.gitignore` আছে কি না
- অন্তত তিনটা commit আছে কি না, আর বার্তাগুলো পড়ে বোঝা যায় কি না
- একটা merge হওয়া pull request আছে কি না

---

## কয়েকটা কথা

**সব ধাপ শেষ না হলেও লিংকটা পাঠাবেন।** যতটুকু হয়েছে ততটুকুই। কোথায়
আটকেছেন সেটা দেখেই আমি বুঝবো কী নিয়ে পরের ক্লাসে কথা বলতে হবে।

**error এলে পুরো লেখাটা গ্রুপে পেস্ট করবেন।** "push হচ্ছে না" লিখলে কেউ
সাহায্য করতে পারবে না। Git-এর error সাধারণত পড়লেই বোঝা যায় কী চাইছে।

**টোকেনটা কাউকে পাঠাবেন না।** গ্রুপে স্ক্রিনশট দেওয়ার আগে দেখে নেবেন
ওখানে টোকেন দেখা যাচ্ছে কি না।
