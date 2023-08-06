#include <openssl/sha.h>
#include <pthread.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define min(a,b)				\
    ({ __typeof__ (a) _a = (a);			\
	__typeof__ (b) _b = (b);		\
	_a < _b ? _a : _b; })


int INCORRECT = 42;
int CORRECT = 13;

int R;


void print32(unsigned char* buff){
    for(int i = 0; i< 32; i++){
	printf("%.02x", buff[i]);
    }
    printf("\n");
}

void sha256(unsigned char* out, unsigned char* in, int r){
    int i;
    memcpy(out, in, 32);
    for(i = 0; i < r; i++){
	SHA256_CTX context;
	SHA256_Init(&context);
	SHA256_Update(&context, out, SHA256_DIGEST_LENGTH);
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
    cores = 1;
    pthread_t threads[cores];
    int j = 0;
    while(j < checks){
	int spawn = min(cores, checks-j);
	for(int i = 0; i < spawn; i++){
	    pthread_create(&threads[i], NULL, check, &checkpoints[i+j]);
	}
	for(int i = 0; i < spawn; i++){
	    int* ret;
	    pthread_join(threads[i], (void**)&ret);
	    if(*ret != CORRECT){
		return j*cores + i;
	    }
	}
	j+= spawn;
    }
    return -1;
}
