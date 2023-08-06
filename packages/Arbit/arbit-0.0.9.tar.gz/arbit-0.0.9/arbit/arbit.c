#include <openssl/sha.h>
#include <pthread.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define max(a,b)				\
    ({ __typeof__ (a) _a = (a);			\
	__typeof__ (b) _b = (b);		\
	_a > _b ? _a : _b; })


int INCORRECT = 1;
int CORRECT = 0;

int R;

void sha256(unsigned char* out, unsigned char* in, int r){
    int i;
    for(i = 0; i < r; i++){
	SHA256_CTX context;
	SHA256_Init(&context);
	SHA256_Update(&context, in, SHA256_DIGEST_LENGTH);
	SHA256_Final(out, &context);
    }
}

unsigned char** solve(unsigned char* seed, int r, int checks){
    unsigned char** checkpoints = malloc((checks+1)*sizeof(unsigned char*));
    checkpoints[0] = seed;
    for(int i = 0; i < checks; i++){
	checkpoints[i+1] = malloc(32);
	sha256(checkpoints[i+1], checkpoints[i], r/checks);
    }
    return checkpoints;
}

void* check(void* ptr){
    unsigned char** chain = ptr;
    unsigned char buffer[32];
    sha256(buffer, chain[0], R);
    if(memcmp(buffer, chain[1], 32) == 0){
	return &CORRECT;
    }
    else {
	return &INCORRECT;
    }
}

int verify(unsigned char** checkpoints, int r, int checks){
    R = r/checks;
    int cores = sysconf(_SC_NPROCESSORS_ONLN);
    pthread_t threads[cores];
    int j = 0;
    while(j < checks){
	int spawn = max(cores, checks-j);
	for(int i = j; i < j+spawn; i++){
	    pthread_create(&threads[i], NULL, check, &checkpoints[i]);
	}
	for(int i = 0; i < spawn; i++){
	    int* ret;
	    pthread_join(threads[i], (void**)&ret);
	    if(*ret == INCORRECT){
		return j*cores + i;
	    }
	}
	j+= spawn;
    }
    return -1;
}
