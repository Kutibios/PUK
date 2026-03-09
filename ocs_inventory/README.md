# OCS Inventory NG Service

This repository contains the configuration to run the OCS Inventory NG server. It is deployed as a Docker container, with the environment managed by [Nix](https://nixos.org/) and deployment automated by [Taskfile](https://taskfile.dev/).

This server acts as the central collector for OCS agents and is designed to be linked with the [GLPI service](https://gitlab.basarsoft.com.tr/int.kutay.sezer/glpi/-/wikis/).

## Quick Start (Deployment)

**Prerequisites:**
* [Nix Package Manager](https://nixos.org/download.html) must be installed locally.
* Target server (`ocs01`) must be configured in your `~/.ssh/config`.

**1. Initialize Environment:**
Navigate to this repository's root directory (`ocs_inventory/`) and run `nix-shell` to load all required tools (`task`, `rsync`, `ssh`).
While inside the `nix-shell`, run the deploy task : `task deploy`

```bash
nix-shell