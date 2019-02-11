extern void Val_Set();
extern int Val_Get();

#include <iostream>
using namespace std;

int main() {
  Val_Set();
  cout << Val_Get() << endl;
  return 0;
}