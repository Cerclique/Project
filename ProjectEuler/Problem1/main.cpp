#include <iostream>

int main(int argc, char const *argv[])
{
  unsigned int result = 0;

  for(int i = 1; i < 1000; ++i)
  {
    if (i%3 == 0 || i%5 == 0)
      result += i;
  }

  std::cout << result << '\n';

  return 0;
}
