{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # Uygulama için gerekli olan temel paketler:
  # Python 3.11, paket yönetimi için Poetry ve otomasyon için Task (go-task)
  buildInputs = [
    pkgs.python311
    pkgs.poetry
    pkgs.go-task
  ];

  # Shell başlatıldığında çalıştırılacak ekstra komutlar
  shellHook = ''
    echo "=========================================================="
    echo "  PUK Core API - Geliştirme Ortamına (Nix-Shell) Hoş Geldiniz!"
    echo "  Python Versiyonu: $(python --version)"
    echo "  Poetry Versiyonu: $(poetry --version)"
    echo "  Mevcut komutları görmek için 'task --list' yazabilirsiniz."
    echo "=========================================================="
    
    # Poetry ortamının proje klasörünün içinde (.venv) oluşturulmasını sağlar
    export POETRY_VIRTUALENVS_IN_PROJECT=true
  '';
}
