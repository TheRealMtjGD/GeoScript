#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    char *cmd = "./gsmodules/Scripts/";

    for (int i; i<argc; i++) {
        cmd = "%s%s", cmd, argv[i];
    }
    system(cmd);

    return 0;
}