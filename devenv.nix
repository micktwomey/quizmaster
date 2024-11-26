{ pkgs, lib, config, inputs, ... }:

let
  pkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
in
{
  packages = [ pkgs.git ];

  languages.python = {
    enable = true;
    uv.enable = true;
    uv.package = pkgs-unstable.uv;
    uv.sync.enable = true;
    venv.enable = true;
  };

}
