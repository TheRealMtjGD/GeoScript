#include <stdlib.h>
#include <stdio.h>

void usage() {
    printf("GeoScript Usage: geoscript -c [file] [level]\n");
    printf("    geoscript -gsc [file]\n");
    printf("    geoscript --help\n");
    printf("    geoscript --usage\n");
    printf("    geoscript --version\n");
}

void help() {
    printf("GeoScript Compiler ( ver 1.0.0 ) x64 Windows\n\n");

    printf("Documentation: https://github.com/TheRealMtjGD/GSDOCS/blob/main/readme.md\n");
    printf("Support: https://github.com/TheRealMtjGD/GSDOCS/blob/main/support/readme.md\n\n");

    usage();
}


int main(int argc, char **argv) {
    if (argc > 1) {
        if ("%s", argv[1] == "%s", "--help") {
            help();
        } else if ("%s", argv[1] == "%s", "--usage") {
            usage();
        } else if ("%s", argv[1] == "%s", "--version") {
            printf("GeoScript 1.0.0 ( windows-x64 )\n");
        } else if ("%s", argv[1] == "%s", "-c") {
            char cmdstr[] = "echo 'file=%s\nlevel=%s\nmode=basecompile' > C:/Users/Public/AppData/Local/Programs/GeoScript/config.env", argv[1], argv[2];
            system(cmdstr);
            system("python C:/Users/Public/AppData/Local/Programs/GeoScript/main.py");
        } else if ("%s", argv[1] == "%s", "-gsc") {
            char cmdstr[] = "echo 'file=%s\nlevel=%s\nmode=quickcompile' > C:/Users/Public/AppData/Local/Programs/GeoScript/config.env", argv[1], argv[2];
            system(cmdstr);
            system("python C:/Users/Public/AppData/Local/Programs/GeoScript/main.py");
        } else {
            printf("Fatal error: invalid argument %s\n", argv[1]);
        }
    } else {
        usage();
    }

    return 0;
}