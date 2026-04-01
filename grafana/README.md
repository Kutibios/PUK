# Grafana & Prometheus Monitoring Stack

This repository contains the configuration to run the Grafana & Prometheus monitoring stack. It is deployed as a Docker container, with the environment managed by [Nix](https://nixos.org/) and deployment automated by [Taskfile](https://taskfile.dev/).

This stack is intended to scrape metrics from services like `node_exporter`.

##  Quick Start (Deployment)

**Prerequisites:**
* [Nix Package Manager](https://nixos.org/download.html) must be installed locally.
* Target server must be configured in your `~/.ssh/config`.

**1. Initialize Environment:**
Navigate to this repository's root directory and run `nix-shell` to load all required tools (`task`, `rsync`, `ssh`).
While inside the `nix-shell`, run the deploy task : `task deploy`
```bash
nix-shell