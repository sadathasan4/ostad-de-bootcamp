#!/usr/bin/env bash
# setup.sh — Ostad Data Engineering Bootcamp
# WSL (Ubuntu), Linux বা macOS-এ কাজের পরিবেশ তৈরি করে দেয়।
#
# চালানোর নিয়ম:   bash setup/setup.sh
#
# একই স্ক্রিপ্ট বারবার চালানো যায় — যা আগে থেকে বসানো আছে, সেটা আবার বসাবে না।

set -u

GREEN=$'\033[32m'; YELLOW=$'\033[33m'; RED=$'\033[31m'; BOLD=$'\033[1m'; OFF=$'\033[0m'
say()  { printf '%s\n' "$*"; }
step() { printf '\n%s==> %s%s\n' "$BOLD" "$*" "$OFF"; }
ok()   { printf '%s  ok%s  %s\n' "$GREEN" "$OFF" "$*"; }
warn() { printf '%s  !! %s  %s\n' "$YELLOW" "$OFF" "$*"; }
die()  { printf '%s  xx %s  %s\n' "$RED" "$OFF" "$*"; exit 1; }

say ""
say "${BOLD}  Ostad · Data Engineering Bootcamp — সেটআপ${OFF}"
say "  ------------------------------------------------"

# ---------------------------------------------------------------- 1. কোথায় চলছি
step "১/৫  সিস্টেম দেখছি"

OS="$(uname -s)"
case "$OS" in
  Linux)
    if grep -qiE "microsoft|wsl" /proc/version 2>/dev/null; then
      PLATFORM="wsl";   ok "WSL-এর ভেতরে চলছি — ঠিক জায়গা"
    else
      PLATFORM="linux"; ok "Linux"
    fi
    ;;
  Darwin) PLATFORM="mac"; ok "macOS" ;;
  *) die "অচেনা সিস্টেম ($OS)। Windows হলে PowerShell না — Ubuntu টার্মিনাল খুলে চালান।" ;;
esac

if [ "$PLATFORM" = "wsl" ] || [ "$PLATFORM" = "linux" ]; then
  case "$PWD" in
    /mnt/c/*|/mnt/d/*|/mnt/e/*)
      warn "আপনি Windows ড্রাইভের ভেতরে আছেন ($PWD)"
      warn "এখানে সব ধীরে চলবে। পরে ফাইলগুলো ~/de-bootcamp-এ সরিয়ে নিন।"
      ;;
  esac
fi

# ---------------------------------------------------------------- 2. প্যাকেজ
step "২/৫  দরকারি প্যাকেজ বসাচ্ছি"

if [ "$PLATFORM" = "mac" ]; then
  if command -v brew >/dev/null 2>&1; then
    brew list git >/dev/null 2>&1 || brew install git
    command -v python3 >/dev/null 2>&1 || brew install python
    ok "Homebrew দিয়ে git আর python দেখা হলো"
  else
    warn "Homebrew নেই। macOS-এ আগে Homebrew বসান: https://brew.sh"
    warn "তারপর এই স্ক্রিপ্টটা আবার চালান।"
  fi
else
  if ! command -v apt-get >/dev/null 2>&1; then
    warn "apt-get পাওয়া গেলো না — নিজের ডিস্ট্রোর প্যাকেজ ম্যানেজার দিয়ে"
    warn "python3, python3-pip, python3-venv আর git বসিয়ে নিন।"
  else
    say "  (sudo-র পাসওয়ার্ড চাইতে পারে — এটা আপনার WSL-এর পাসওয়ার্ড)"
    sudo apt-get update -qq || warn "apt update-এ সমস্যা হলো, তবু এগোচ্ছি"
    sudo apt-get install -y -qq python3 python3-pip python3-venv git curl unzip \
      && ok "python3, pip, venv, git, curl, unzip — সব বসানো হলো" \
      || die "প্যাকেজ বসাতে সমস্যা হলো। উপরের লেখাটা ক্লাসের চ্যাটে পাঠান।"
  fi
fi

# ---------------------------------------------------------------- 3. venv
step "৩/৫  প্রজেক্টের নিজের Python পরিবেশ (.venv) তৈরি করছি"

if [ -d ".venv" ]; then
  ok ".venv আগে থেকেই আছে"
else
  python3 -m venv .venv && ok ".venv তৈরি হলো" || die ".venv তৈরি করা গেলো না"
fi

# shellcheck disable=SC1091
. .venv/bin/activate || die ".venv চালু করা গেলো না"
ok "এখন .venv চালু আছে"

# ---------------------------------------------------------------- 4. লাইব্রেরি
step "৪/৫  কয়েকটা লাইব্রেরি বসাচ্ছি"

python -m pip install --quiet --upgrade pip
if [ -f "requirements.txt" ]; then
  python -m pip install --quiet -r requirements.txt && ok "requirements.txt থেকে বসানো হলো"
else
  python -m pip install --quiet pandas requests && ok "pandas, requests বসানো হলো"
fi

# ---------------------------------------------------------------- 5. git পরিচয়
step "৫/৫  git-এর পরিচয় দেখছি"

GIT_NAME="$(git config --global user.name  2>/dev/null || true)"
GIT_MAIL="$(git config --global user.email 2>/dev/null || true)"
if [ -n "$GIT_NAME" ] && [ -n "$GIT_MAIL" ]; then
  ok "git পরিচয় দেওয়া আছে: $GIT_NAME <$GIT_MAIL>"
else
  warn "git-এ এখনো নাম-ইমেইল দেওয়া নেই। মডিউল ২-তে লাগবে। তখন এই দুইটা চালাবেন:"
  say  "      git config --global user.name  \"আপনার নাম\""
  say  "      git config --global user.email \"আপনার@ইমেইল\""
fi

# ---------------------------------------------------------------- শেষ
say ""
say "  ------------------------------------------------"
say "${GREEN}${BOLD}  সেটআপ শেষ।${OFF}"
say ""
say "  এখন এটা চালিয়ে দেখুন সব ঠিক আছে কি না:"
say "      ${BOLD}python3 setup/doctor.py${OFF}"
say ""
say "  পরের বার টার্মিনাল খুললে .venv চালু করতে ভুলবেন না:"
say "      ${BOLD}source .venv/bin/activate${OFF}"
say ""
