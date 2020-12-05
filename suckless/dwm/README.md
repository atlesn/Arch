# dwm 6.2

See also: https://github.com/geirda/dwm-geir.git

Patches included:

* attachbelow
* autostart
* centeredmaster
* gaplessgrid
* layoutmenu
* pertag
* resetnmaster
* rotatestack
* ru_gaps
* status2d
* statuspadding
* swallow
* switchtotag
* titlecolor

This build of dwm uses the following two fonts:

* extra/ttf-hack
* aur/nerd-fonts-roboto-mono

Please note that RobotoMono Nerd Font must be installed manually, e.g.:

	$ yay -S nerd-fonts-roboto-mono

To get a layouts menu when rightclicking the layouts-icon, please install xmenu:

	$ yay -S xmenu

## Installation (choose one of the methods):

### From precompiled binary:

	$ wget https://github.com/geirda/Arch/raw/master/suckless/dwm/dwm-geir-6.2-5-x86_64.pkg.tar.zst
	$ sudo pacman -U dwm-geir-6.2-5-x86_64.pkg.tar.zst

### From PKGBUILD:

	$ wget https://raw.githubusercontent.com/geirda/Arch/master/suckless/dwm/PKGBUILD
	$ makepkg -ci


![suckless](https://raw.githubusercontent.com/geirda/Arch/master/suckless/suckless.png)
