from __future__ import annotations

from pathlib import Path
from urllib.request import Request, urlopen


UPSTREAM = (
    "https://raw.githubusercontent.com/fmz200/wool_scripts/"
    "main/Shadowrocket/module/blockAds.srmodule"
)
OUTPUT = Path(__file__).resolve().parents[1] / "dist" / "Shadowrocket_CN_Apps_AdBlock_730.srmodule"
SELF_RAW = (
    "https://raw.githubusercontent.com/haokun-1/shadowrocket-rules/"
    "main/dist/Shadowrocket_CN_Apps_AdBlock_730.srmodule"
)


def download(url: str) -> str:
    request = Request(url, headers={"User-Agent": "shadowrocket-rule-updater/1.0"})
    with urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8-sig")


def sanitize(source: str) -> str:
    result: list[str] = []
    for line in source.splitlines():
        lowered = line.lower()

        # Keep this distribution focused on ad blocking, not account or entitlement changes.
        if "spotify" in lowered and not line.startswith("hostname ="):
            continue
        if any(
            marker in lowered
            for marker in (
                ".vip_type = 2",
                ".data.vip |=",
                "due_date: 9005270400000",
                "spotify.crack",
            )
        ):
            continue
        if line.startswith("#!raw-url="):
            continue

        if line.startswith("hostname ="):
            prefix, values = line.split("=", 1)
            hosts = [host.strip() for host in values.split(",")]
            hosts = [host for host in hosts if "spotify" not in host.lower()]
            line = f"{prefix}= " + ", ".join(hosts)
        elif line.startswith("#!name="):
            line = "#!name=国内应用广告拦截与净化（约730款）"
        elif line.startswith("#!desc="):
            line = "#!desc=自动同步上游；已移除会员状态修改和非广告破解条目"

        result.append(line)

    insert_at = next(
        (index + 1 for index, line in enumerate(result) if line.startswith("#!desc=")),
        1,
    )
    result.insert(insert_at, f"#!raw-url={SELF_RAW}")

    return "\n".join(result).rstrip() + "\n"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(sanitize(download(UPSTREAM)), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
