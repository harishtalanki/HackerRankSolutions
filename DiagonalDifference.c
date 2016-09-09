#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    scanf("%d",&n);
    int a[n][n], pDiog =0, sDiog = 0;
    for(int a_i = 0; a_i < n; a_i++){
       for(int a_j = 0; a_j < n; a_j++){
         scanf("%d",&a[a_i][a_j]);
       }
    }
    for(int a_i = 0; a_i < n; a_i++){
        pDiog = pDiog + a[a_i][a_i];
        sDiog = sDiog + a[a_i][n - a_i - 1];
    }
    printf("%d",abs(pDiog-sDiog));
    return 0;
}