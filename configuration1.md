# Monitor
monitor=,preferred,auto,1

# Autostart
exec-once = waybar & dunst
exec-once = /usr/lib/polkit-kde-authentication-agent-1

# Variabel utama
$mainMod = SUPER
$terminal = kitty
$menu = wofi --show drun

# Keybindings dasar
bind = $mainMod, Q, exec, $terminal
bind = $mainMod, C, killactive, 
bind = $mainMod, M, exit, 
bind = $mainMod, D, exec, $menu
bind = $mainMod, E, exec, dolphin
bind = $mainMod, F, fullscreen
bind = $mainMod, SPACE, togglefloating, 

# Pindah window
bind = $mainMod, left, movefocus, l
bind = $mainMod, right, movefocus, r
bind = $mainMod, up, movefocus, u
bind = $mainMod, down, movefocus, d

# Pindah workspace
bind = $mainMod, 1, workspace, 1
bind = $main_mod, 2, workspace, 2
bind = $main_mod, 3, workspace, 3

# Pindahkan window ke workspace
bind = $mainMod SHIFT, 1, movetoworkspace, 1
bind = $mainMod SHIFT, 2, movetoworkspace, 2
bind = $mainMod SHIFT, 3, movetoworkspace, 3
