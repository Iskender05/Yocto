import subprocess

def main():
    # Установка необходимых пакетов
    print("Установка необходимых пакетов...")
    subprocess.run(["sudo", "apt", "install", "gawk", "wget", "git", "diffstat", "unzip", "texinfo", "gcc", "build-essential", "chrpath", "socat", "cpio", "python3", "python3-pip", "python3-pexpect", "xz-utils", "debianutils", "iputils-ping", "python3-git", "python3-jinja2", "python3-subunit", "zstd", "liblz4-tool", "file", "locales", "libacl1"], check=True)
    
    # Генерация локали
    print("Генерация локали...")
    subprocess.run(["sudo", "locale-gen", "en_US.UTF-8"], check=True)
    
    # Клонирование репозитория Yocto Project и переключение на ветку kirkstone
    print("Клонирование репозитория Yocto Project...")
    subprocess.run(["git", "clone", "git://git.yoctoproject.org/poky"], check=True)
    subprocess.run(["cd", "poky"], shell=True)
    subprocess.run(["git", "branch", "-a"], check=True)
    subprocess.run(["git", "checkout", "kirkstone"], check=True)
    subprocess.run(["git", "pull"], check=True)
    
    # Инициализация среды сборки
    print("Инициализация среды сборки...")
    subprocess.run(["source", "oe-init-build-env"], shell=True)
    
    # Сборка образа
    print("Сборка образа...")
    subprocess.run(["bitbake", "core-image-minimal"], check=True)
    
    # Запуск QEMU
    print("Запуск QEMU...")
    subprocess.run(["runquemu", "qemux86_64"], check=True)

if __name__ == "__main__":
    main()
