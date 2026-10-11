# -*- coding: utf-8 -*-
"""ゲームのプライバシーポリシーに Google Analytics for Firebase の節を追加する(冪等)。
usage: python tools/add_firebase_analytics_privacy.py samurairogue/privacy/index.html yokaimahjong/privacy/index.html
"""
import re
import sys

REV_JA = "改定日：2026年10月11日"
REV_EN = "Last updated: October 11, 2026"

JA = """  <h2>3. 利用状況の分析（Google Analytics for Firebase）</h2>
  <p>どのくらいの方が続けて遊んでいるか（継続率）やゲームの進み具合を把握して本アプリを改善するために、Google LLC の Google Analytics for Firebase を利用します。これにより、次の情報が Google へ送られます。</p>
  <ul>
    <li>利用状況：アプリの初回起動と起動、利用時間、ゲームの開始と終了（到達した段階・経過時間・結果）、広告が表示された回数</li>
    <li>端末の情報：機種、OS、言語、国や地域（IP アドレスから推定）</li>
    <li>端末の識別子：アプリインスタンス ID（本アプリのインストールごとに振られる識別子）。端末の設定で許可されている場合は広告 ID が含まれることがあります</li>
  </ul>
  <p>氏名や連絡先など、個人を特定する情報は送りません。当方が見るのは集計された統計で、特定の個人を識別する目的には使いません。取り扱いは Google の方針に従います（Google のプライバシーポリシー：<a href="https://policies.google.com/privacy">https://policies.google.com/privacy</a>）。本アプリをアンインストールすると、以後の送信は止まります。</p>

"""

EN = """    <li><strong>Usage analytics.</strong> To understand how many players keep playing (retention) and how far they get, the App uses Google Analytics for Firebase (Google LLC). It sends Google usage data (first open and app opens, time in app, game start and end with the stage reached, elapsed time and result, and how many ads were shown), device information (model, OS, language, country/region estimated from the IP address) and the app instance ID (an identifier assigned to each installation of the App); the Advertising ID may be included where your device settings allow it. No name, contact details or other information that directly identifies you is sent. We only look at aggregated statistics and do not use them to identify individuals. Google handles the data under its own policy (<a href="https://policies.google.com/privacy">https://policies.google.com/privacy</a>). Uninstalling the App stops further sending.</li>
"""


def patch(path):
    s = open(path, encoding="utf-8").read()
    if "Google Analytics for Firebase" in s:
        print("SKIP(already)", path)
        return
    # 3〜8 を 4〜9 へ繰り下げ(後ろから)
    for n in range(8, 2, -1):
        s = s.replace("<h2>%d. " % n, "<h2>%d. " % (n + 1), 1)
    s = s.replace("  <h2>4. 広告について</h2>", JA + "  <h2>4. 広告について</h2>", 1)
    s = s.replace("当方は利用者の情報を受け取らないため、当方が利用者の情報を第三者へ提供することはありません。広告サービスが取得する情報は、上記 3 のとおりです。",
                  "当方が受け取るのは上記 3 の集計された利用状況だけで、これを第三者へ販売・提供することはありません。広告サービスが取得する情報は、上記 4 のとおりです。", 1)
    s = s.replace("<p class=\"meta\">制定日：2026年10月10日</p>", "<p class=\"meta\">制定日：2026年10月10日　" + REV_JA + "</p>", 1)
    s = s.replace("<p class=\"meta\">Effective: October 10, 2026</p>", "<p class=\"meta\">Effective: October 10, 2026 / " + REV_EN + "</p>", 1)
    i = s.index("    <li><strong>Ads.</strong>")
    s = s[:i] + EN + s[i:]
    checks = [JA.strip()[:40] in s, "Usage analytics" in s, REV_JA in s, REV_EN in s, "上記 4 のとおり" in s,
              len(re.findall(r"<h2>\d\. ", s)) == 9]
    if not all(checks):
        raise SystemExit("CHECK_FAIL %s %s" % (path, checks))
    open(path, "w", encoding="utf-8", newline="\n").write(s)
    print("PATCHED", path, checks)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        patch(p)
