# Maintainer: Geir Damstuen
pkgname="dmenu-geir"
pkgver=5.0
pkgrel=1
pkgdesc="A generic menu for X"
url="https://github.com/geirda/dmenu-geir.git"
arch=('i686' 'x86_64')
license=('MIT')
depends=('libx11' 'libxinerama' 'libxft' 'freetype2' 'ttf-hack')
provides=(dmenu)
conflicts=(dmenu)
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
}
