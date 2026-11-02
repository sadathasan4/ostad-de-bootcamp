# ক্লাস ২ — ল্যাবের উত্তর

ফাইল: `module-01/data/app_2026-10.log` — ১,০০,০০০ লাইন, ৮.০ MB

## মূল তিনটা প্রশ্ন

| প্রশ্ন | উত্তর |
|---|---|
| মোট ERROR | **৪,৮২৭** |
| `grep -c ERROR` দিলে আসে | ৪,৮৮৭ — ৬০টা বেশি |
| সবচেয়ে খারাপ দিন | **১৭ অক্টোবর, ৭৮১টা ERROR** |

৬০টা বেশি কেন — কিছু WARN লাইনের বার্তার ভেতরেই `ERROR_CODE=502` জাতীয় লেখা আছে।
তাই `grep -c "| ERROR |"` লিখতে হয়, যাতে level-এর ঘরটাই মেলে।

```
2026-10-01 03:10:24 | WARN  | ingest.api      | gateway sent ERROR_CODE=429, backing off
```

## তারিখ অনুযায়ী — উপরের পাঁচটা

```
 781 2026-10-17
 264 2026-10-19
 243 2026-10-18
 168 2026-10-13
 166 2026-10-14
```

স্বাভাবিক দিনে ১২০–১৭০টার মধ্যে থাকে। ১৭ তারিখ তার পাঁচ গুণ, আর ১৮–১৯ তারিখেও
রেশ থেকে গেছে।

## পুরো ফাইলে level-এর হিসাব

```
78306 INFO
12884 WARN
 4827 ERROR
 3983 DEBUG
```

## কোন component-এ সবচেয়ে বেশি ERROR

```
1308 ingest.api
 998 transform
 956 loader
 691 ingest.scraper
 632 scheduler
 242 auth
```

## ১৭ তারিখে আসলে কী হয়েছিল

সবচেয়ে বেশি যে বার্তাগুলো:

```
 65  deadlock detected while writing staging.orders
 55  worker did not respond to heartbeat
 55  invalid json in response body
 52  disk write failed, no space left on device
 47  job orders_hourly failed, exit code 1
```

ERROR সারাদিন ছড়ানো, কোনো এক ঘণ্টায় জমে নেই (ঘণ্টায় ৩০–৩৫টা করে)।

পড়লে একটা গল্প দাঁড়ায় — ডিস্ক ভরে যাওয়ায় loader আটকে গেছে, তাতে deadlock,
তাতে worker-এর heartbeat মিস, তাতে job ফেল। মানে একটা সমস্যা থেকে আরও
চারটা। এটাই বাস্তবে হয়, আর এজন্যই log পড়তে জানা দরকার।

> ক্লাসে এই জায়গাটায় থামুন। সংখ্যা বের করা অর্ধেক কাজ — সংখ্যাটা পড়ে গল্পটা
> বলতে পারাটাই বাকি অর্ধেক।
