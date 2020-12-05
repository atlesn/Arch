# st 0.8.4

See also: https://github.com/geirda/st-geir.git

Patches included:

* alphaFocusHighlight
* scrollback
* scrollback-mouse
* scrollback-mouse-altscreen

This build of st uses the following two fonts:

* aur/nerd-fonts-hack
* extra/ttf-hack

Please note that Hack Nerd Font must be installed manually. This is optional though, as st will use Hack Font as the fallback. To install Hack Nerd Font:

	$ yay -S nerd-fonts-hack

## Installation (choose one of the methods):

### From precompiled binary:

	$ wget https://github.com/geirda/Arch/raw/master/suckless/st/st-geir-0.8.4-2-x86_64.pkg.tar.zst
	$ sudo pacman -U st-geir-0.8.4-2-x86_64.pkg.tar.zst

### From PKGBUILD:

	$ wget https://raw.githubusercontent.com/geirda/Arch/master/suckless/st/PKGBUILD
	$ makepkg -ci


![suckless](https://raw.githubusercontent.com/geirda/Arch/master/suckless/suckless.png)
