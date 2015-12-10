import os, sys
import platform


def system(command):
    retcode = os.system(command)
    if retcode != 0:
        raise Exception("Error while executing:\n\t %s" % command)


if __name__ == "__main__":
    system('conan export memsharded/testing')
    params = " ".join(sys.argv[1:])

    if platform.system() == "Windows":
        for version in ["12", "14"]:
            system('conan test -s compiler="Visual Studio" -s compiler.version=%s -s build_type=Debug '
                              '-s compiler.runtime=MTd -o SFML:static=True %s' % (version, params))
            system('conan test -s compiler="Visual Studio" -s compiler.version=%s -s build_type=Release '
                              '-s compiler.runtime=MT -o SFML:static=True %s' % (version, params))
            system('conan test -s compiler="Visual Studio" -s compiler.version=%s -s build_type=Debug '
                              '-s compiler.runtime=MDd -o SFML:static=False %s' % (version, params))
            system('conan test -s compiler="Visual Studio" -s compiler.version=%s -s build_type=Release '
                              '-s compiler.runtime=MD -o SFML:static=False %s' % (version, params))
    else:
        system('conan test -s compiler="gcc" -s build_type=Debug')
        system('conan test -s compiler="gcc" -s build_type=Release')
