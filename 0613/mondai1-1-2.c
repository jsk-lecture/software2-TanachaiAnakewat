/* test-minus.c */
#include <stdio.h>

int print_bit (unsigned short s) {
  int i;
  printf("0x%04x : ", s);
  for (i = 0; i < 16; i++) {
    printf("%c", ((0x8000)&s)?'1':'0');
    s = s << 1;
  }
  printf("\n");
}

int main (int argc, char* argv[]) {
  int i;
  unsigned short u1, u2, u3;
  u1 = 255; //下4桁 0255
  printf("u1 = "); print_bit(u1);
  printf("u1 = %d\n", u1);
  // 2's complement
  u2 = 322; //上4桁 0322
  u2 = (0xffff ^ u2) + 0x0001;
  printf("u2 = "); print_bit(u2);
  printf("u2 = %d\n", u2);
  printf("u2 = %d\n", (short)u2);
  u3 = u1 + u2;
  printf("u3 = ");  print_bit(u3);
}
