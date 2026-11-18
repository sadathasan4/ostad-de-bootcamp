#!/usr/bin/env python3
"""
doctor.py — Ostad Data Engineering Bootcamp
আপনার সেটআপ ঠিক আছে কি না, সেটা এক কমান্ডে বলে দেয়।

চালানোর নিয়ম:   python3 setup/doctor.py
শেষের SUMMARY লাইনটা কপি করে ক্লাসের চ্যাটে পেস্ট করুন।

এই ফাইলটা শুধু Python-এর standard library ব্যবহার করে, তাই
কিছু ইনস্টল না করেও চলবে।
"""

import os
import platform
import shutil
import subprocess
import sys

OK, WARN, FAIL = "OK", "WARN", "FAIL"
RESULTS = []

GREEN, YELLOW, RED, GREY, BOLD, OFF = (
    ("\033[32m", "\033[33m", "\033[31m", "\033[90m", "\033[1m", "\033[0m")
    if sys.stdout.isatty() and os.environ.get("TERM") not in (None, "dumb")
    else ("", "", "", "", "", "")
)
MARK = {OK: GREEN + "[  OK  ]" + OFF, WARN: YELLOW + "[ WARN ]" + OFF, RED: "", FAIL: RED + "[ FAIL ]" + OFF}


def record(status, title, detail="", fix=""):
    RESULTS.append((status, title, detail, fix))
    print("{} {:<34} {}".format(MARK[status], title, GREY + detail + OFF if detail else ""))
    if fix and status != OK:
        print("         {}→ {}{}".format(YELLOW, fix, OFF))


def run(cmd):
    """একটা কমান্ড চালিয়ে তার আউটপুট ফেরত দেয়। না চললে None।"""
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=12)
        if out.returncode == 0:
            return (out.stdout + out.stderr).strip()
    except Exception:
        pass
    return None


def first_line(text):
    return text.splitlines()[0].strip() if text else ""


# ---------------------------------------------------------------- platform
def detect_platform():
    sysname = platform.system()
    if sysname == "Linux":
        release = platform.release().lower()
        is_wsl = "microsoft" in release or "wsl" in release
        distro = ""
        try:
            with open("/etc/os-release") as fh:
                for line in fh:
                    if line.startswith("PRETTY_NAME="):
                        distro = line.split("=", 1)[1].strip().strip('"')
                        break
        except OSError:
            pass
        if is_wsl:
            return "wsl", "WSL · " + (distro or "Linux")
        return "linux", distro or "Linux"
    if sysname == "Darwin":
        return "mac", "macOS " + platform.mac_ver()[0]
    if sysname == "Windows":
        return "windows", "Windows (WSL-এর বাইরে)"
    return "other", sysname


def check_platform():
    kind, label = detect_platform()
    if kind == "wsl":
        record(OK, "কোথায় চলছে", label)
    elif kind in ("linux", "mac"):
        record(OK, "কোথায় চলছে", label)
    elif kind == "windows":
        record(
            FAIL,
            "কোথায় চলছে",
            label,
            "Windows PowerShell/CMD না — WSL-এর ভেতরে চালাতে হবে। "
            "Start menu-তে 'Ubuntu' লিখে টার্মিনাল খুলুন, তারপর আবার চালান।",
        )
    else:
        record(WARN, "কোথায় চলছে", label, "অচেনা সিস্টেম — ক্লাসে জানাবেন।")
    return kind


# ---------------------------------------------------------------- python
def check_python():
    v = sys.version_info
    ver = "{}.{}.{}".format(v.major, v.minor, v.micro)
    if v[:2] >= (3, 10):
        record(OK, "Python", ver)
    elif v[:2] >= (3, 8):
        record(WARN, "Python", ver, "চলবে, তবে 3.10+ হলে ভালো। পরে আপডেট করে নেবেন।")
    else:
        record(FAIL, "Python", ver, "3.10 বা তার পরের ভার্সন দরকার। setup.sh চালান।")
    return ver


def check_pip():
    out = run([sys.executable, "-m", "pip", "--version"])
    if out:
        record(OK, "pip", first_line(out).split(" from ")[0])
    else:
        record(FAIL, "pip", "পাওয়া যায়নি",
               "sudo apt install -y python3-pip   (WSL/Linux) চালান")


def check_venv():
    try:
        import venv  # noqa: F401
        record(OK, "venv module", "আছে")
    except ImportError:
        record(FAIL, "venv module", "নেই",
               "sudo apt install -y python3-venv   চালান")


def check_virtualenv_active():
    active = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    if active:
        record(OK, "virtual environment", os.path.basename(sys.prefix) + " চালু আছে")
    else:
        record(WARN, "virtual environment", "চালু নেই",
               "source .venv/bin/activate   — ক্লাস ১-এর পরে এটা লাগবে, এখন না হলেও চলবে")


