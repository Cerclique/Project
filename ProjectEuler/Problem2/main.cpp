#include <iostream>

int main(int argc, char const *argv[])
{
  unsigned int x = 1;
  unsigned int y = 2;
  unsigned int temp = 0;
  unsigned int result = y;
  while (temp < 4000000)
  {
    temp = x + y;
    if (temp%2 == 0)
      result += temp;
    x = y;
    y = temp;
  }

  std::cout << result << std::endl;
  return 0;
}
