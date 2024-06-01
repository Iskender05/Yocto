SUMMARY = "Hello for Yadro"
DESCRIPTION = "Hello World Program write in C by Iskender"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

python do_display_banner() {
    bb.plain("***********************************************");
    bb.plain("*                                             *");
    bb.plain("*               Hello World Yadro             *");
    bb.plain("*                                             *");
    bb.plain("***********************************************");
}

SRC_URI = "file://hello.c"

S = "${WORKDIR}/build"

addtask display_banner before do_build

do_compile() {
	${CC} ${CFLAGS} ${LDFLAGS} ${WORKDIR}/hello.c -o ${S}/hello
}

do_install() {
	install -d ${D}${bindir}
	install -m 0755 ${S}/hello ${D}${bindir}/
}