# ---------------------------------------------------------------- tools
def check_git():
    path = shutil.which("git")
    if not path:
        record(FAIL, "git", "নেই", "sudo apt install -y git   চালান")
        return ""
    ver = first_line(run(["git", "--version"]) or "").replace("git version ", "")
    record(OK, "git", ver)

    name = run(["git", "config", "--global", "user.name"])
    email = run(["git", "config", "--global", "user.email"])
    if name and email:
        record(OK, "git পরিচয়", "{} <{}>".format(first_line(name), first_line(email)))
    else:
        record(WARN, "git পরিচয়", "দেওয়া নেই",
               'git config --global user.name "আপনার নাম" '
               '&& git config --global user.email "আপনার@ইমেইল" — মডিউল ২-তে লাগবে')
    return ver


def check_vscode():
    if shutil.which("code"):
        record(OK, "VS Code (code কমান্ড)", "আছে")
    else:
        record(WARN, "VS Code (code কমান্ড)", "টার্মিনাল থেকে পাওয়া যাচ্ছে না",
               "VS Code খুলে Remote-WSL extension বসান। এটা না থাকলেও ক্লাস করা যাবে।")


# ---------------------------------------------------------------- workspace
def check_workspace():
    here = os.getcwd()
    if "/mnt/c/" in here.replace("\\", "/"):
        record(WARN, "কাজের ফোল্ডার", here,
               "Windows ড্রাইভের ভেতরে কাজ করলে সব ধীর চলবে। "
               "ফাইলগুলো WSL-এর নিজের ফোল্ডারে নিন: cd ~ && mkdir -p de-bootcamp")
    else:
        record(OK, "কাজের ফোল্ডার", here)

    try:
        probe = os.path.join(here, ".doctor_write_test")
        with open(probe, "w") as fh:
            fh.write("ok")
        os.remove(probe)
        record(OK, "ফোল্ডারে লেখার অনুমতি", "আছে")
    except OSError as exc:
        record(FAIL, "ফোল্ডারে লেখার অনুমতি", str(exc),
               "অন্য একটা ফোল্ডারে গিয়ে চালান: cd ~ && mkdir -p de-bootcamp && cd de-bootcamp")


def check_course_data():
    candidates = [
        os.path.join("module-01", "data", "orders_oct2026.csv"),
        os.path.join("..", "module-01", "data", "orders_oct2026.csv"),
        os.path.join("data", "orders_oct2026.csv"),
    ]
    for rel in candidates:
        if os.path.exists(rel):
            size = os.path.getsize(rel) / (1024 * 1024)
            record(OK, "কোর্সের data ফাইল", "{} ({:.1f} MB)".format(os.path.normpath(rel), size))
            return
    record(WARN, "কোর্সের data ফাইল", "এখনো পাওয়া যায়নি",
           "repo-র ভেতরে ঢুকে চালাচ্ছেন কি না দেখুন। না থাকলে ক্লাসে নামিয়ে নেবেন।")


def check_optional_packages():
    missing = []
    for pkg in ("pandas", "requests"):
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if not missing:
        record(OK, "pandas, requests", "বসানো আছে")
    else:
        record(WARN, "pandas, requests", "নেই: " + ", ".join(missing),
               "pip install " + " ".join(missing) + "   — সপ্তাহ ৭ থেকে লাগবে, এখন না হলেও চলবে")


def check_internet():
    try:
        import socket
        socket.setdefaulttimeout(4)
        socket.create_connection(("pypi.org", 443)).close()
        record(OK, "ইন্টারনেট", "ঠিক আছে")
    except Exception:
        record(WARN, "ইন্টারনেট", "pypi.org-এ পৌঁছানো গেলো না",
               "এখন অফলাইন থাকলে সমস্যা নেই। পরে প্যাকেজ বসানোর সময় লাগবে।")


# ---------------------------------------------------------------- main
def main():
    print()
    print(BOLD + "  Ostad · Data Engineering Bootcamp — সেটআপ পরীক্ষা" + OFF)
    print("  " + GREY + "-" * 56 + OFF)
    print()

    kind = check_platform()
    ver = check_python()
    check_pip()
    check_venv()
    check_virtualenv_active()
    git_ver = check_git()
    check_vscode()
    check_workspace()
    check_course_data()
    check_optional_packages()
    check_internet()

    fails = [r for r in RESULTS if r[0] == FAIL]
    warns = [r for r in RESULTS if r[0] == WARN]
    oks = [r for r in RESULTS if r[0] == OK]

    print()
    print("  " + GREY + "-" * 56 + OFF)
    if not fails and not warns:
        print(GREEN + BOLD + "  সব ঠিক আছে। ক্লাসের জন্য আপনি তৈরি।" + OFF)
    elif not fails:
        print(YELLOW + BOLD + "  বড় কোনো সমস্যা নেই। উপরের হলুদ লাইনগুলো পরে দেখলেই হবে।" + OFF)
    else:
        print(RED + BOLD + "  {}টা জিনিস ঠিক করতে হবে।".format(len(fails)) + OFF)
        print("  উপরের তীর চিহ্নের লাইনগুলো এক এক করে চালান, তারপর আবার doctor চালান।")

    summary = "SUMMARY: {} OK, {} WARN, {} FAIL | py{} | {} | git{}".format(
        len(oks), len(warns), len(fails), ver, kind, git_ver or "none")
    print()
    print("  নিচের লাইনটা কপি করে ক্লাসের চ্যাটে পেস্ট করুন:")
    print("  " + BOLD + summary + OFF)
    print()
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
