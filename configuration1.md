echo "[INFO] Membuat folder-folder konfigurasi..."
mkdir -p ~/.config/hypr
mkdir -p ~/.config/waybar

echo "[INFO] Mengunduh file hyprland.conf dari Gist..."
curl -sL https://gist.githubusercontent.com/GoogleCloudPlatform/51834c26d1783307590d2382436f6d54/raw > ~/.config/hypr/hyprland.conf

echo "[INFO] Menyalin konfigurasi default untuk Waybar..."
cp /etc/xdg/waybar/config.jsonc ~/.config/waybar/
cp /etc/xdg/waybar/style.css ~/.config/waybar/

echo "[INFO] Mengaktifkan layanan audio untuk user Anda..."
systemctl --user enable --now pipewire.service pipewire.socket pipewire-pulse.service wireplumber.service

echo ""
echo "=========================================================="
echo "  SETUP SELESAI! SEMUA KONFIGURASI SUDAH SIAP."
echo "  Ketik 'Hyprland' (dengan H besar) lalu Enter."
echo "=========================================================="
echo ""
