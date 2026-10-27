from __future__ import annotations

import argparse

import requests

from .checks import check_repository, parse_repo


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="oss-repo-check",
        description="Check whether a GitHub repository exposes common contributor onboarding files.",
    )
    parser.add_argument("repository", help="GitHub URL or owner/repository")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        owner, repo = parse_repo(args.repository)
        results = check_repository(owner, repo)
    except ValueError as exc:
        print(f"Input error: {exc}")
        return 2
    except requests.RequestException as exc:
        print(f"GitHub API error: {exc}")
        return 1

    print(f"Repository: {owner}/{repo}")
    for result in results:
        status = "OK" if result.found else "MISSING"
        print(f"{result.name:<24} {status}")

    score = sum(result.found for result in results)
    print(f"\nScore: {score}/{len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
