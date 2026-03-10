{
  description = "Development Environment for OCS and Monitoring Projects";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          name = "devops-shell";
          
          packages = with pkgs; [
            go-task 
            
            rsync
            
            openssh
            
            docker-compose
          ];

        };
      }
    );
}
