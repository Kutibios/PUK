# shell.nix
let
  # Use your local nixpkgs (or pin with fetchTarball if you want reproducibility)
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  buildInputs = with pkgs; [
    # openssh
    ansible
    docker-compose
    go-task
    rsync
    sshpass
  ];

}
 