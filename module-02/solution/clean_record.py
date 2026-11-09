#!/usr/bin/env python3
"""
ক্লাস ৪ — ল্যাবের সমাধান

starter ফাইলটার হুবহু একই গড়ন, শুধু TODO-গুলো পূরণ করা।
নিজে চেষ্টা করার পরেই এটা দেখুন।

চালান:  python3 module-02/solution/clean_record.py
"""

raw = "  ord100045 ; 2026-10-07 ;  RAHIM  uddin ; Miniket Chal 5kg ; 2 ; ৳ 1,240.50 ; BKASH ; delivered"


# ---------- ধাপ ১: আটটা টুকরোয় ভাগ ----------
parts = raw.split(";")

order_id      = parts[0]
order_date    = parts[1]
customer_name = parts[2]
item_name     = parts[3]
quantity_text = parts[4]
amount_text   = parts[5]
payment       = parts[6]
status        = parts[7]


# ---------- ধাপ ২: বাড়তি ফাঁকা জায়গা ----------
order_id      = order_id.strip()
order_date    = order_date.strip()
customer_name = customer_name.strip()
item_name     = item_name.strip()
quantity_text = quantity_text.strip()
amount_text   = amount_text.strip()
payment       = payment.strip()
status        = status.strip()


# ---------- ধাপ ৩: হাতের অক্ষর ----------
order_id      = order_id.upper()        # ord100045 → ORD100045
customer_name = customer_name.title()   # RAHIM  uddin → Rahim  Uddin
payment       = payment.lower()         # BKASH → bkash
status        = status.lower()

# নামের মাঝখানে দুইটা স্পেস ছিল — একটায় নামিয়ে আনি
customer_name = customer_name.replace("  ", " ")


# ---------- ধাপ ৪: সংখ্যায় বদলানো ----------
quantity = int(quantity_text)

# ৳ আর কমা সরানোর আগে float() কাজ করবে না
amount_text = amount_text.replace("৳", "").replace(",", "").strip()
amount = float(amount_text)


# ---------- ধাপ ৫: হিসাব ----------
unit_price = amount / quantity


# ---------- ধাপ ৬: সারাংশ ----------
print()
print(f"{order_id}  ·  {order_date}")
print(f"{customer_name} কিনেছেন {item_name} — {quantity}টা")
print(f"মোট ৳{amount:.2f}  (প্রতিটা ৳{unit_price:.2f})")
print(f"পেমেন্ট: {payment}  ·  অবস্থা: {status}")
print()


# ---------- প্রতিটা ঘরে কী type বসেছে ----------
print("type পরীক্ষা:")
print(f"  order_id   {type(order_id).__name__:<6} {order_id}")
print(f"  quantity   {type(quantity).__name__:<6} {quantity}")
print(f"  amount     {type(amount).__name__:<6} {amount}")
print(f"  unit_price {type(unit_price).__name__:<6} {unit_price}")
print()


# ---------- বোনাস: সতর্কবার্তা ----------
if status == "cancelled":
    print("সতর্কতা: এই অর্ডারটা বাতিল হয়েছে, হিসাবে ধরবেন না।")
    print()


# ---------- বোনাস: দ্বিতীয় record ----------
# খেয়াল করুন — নিচের কোডটা উপরেরটার হুবহু নকল, শুধু raw বদলেছে।
# একই জিনিস দুইবার লেখা মানে কোথাও একটা ভুল থেকে যাবে।
# পরের ক্লাসে loop শিখলে এই পুরো অংশটা তিন লাইনে নেমে আসবে।

raw2 = "ORD100046;2026-10-07;nusrat akter;Soybean Oil 2L;  1  ;৳350.00;nagad;delivered"

p = raw2.split(";")
oid    = p[0].strip().upper()
odate  = p[1].strip()
cname  = p[2].strip().title().replace("  ", " ")
iname  = p[3].strip()
qty    = int(p[4].strip())
amt    = float(p[5].strip().replace("৳", "").replace(",", ""))
pay    = p[6].strip().lower()
stat   = p[7].strip().lower()

print(f"{oid}  ·  {odate}")
print(f"{cname} কিনেছেন {iname} — {qty}টা")
print(f"মোট ৳{amt:.2f}  (প্রতিটা ৳{amt / qty:.2f})")
print(f"পেমেন্ট: {pay}  ·  অবস্থা: {stat}")
print()
