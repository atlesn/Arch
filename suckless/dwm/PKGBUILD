# Maintainer: Geir Damstuen
pkgname="dwm-geir"
pkgver=6.2
pkgrel=5
pkgdesc="A dynamic window manager for X"
url="https://github.com/geirda/dwm-geir.git"
arch=('i686' 'x86_64')
license=('MIT')
depends=('libx11' 'libxinerama' 'libxft' 'freetype2' 'ttf-hack')
optdepends=(nerd-fonts-roboto-mono)
provides=(dwm)
conflicts=(dwm)
source=("git+$url")
md5sums=('SKIP')

prepare() {
	cd "$srcdir/$pkgname"
}

build() {
	cd "$srcdir/$pkgname"
	make
}

package() {
	cd "$srcdir/$pkgname"
	make PREFIX=/usr DESTDIR="$pkgdir" install
	install -Dm644 "${srcdir}/${pkgname}/dwm-geir.desktop" "$pkgdir/usr/share/xsessions/dwm-geir.desktop"
	install -Dm755 "${srcdir}/${pkgname}/dwmupdate.sh" "$pkgdir/usr/bin/dwmupdate.sh"
	install -Dm755 "${srcdir}/${pkgname}/dwmlayoutmenu.sh" "$pkgdir/usr/bin/dwmlayoutmenu.sh"
}
