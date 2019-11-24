
#include<string>
#include <map>

#ifndef CHR_H
#define CHR_H

class Chr
{
private:
  std::string chr_name;
  int start;
  int end;
  std::map<std::string, int> varaints;

public:
  Chr(std::string chr_name, int position);
  void SetChr(std::string chr_name, int position);
  void updatePosition(int position, int gap);
  void addVariant(std::string variant);
};
#endif
