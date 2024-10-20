#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define CONFIG_FILE_PATH "C:/Users/Public/AppData/Local/Programs/GeoScript/config.env"

int writeToConfig(char *file, char *level, char *buildmode) {
    FILE *wstream;
    wstream = fopen(CONFIG_FILE_PATH, "w");

    fprintf(wstream, "file=%s\nlevel=%s\nbuildmode=%s", file, level, buildmode);
    fclose(wstream);

    return 0;
}

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
        if (strcmp(argv[1], "--help") == 0) {
            help();
        } else if (strcmp(argv[1], "--usage") == 0) {
            usage();
        } else if (strcmp(argv[1], "--version") == 0) {
            printf("GeoScript 1.0.0 ( windows-x64 )\n");
        } else if (strcmp(argv[1], "-c") == 0) {
            writeToConfig(argv[2], argv[3], "std");
            system("python C:/Users/Public/AppData/Local/Programs/GeoScript/main.py");
        } else if (strcmp(argv[1], "-gsc") == 0) {
            writeToConfig(argv[2], argv[3], "gsc");
            system("python C:/Users/Public/AppData/Local/Programs/GeoScript/main.py");
        } else {
            printf("Fatal error: invalid argument '%s'\n", argv[1]);
        }
    } else {
        usage();
    }

    return 0;
}