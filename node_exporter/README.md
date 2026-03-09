# Node Exporter Service

This repository contains the configuration to run the Prometheus Node Exporter. It is deployed as a Docker container, with the environment managed by [Nix](https://nixos.org/) and deployment automated by [Taskfile](https://taskfile.dev/).

Its purpose is to collect hardware and OS metrics from the host server for Prometheus to scrape.

## 🚀 Quick Start (Deployment)

**Prerequisites:**
* [Nix Package Manager](https://nixos.org/download.html) must be installed locally.
* Target server (`ocs01`) must be configured in your `~/.ssh/config`.

**1. Initialize Environment:**
Navigate to this repository's root directory (`node_exporter/`) and run `nix-shell` to load all required tools (`task`, `rsync`, `ssh`).
While inside the `nix-shell`, run the deploy task : `task deploy`

```bash
nix-shell