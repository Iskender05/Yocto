FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y sudo kmod php apache2 curl openvpn zip unzip bridge-utils vim gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 python3-subunit zstd liblz4-tool file locales libacl1

RUN echo 'root:root' | chpasswd
RUN locale-gen en_US.UTF-8

ARG USER_NAME=user

SHELL ["/bin/bash","-c"]

RUN groupadd -g 1001 $USER_NAME && \
    useradd -g 1001 -m -s /bin/bash -u 1001 $USER_NAME

RUN mkdir -p /dev/net && \
    mknod /dev/net/tun c 10 200 && \
    chmod 600 /dev/net/tun

#COPY tcp /etc/openvpn
EXPOSE 8888

RUN sudo usermod -aG sudo user
#CMD openvpn --config /etc/openvpn/Belgium.Brussels.TCP.ovpn

USER $USER_NAME
SHELL ["/bin/bash", "-c"]
WORKDIR /home/$USER_NAME

VOLUME /home/$USER_NAME

RUN git clone git://git.yoctoproject.org/poky
WORKDIR /home/$USER_NAME/poky
RUN git checkout kirkstone
RUN git pull

ENV mode=build

CMD echo "Start Yocto Container: container_user=$USER_NAME, mode=$mode..."

CMD if [ $mode = build ]; then source oe-init-build-env && bitbake core-image-minimal && echo "Build Yocto end's successful!\nYou can run docker with mode=run"; \
	elif [ $mode = run ]; then source oe-init-build-env && runqemu slirp nographic bootparams="loglevel=0" qemux86-64 && echo "Run emulate was end's successful!"; \
	else echo "The mode was set incorrectly... Please enter (-e mode=build) or (-e mode=run)"; fi
