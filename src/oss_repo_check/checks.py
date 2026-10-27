from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import requests


@dataclass(frozen=True)
class CheckResult:
    name: str
    found: bool
    matched_path: str | None = None


CHECKS: dict[str, tuple[str, ...]] = {
    "README": ("README.md", "README.rst", "README.txt", "README"),
    "CONTRIBUTING": ("CONTRIBUTING.md", ".github/CONTRIBUTING.md"),
    "CODE_OF_CONDUCT": ("CODE_OF_CONDUCT.md", ".github/CODE_OF_CONDUCT.md"),
    "LICENSE": ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"),
    "ISSUE_TEMPLATE": (".github/ISSUE_TEMPLATE/config.yml", ".github/ISSUE_TEMPLATE/bug_report.md"),
    "PULL_REQUEST_TEMPLATE": (".github/PULL_REQUEST_TEMPLATE.md", "PULL_REQUEST_TEMPLATE.md"),
}


def parse_repo(value: str) -> tuple[str, str]:
    """Parse a GitHub URL or owner/repository string."""
    value = value.strip().removesuffix("/")
    if value.startswith("https://github.com/"):
        value = value.removeprefix("https://github.com/")
    elif value.startswith("http://github.com/"):
        value = value.removeprefix("http://github.com/")

    parts = value.split("/")
    if len(parts) != 2 or not all(parts):
        raise ValueError("Repository must be 'owner/repository' or a GitHub repository URL.")
    return parts[0], parts[1]


def _path_exists(owner: str, repo: str, path: str, timeout: float = 8.0) -> bool:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url, timeout=timeout, headers={"Accept": "application/vnd.github+json"})
    if response.status_code == 200:
        return True
    if response.status_code == 404:
        return False
    response.raise_for_status()
    return False


def check_repository(owner: str, repo: str, checks: dict[str, Iterable[str]] | None = None) -> list[CheckResult]:
    """Run contribution-readiness checks against a public GitHub repository."""
    selected = checks or CHECKS
    results: list[CheckResult] = []

    for name, paths in selected.items():
        matched: str | None = None
        for path in paths:
            if _path_exists(owner, repo, path):
                matched = path
                break
        results.append(CheckResult(name=name, found=matched is not None, matched_path=matched))

    return results
