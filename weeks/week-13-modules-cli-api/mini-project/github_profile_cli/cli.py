"""Command-line interface for looking up a public GitHub profile."""

import argparse
import json

from github_profile_cli.client import GitHubAPIError, get_user


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Look up a public GitHub profile using the GitHub API."
    )
    parser.add_argument("username", help="GitHub username, for example: octocat")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the complete API response as formatted JSON.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        user = get_user(args.username)
    except (GitHubAPIError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    if args.json:
        print(json.dumps(user, indent=2, ensure_ascii=False))
        return 0

    print(f"Username: {user.get('login', 'N/A')}")
    print(f"Name: {user.get('name') or 'Not provided'}")
    print(f"Public repositories: {user.get('public_repos', 0)}")
    print(f"Followers: {user.get('followers', 0)}")
    print(f"Following: {user.get('following', 0)}")
    print(f"Profile: {user.get('html_url', 'N/A')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
