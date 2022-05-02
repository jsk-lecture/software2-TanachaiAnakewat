#include <stdio.h>

/*
* 引数：整数 i, j
* 返値：i と j の積となる整数
* 機能：引き数の積を計算し返す関数
*/
int test(int i, int j) {
return (i * j);
}
int main(int argc, char *argv) {
  /* 入力となる整数 i,j */
  /* i と j の積 */
int i,j,k;

 /* i と j を掛けて k に代入する */
i = 3;
j = 2;
k = test(i,j);
 /* k の値が 5 より大きければ">5"と表示し，
そうでなければ"<=5"を表示する */
if (k > 5) printf(">5\n");
else printf("<=5\n");

return 0;
} 
