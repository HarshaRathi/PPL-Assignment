#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
int hour = -01;
int min = 00;
int sec = 00;

void *myfunhours(void *vargp){
    if(hour == -01 || min == 60){
        pthread_mutex_lock(&mutex1);
        hour = hour + 01;
        min=00;
        sec=00;
        pthread_mutex_unlock(&mutex1);
    }
    return NULL;
}

void *myfunmins(void *vargp){
    if(min<=60){
        pthread_mutex_lock(&mutex1);
        sleep(1);
        min = min + 01;
        sec=00;
        pthread_mutex_unlock(&mutex1);
    }
    return NULL;
}

void *myfunsecs(void *vargp){
    while(sec!=60){
        pthread_mutex_lock(&mutex1);
        sleep(1);
        printf("\n%2d",hour);
        printf(" :%2d",min);
        printf(" :%2d",sec);
        sec = sec + 01;
        pthread_mutex_unlock(&mutex1);
    }
    return NULL;
}

int main(){
    pthread_t thread_id1,thread_id2,thread_id3;
    printf("Start Clock");
    while(1){
        pthread_create(&thread_id1,NULL,myfunhours,NULL);
        sleep(1);
        pthread_create(&thread_id3,NULL,myfunsecs,NULL);
        sleep(1);
        pthread_create(&thread_id2,NULL,myfunmins,NULL);
        sleep(1);
        pthread_join(thread_id1,NULL);
        pthread_join(thread_id3,NULL);
        pthread_join(thread_id2,NULL);
    }
   return 0;
}