#include <stdlib.h>

int *name_value(size_t n, const char *const words[n]) {
    int *ptr = malloc(n * sizeof(int));
    if (ptr == NULL)
        return NULL;

    for (size_t i = 0; i < n; i++) {
        int word_sum = 0;
        for (const char *c = words[i]; *c != '\0'; c++) {
            if (*c >= 'a' && *c <= 'z')
                word_sum += *c - 'a' + 1;
        }
        ptr[i] = word_sum * (int)(i + 1);
    }
    return ptr;
}
