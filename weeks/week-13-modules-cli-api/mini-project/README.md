# Mini-project — GitHub Profile CLI

Build a small Python command-line application that reads a public GitHub
profile through the official GitHub Users API.

## What you practise

- **Modules and packages:** separate the HTTP client from the CLI.
- **Dependencies:** use Python's standard library; no third-party package needed.
- **CLI:** parse a username and an optional `--json` flag with `argparse`.
- **HTTP/API:** send a GET request, set headers, and decode JSON.
- **Error handling:** handle missing users, HTTP errors, invalid JSON and network
  failures. Every request has a timeout.

## Run on Windows, macOS or Linux

From the repository root:

```bash
python weeks/week-13-modules-cli-api/mini-project/github_profile_cli/cli.py octocat
```

Print the complete JSON response:

```bash
python weeks/week-13-modules-cli-api/mini-project/github_profile_cli/cli.py octocat --json
```

The first command needs an internet connection. Tests use mocked HTTP responses,
so the automated test suite does not depend on GitHub being reachable.

## Design

```text
cli.py  ->  client.py  ->  GitHub Users API
 argparse     urllib       JSON response
```

The CLI handles user input and presentation. The client owns HTTP details.
This separation makes the API client easier to test and reuse.
