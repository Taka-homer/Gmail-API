"""指定した宛先・件名・本文を入れた Gmail の作成画面を開く。

送信はプログラムでは行わない。開いた画面の「送信」ボタンを押す。
"""

import argparse
import urllib.parse
import webbrowser

# ここを書き換えるか、実行時に --to で指定する。
TO_ADDRESS = "recipient@example.com"
SUBJECT = "Gmail テスト送信"
BODY = "これは Gmail の作成画面から送るテストメールです。"

COMPOSE_URL = "https://mail.google.com/mail/"


def build_compose_url(to: str, subject: str, body: str) -> str:
    """Gmail の新規メール画面を開く URL を作る。"""
    query = urllib.parse.urlencode(
        {
            "view": "cm",
            "fs": "1",
            "to": to,
            "su": subject,
            "body": body,
        }
    )
    return f"{COMPOSE_URL}?{query}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gmail の作成画面を開き、画面上の送信ボタンで送る"
    )
    parser.add_argument("--to", default=TO_ADDRESS, help="宛先メールアドレス")
    parser.add_argument("--subject", default=SUBJECT, help="件名")
    parser.add_argument("--body", default=BODY, help="本文")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.to == "recipient@example.com" or "@" not in args.to:
        raise SystemExit(
            "宛先を指定してください。\n"
            "send_mail.py の TO_ADDRESS を書き換えるか、次のように実行します。\n"
            '  python send_mail.py --to "you@example.com"'
        )

    url = build_compose_url(args.to, args.subject, args.body)
    opened = webbrowser.open(url)
    if not opened:
        raise SystemExit(f"ブラウザを開けませんでした。次の URL を開いてください。\n{url}")

    print("Gmail の作成画面を開きました。内容を確認して「送信」を押してください。")
    print(f"宛先: {args.to}")
    print(f"件名: {args.subject}")


if __name__ == "__main__":
    main()
