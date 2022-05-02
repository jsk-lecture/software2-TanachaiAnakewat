/* fact0.c */
#include <stdio.h>
#include <stdlib.h>

#define FALSE 0
#define TRUE 1
/*
* 引数：整数 x
* 返値：factorial of x
* 機能：xの階乗を計算し返す関数
*/
int fact (int x) {
 /* x の値が 0 より大きければ回帰的にx*(factx-1)を計算し，
そうでなければ１を返す */
  if (x > 0) {
#ifdef DEBUG
    printf("x = %d\n", x);
#endif
    return ( x * fact (x - 1) );
  } else {
#ifdef DEBUG
    printf("x = %d, return 1\n", x);
#endif
    return 1;
  }
}

int main (int argc, char *argv[]) {
  int x, ret;
  x = atoi(argv[1]);
  ret = fact(x);
  /* insert result of fact(x) in ret and print out */
  printf("ret = %d\n", ret);
}
